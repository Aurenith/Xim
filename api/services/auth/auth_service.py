from fastapi import HTTPException, Request,Response
from lib.prisma.prisma import get_prisma_client
from models.auth_payload import LogInPayload, SignUpPayload,AuthPayload
from utils.hashing.hashing import hash_password, verify_password, create_access_token

async def user_authenticated_log(payload: LogInPayload, response: Response) -> dict[str, str]:
    ...
   
    # return {"message": "login successful", "userId": payload.user.id}
    username = payload.username
    email = payload.email

    prisma = await get_prisma_client()

    user = await prisma.user.find_unique(
        where={
           "email": email
        }
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )

    password = payload.password
       
    if not verify_password(
        payload.password,
        user.passwordHash,
    ):
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )


    token = create_access_token({"user_id": str(user.id), "username": str(user.username)})

    if not token: 
        return {
                "message": "login unsuccessful",
            }

    response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=60 * 60,
        )

    return {
        "message": "login successful",
        "userId": user.id,
        "token": str(token)
    }


async def user_authenticated_sign(payload: SignUpPayload) -> dict[str, str]:
    if not payload.username or not payload.password or not payload.email:
        raise HTTPException(status_code=400, detail="username, email and password are required")

    prisma = await get_prisma_client()

    existing_user = await prisma.user.find_first(
        where={
            "username":payload.username,
        }
    )
    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="username already exists",
        )

    user = await prisma.user.create(
        data={
            "username": payload.username,
            "email": payload.email,
            "passwordHash": hash_password(payload.password),
        }
    )

    return {"message": "user signup successful",
            "userID":user.id,
            }


async def user_authenticated_logout(response: Response) -> dict[str, str]:
    response.delete_cookie("access_token")
    return {"message": "logout successful"}