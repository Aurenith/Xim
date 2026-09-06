from pydantic import BaseModel
from enum import Enum

class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    SUPERADMIN = "SUPERADMIN"


class SignUpPayload(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None

class LogInPayload(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None
    xim_token: str | None = None

class AuthPayload(BaseModel):
    id: str
    user_token: str | None = None
    email: str | None = None
    role: Role


class TokenPayload(BaseModel):
    id: str
    username: str
    email: str
    image_url: str 