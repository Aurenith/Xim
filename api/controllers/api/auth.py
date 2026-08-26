from fastapi import APIRouter, Request
from services.auth import user_authenticated_log, user_authenticated_sign
from models.auth_payload import SignUpPayload

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/login")
async def user_auth_login(request: Request) -> dict[str, str]:
    print("reached user_auth_login")
    return await user_authenticated_log(request)

@router.post("/signup")
async def user_auth_signup(payload: SignUpPayload) -> dict[str, str]:
    print("reached user_signup_login")
    return await user_authenticated_sign(payload)