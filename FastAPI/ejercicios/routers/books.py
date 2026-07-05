from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
tags=["Books"],
responses={404: {"description": "No encontrado"}}
)
# en este caso en router=Apirouter se deja son prefix ya que existen:
#book y books y si dejo prefix book para hacer cualquier peticion para books seria
# s/ y no seria muy legible ni logico
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

    
   
@router.get("/books", response_model=list[Book])
async def books():
    return books_list



@router.get("/book/{id}")
async def book(id: int):
    return search_book(id)


@router.get("/book/")
async def book_query(id: int):
    return search_book(id)


@router.get("/books/")
async def books_by_available(available: Optional[bool] = None):
    if available is None:
        return books_list
    return [b for b in books_list if b.available == available]



@router.post("/book/", response_model=Book, status_code=201)
async def create_book(book: Book):
    if any(b.id == book.id for b in books_list):
         raise HTTPException(status_code=400, detail="El libro ya existe")
    books_list.append(book)
    return book

@router.put("/book/")
async def modificate_book(book: Book):
    for index, modify_book in enumerate(books_list):
        if modify_book.id == book.id:
            books_list[index] = book
            return book
    raise HTTPException(status_code=404, detail="No se ha actualizado el libro")

@router.delete("/book/{id}", status_code=204)
async def delete_book(id: int):
    for index, delete_book in enumerate(books_list):
        if delete_book.id == id:
            del books_list[index]
            return 
    raise HTTPException(status_code=404, detail="Libro no encontrado")