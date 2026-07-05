from fastapi import FastAPI
from ejercicios.routers import books

app= FastAPI()
app.include_router(books.router)

@app.get("/")
async def root():
    return "API Biblioteca"

"""
para iniciar el servidor: uvicorn ejercicios.main_biblioteca:app --reload
"""