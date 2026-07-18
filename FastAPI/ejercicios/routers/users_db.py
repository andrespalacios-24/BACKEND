from fastapi import APIRouter, HTTPException, status
from typing import Optional
from db.models.book import User
from db.client import db_client

router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


books_list= []


def search_book(id: int):
    books= filter(lambda book: book.id == id, books_list)
    try:
        return list(books)[0]
    except:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    
   
@router.get("/books", response_model=list[Book])
async def books():
    return books_list



@router.get("/booksjson")
async def booksjson():
    return  [
        {"id": 1, "title": "Cien años de soledad", "author": "Gabriel García Márquez", "year": 1967, "available": True},
        {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "available": False},
        {"id": 3, "title": "El señor de los anillos", "author": "J.R.R. Tolkien", "year": 1954, "available": True},
        {"id": 4, "title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes", "year": 1605, "available": True}
    ]

@router.get("/{id}")
async def book(id: int):
    return search_book(id)


@router.get("/")
async def book_query(id: int):
    return search_book(id)
# Para buscar por query param escribís en Thunder Client o navegador:
# GET http://127.0.0.1:8000/book/?id=1
# GET http://127.0.0.1:8000/book/?id=3
# El ?id= es el query param — el cliente envía el ID como parámetro nombrado
# FastAPI lo detecta automáticamente porque "id" no está en la ruta entre llaves


@router.get("/")
async def books_by_available(available: Optional[bool] = None):
    if available is None:
        return books_list
    return [b for b in books_list if b.available == available]

# GET http://127.0.0.1:8000/books/               → todos
# GET http://127.0.0.1:8000/books/?available=true  → solo disponibles
# GET http://127.0.0.1:8000/books/?available=false → solo no disponibles

@router.post("/", response_model=Book, status_code= status.HTTP_201_CREATED)
async def create_book(book: Book):
    
   # if any(b.id == book.id for b in books_list):
         #raise HTTPException(status_code=400, detail="El libro ya existe")
    
    db_client.local

    books_list.append(book)
   
    return book

@router.put("/")
async def modificate_book(book: Book):
    for index, modify_book in enumerate(books_list):
        if modify_book.id == book.id:
            books_list[index] = book
            return book
    raise HTTPException(status_code=404, detail="No se ha actualizado el libro")

@router.delete("/{id}", status_code=204)
async def delete_book(id: int):
    for index, delete_book in enumerate(books_list):
        if delete_book.id == id:
            del books_list[index]
            return 
    raise HTTPException(status_code=404, detail="Libro no encontrado")