from fastapi import APIRouter, Request
from services.auth import user_authenticated_log

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/login")
def user_auth_login(request: Request) -> str:
    return  user_authenticated_log()