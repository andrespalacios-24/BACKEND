from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn users:app --reload para iniciar el servidor
app= FastAPI()

class user(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list= [
user(id= 1, name="rey",surname="naldo",url="reynaldo.com",age =35),
user(id=2, name="mai",surname="kel",url="maikel.com",age =24),
user(id=3, name="kiyo",surname="zaki",url="kiyozaki.com",age =55)
]

@app.get("/users")
async def users():
    return users_list

