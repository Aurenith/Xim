from fastapi import HTTPException, Request
from lib.prisma.prisma import get_prisma_client
from models.auth_payload import LogInPayload, SignUpPayload


async def user_authenticated_log(request: Request) -> dict[str, str]:
    """Create a user record for an authenticated request."""
    username = request.query_params.get("username")
    email = request.query_params.get("email")

    if not username:
        raise HTTPException(status_code=400, detail="username is required")

    prisma = await get_prisma_client()
    user = await prisma.user.create(
        data={
            "username": username,
            "email": email,
        }
    )

    return {
        "message": "user authenticated successfully",
        "userId": user.id,
    }


async def user_authenticated_sign(payload: SignUpPayload) -> dict[str, str]:
    return {"message": "user signup"}