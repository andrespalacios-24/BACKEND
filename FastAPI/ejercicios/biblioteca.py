from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Book (BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: bool

books_list= [
Book(id= 1, title= "Cien años de soledad", author= "Gabriel García Márquez", year= 1967, available= True),
Book(id= 2, title= "1984", author= "George Orwell", year= 1949, available= False),
Book(id= 3, title= "El señor de los anillos", author= "J.R.R. Tolkien", year= 1954, available= True),
Book(id= 4, title= "Don Quijote de la Mancha", author= "Miguel de Cervantes", year= 1605, available= True)
]

def search_book(id: int):
    books= filter(lambda book: book.id == id, books_list)
    try:
        return list(books)[0]
    except:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    
   
@app.get("/books", response_model=list[Book])
async def books():
    return books_list



@app.get("/booksjson")
async def booksjson():
    return  [
        {"id": 1, "title": "Cien años de soledad", "author": "Gabriel García Márquez", "year": 1967, "available": True},
        {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "available": False},
        {"id": 3, "title": "El señor de los anillos", "author": "J.R.R. Tolkien", "year": 1954, "available": True},
        {"id": 4, "title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes", "year": 1605, "available": True}
    ]

@app.get("/book/{id}")
async def book(id: int):
    return search_book(id)


@app.get("/book/")
async def book_query(id: int):
    return search_book(id)
# Para buscar por query param escribís en Thunder Client o navegador:
# GET http://127.0.0.1:8000/book/?id=1
# GET http://127.0.0.1:8000/book/?id=3
# El ?id= es el query param — el cliente envía el ID como parámetro nombrado
# FastAPI lo detecta automáticamente porque "id" no está en la ruta entre llaves


@app.get("/books/")
async def books_by_available(available: Optional[bool] = None):
    if available is None:
        return books_list
    return [b for b in books_list if b.available == available]

# GET http://127.0.0.1:8000/books/               → todos
# GET http://127.0.0.1:8000/books/?available=true  → solo disponibles
# GET http://127.0.0.1:8000/books/?available=false → solo no disponibles

@app.post("/book/", response_model=Book, status_code=201)
async def create_book(book: Book):
    # any() recorre books_list y devuelve True si algún libro ya tiene ese id
    # b es el nombre temporal de cada elemento en cada vuelta
    if any(b.id == book.id for b in books_list):
         raise HTTPException(status_code=400, detail="El libro ya existe")
    # si no hay duplicado, agrega el libro a la lista
    books_list.append(book)
    # devuelve el libro creado con status code 201
    return book

@app.put("/book/")
async def modificate_book(book: Book):
    for index, modify_book in enumerate(books_list):
        if modify_book.id == book.id:
            books_list[index] = book
            return book
    raise HTTPException(status_code=404, detail="No se ha actualizado el libro")

@app.delete("/book/{id}", status_code=204)
async def delete_book(id: int):
    for index, delete_book in enumerate(books_list):
        if delete_book.id == id:
            del books_list[index]
            return 
    raise HTTPException(status_code=404, detail="Libro no encontrado")