from fastapi import FastAPI
from ejercicios.routers import books
from fastapi.staticfiles import StaticFiles
from fastapi import Cookie, FastAPI

app= FastAPI()
app.include_router(books.router)

@app.get("/")
async def root():
    return "API Biblioteca"

app.mount("/static", StaticFiles(directory="static"), name="static")

app.post("/login")
async def login():




"""
para iniciar el servidor: uvicorn ejercicios.main_biblioteca:app --reload
"""