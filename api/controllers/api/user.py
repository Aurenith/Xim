from fastapi import APIRouter, Request

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get("/")
async def get_users(request: Request) -> dict:
    return {"message": "List of users", "headers": dict(request.headers)}