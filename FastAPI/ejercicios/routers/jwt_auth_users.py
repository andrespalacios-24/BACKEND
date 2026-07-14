from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
import jwt                                          
from jwt.exceptions import InvalidTokenError       
from pwdlib import PasswordHash 

ALGORITHM = "HS256"           
ACCESS_TOKEN_DURATION = 1   
SECRET = "eaf3aa7ee7ae058981c68447991a2fd5071326e2ec96a1aff7ed1dadb1dce5cc"

router = APIRouter(
    prefix="/jwt",
    tags=["jwt"]
)

oauth2 = OAuth2PasswordBearer(tokenUrl="jwt/login")
password_hash = PasswordHash.recommended()

class JWTBibliotecaUser(BaseModel):
     username: str
     full_name: str
     email: str
     disabled: bool 
    


class JWTBibliotecaUserDB (JWTBibliotecaUser):
    password: str 


jwt_biblioteca_users_db = {
    "danilo": {
        "username": "danilo",
        "full_name": "danilo jose",
        "email": "danilo.com",
        "disabled": True,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$eFn8Q+lQydvyigExOUJtaA$uoNqC78/m+Pv5LDMKoKYrsdpj7wwi0YppS7oxAiicvQ"  # DJ123456
    },
    "reinaldo": {
        "username": "reinaldo",
        "full_name": "reinaldo maicol",
        "email": "reinaldomaicol.com",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$mu558RmSrIRXdPZ27t5Img$2JU/5NDzqZbVzsEpHM32F/omG9P2E0AcDOYOA/cHb4U" # RM654321
    }
}

def search_user_db(username:str):
    if username in jwt_biblioteca_users_db:
        return JWTBibliotecaUserDB(**jwt_biblioteca_users_db[username])
    
def search_user(username:str):
    if username in jwt_biblioteca_users_db:
        return JWTBibliotecaUser(**jwt_biblioteca_users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",                             
        headers={"WWW-Authenticate": "Bearer"})   
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")  
        if username is None:
            raise exception
    except InvalidTokenError:                    
        raise exception
    return search_user(username)

async def current_user(user: JWTBibliotecaUser = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = jwt_biblioteca_users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not password_hash.verify(form.password, user.password):  # pwdlib
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    access_token = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: JWTBibliotecaUser = Depends(current_user)):
    return user