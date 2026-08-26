from fastapi import FastAPI, Request, APIRouter
import uvicorn

from controllers.api import user, auth
from controllers.api.router import api_router

app = FastAPI(title="Xim API")

api_router = APIRouter(prefix="/api/v1", tags=["api"])
app.include_router(api_router)
api_router.include_router(user.user_router)
api_router.include_router(auth.router)



@app.get("/")
async def home(request: Request) -> dict:
    return {"message": "Welcome to Xim"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)