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
    disabled: bool 

class BibliotecaUserDB(BibliotecaUser):
    password: str 


biblioteca_users_db = {
    "simon": {
        "username": "simon",
        "full_name": "Brais Moure",
        "email": "simon.com",
        "disabled": False,
        "password": "123456"
    },
    "ruperto": {
        "username": "ruperto",
        "full_name": "Brais Moure 2",
        "email": "ruperto.co",
        "disabled": True,
        "password": "654321"
    }
}

def search_user_db(username:str):
    if username in biblioteca_users_db:
        return BibliotecaUserDB(**biblioteca_users_db[username])
    
def search_user(username:str):
    if username in biblioteca_users_db:
        return BibliotecaUser(**biblioteca_users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/login")                                       
async def login(form: OAuth2PasswordRequestForm = Depends()): 
    user_db = biblioteca_users_db.get(form.username)          
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,          
            detail="El usuario no es correcto")                                      
    user = search_user_db(form.username)                      
    if not form.password == user.password:                    
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,          
            detail="La contraseña no es correcta")                                      
    return {"access_token": user.username, "token_type": "bearer"} 


@router.get("/users/me")
async def me(user: BibliotecaUser = Depends(current_user)):
    return user