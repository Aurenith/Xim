from fastapi import APIRouter, Request

api_router = APIRouter(prefix="/api/v1", tags=["api"])


@api_router.get("")
async def api_index(request: Request) -> dict:
    return {"message": "Xim API v1", "headers": dict(request.headers)}


@api_router.get("/health/")
async def health_check() -> dict:
    return {"status": "ok"}

@api_router.get("/auth")
async def auth_check() -> dict:
    return {"status": "authenticated"}