from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/v1", tags=["api"])


@router.get("")
async def api_index(request: Request) -> dict:
    return {"message": "Xim API v1", "headers": dict(request.headers)}


@router.get("/health/")
async def health_check() -> dict:
    return {"status": "ok"}

@router.get("/auth")
async def auth_check() -> dict:
    return {"status": "authenticated"}