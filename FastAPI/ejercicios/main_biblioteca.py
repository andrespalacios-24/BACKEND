from fastapi import FastAPI, Cookie, HTTPException, Header
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from ejercicios.routers import books, auth_users, jwt_auth_users
from typing import Optional


app = FastAPI()
app.include_router(books.router)
app.include_router(jwt_auth_users.router)
#app.include_router(auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "API Biblioteca"



@app.post("/login")
async def login():
    response = JSONResponse(content={"mensaje": "sesión iniciada"})
    response.set_cookie(
        key="biblioteca_session",    
        value="robert123",              
        httponly=True,              
        max_age=3600,                
        samesite="lax"               
    )
    return response

@app.get("/perfil")
async def perfil(biblioteca_session: Optional[str] = Cookie(default=None)):
    if biblioteca_session is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"session": biblioteca_session}

@app.post("/logout")
async def logout():
    response = JSONResponse(content={"mensaje": "sesión cerrada"})
    response.delete_cookie(key="biblioteca_session")  # mismo nombre siempre
    return response

@app.get("/headers")
async def headers(
    user_agent: Optional[str] = Header(default=None),  
    x_api_key: Optional[str] = Header(default=None)     
):
    response = JSONResponse(content={
        "user_agent": user_agent,    
        "api_key": x_api_key        
    })
    response.headers["X-Biblioteca-Version"] = "1.0"   
    return response

# para iniciar el servidor:             
# para activar el venv. source ~/BACKEND/FastAPI/.venv/bin/activate
# crear la clave para el secret: python -c "import secrets; print(secrets.token_hex(32))"