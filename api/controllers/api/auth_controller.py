
from fastapi import APIRouter
from controllers.api.auth_controller import router as auth_router
router = APIRouter(prefix="/api/v1", tags=["api"])
router.include_router(auth_router)