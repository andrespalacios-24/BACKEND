from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router= APIRouter (
prefix="/auth",
tags=["auth"]
)
oauth2 = OAuth2PasswordBearer(tokenUrl="auth/login")

class BibliotecaUser(BaseModel):
    username: str
    full_name: str
    email: str
    disnabled: bool 