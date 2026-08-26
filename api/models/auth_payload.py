from pydantic import BaseModel
from enum import Enum

class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    SUPERADMIN = "SUPERADMIN"


class SignUpPayload(BaseModel):
    sessionId: str
    email: str | None = None
    username: str | None = None
    password: str | None = None

class LogInPayload(BaseModel):
    sessionId: str
    email: str | None = None
    username: str | None = None
    password: str | None = None
    xim_token: str | None = None

class AuthPaylaod(BaseModel): 
    id: str 
    user_token: str | None = None
    email: str | None = None
    role: Role
    sessionId: str | None = None