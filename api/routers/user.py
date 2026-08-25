from fastapi import APIRouter, Request


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def get_users(request: Request) -> dict:
    return {"message": "List of users", "headers": dict(request.headers)}