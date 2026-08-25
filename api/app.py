from fastapi import FastAPI, Request, APIRouter
import uvicorn

from controllers.api import user, products, auth
from controllers.api.router import router as api_router

app = FastAPI(title="Xim API")

api_router = APIRouter(prefix="/api/v1", tags=["api"])
app.include_router(api_router)
api_router.include_router(user.router)
# api_router.include_router(products.router)
api_router.include_router(auth.router)



@app.get("/")
async def home(request: Request) -> dict:
    return {"message": "Welcome to Xim", "headers": dict(request.headers)}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)