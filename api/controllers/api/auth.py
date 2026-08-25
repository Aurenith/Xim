from fastapi import APIRouter, Request


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/login")
def user_auth_login(request: Request) -> str:
    return  "user auth login route"