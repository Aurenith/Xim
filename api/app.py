from fastapi import FastAPI, Request
import uvicorn

from controllers.api import user, auth
from controllers.api.router import api_router

app = FastAPI(title="Xim API")

api_router.include_router(user.user_router)
api_router.include_router(auth.router)
app.include_router(api_router)



@app.get("/")
async def home(request: Request) -> dict:
    return {"message": "Welcome to Xim"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)