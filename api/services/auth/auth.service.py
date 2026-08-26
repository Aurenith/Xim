from fastapi import Request

def user_authenticated_log(request: Request): 
    return { "message": "user authenticated successfully" }   