from fastapi import APIRouter, Request
from services.auth.auth_service import (
    user_authenticated_log,
    user_authenticated_sign,
    user_authenticated_logout as logout_services
)
from models.auth_payload import SignUpPayload,LogInPayload

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
async def user_auth_login(
    payload: LogInPayload,
) -> dict[str, str]:
    return await user_authenticated_log(payload)

@router.post("/signup")
async def user_auth_signup(payload: SignUpPayload) -> dict[str, str]:
    print("reached user_signup_login")
    return await user_authenticated_sign(payload)

@router.post("/logout")
async def user_auth_logout() -> dict[str, str]:
    print("reached user_logout")
    return await user_auth_logout(Request)