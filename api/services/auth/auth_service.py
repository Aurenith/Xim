from fastapi import HTTPException, Request
from lib.prisma.prisma import get_prisma_client
from models.auth_payload import LogInPayload, SignUpPayload,AuthPayload
from utils import hash_password, verify_password


async def user_authenticated_log(
    payload: LogInPayload,
) -> dict[str, str]:

    if not payload.username and not payload.email:
        raise HTTPException(
            status_code=400,
            detail="username or email is required",
        )

    if not payload.password:
        raise HTTPException(
            status_code=400,
            detail="password is required",
        )

    prisma = await get_prisma_client()

    if payload.username:
        user = await prisma.user.find_unique(
            where={
                "username": payload.username,
            }
        )
    else:
        user = await prisma.user.find_unique(
            where={
                "email": payload.email,
            }
        )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )

    if not user.passwordHash:
        raise HTTPException(
            status_code=401,
            detail="password authentication unavailable",
        )

    if not verify_password(
        payload.password,
        user.passwordHash,
    ):
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )

    return {
        "message": "login successful",
        "userId": user.id,
    }


async def user_authenticated_sign(payload: SignUpPayload) -> dict[str, str]:
    if not payload.username:
        raise HTTPException(
            status_code=400,
            detail="password is required"
        )

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
async def user_authenticated_logout(
    payload: AuthPayload,
) -> dict[str, str]:

    if not payload.sessionId:
        raise HTTPException(
            status_code=400,
            detail="sessionId is required",
        )

    prisma = await get_prisma_client()

    session = await prisma.session.find_unique(
        where={
            "sessionId": payload.sessionId,
        }
    )

    if not session:
        raise HTTPException(
            status_code=401,
            detail="invalid session",
        )

    await prisma.session.delete(
        where={
            "sessionId": payload.sessionId,
        }
    )

    return {
        "message": "logout successful",
    }