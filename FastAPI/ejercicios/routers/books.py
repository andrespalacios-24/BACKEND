from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from ejercicios.db.client import db_client
from ejercicios.db.models.book import Book
from ejercicios.db.schemas.book import book_schema, books_schema

router = APIRouter(
    prefix="/booksdb",
    tags=["booksdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)

# este endpoint se usa para leer en este caso todos los libros
@router.get("/", response_model=list[Book])
async def get_books():
    return books_schema(db_client.books.find())

def search_book(field: str, key):
    try:
        book_document = db_client.books.find_one({field: key})
        if not book_document:
            return None
        return Book(**book_schema(book_document))
    except:
        return None

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    if search_book("title", book.title) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El libro ya existe en la biblioteca"
        )

    book_dict = dict(book)
    del book_dict["id"]

    inserted_id = db_client.books.insert_one(book_dict).inserted_id
    new_book = book_schema(db_client.books.find_one({"_id": inserted_id}))
    
    return Book(**new_book)

@router.get("/{id}", response_model=Book)
async def get_book_by_id(id: str):
    book = search_book("_id", ObjectId(id))
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El libro no existe"
        )
        
    return book


@router.put("/{id}", response_model=Book)
async def update_book(id: str, book: Book):
    book_dict = dict(book)
    del book_dict["id"]
    
    try:
        
        from pymongo import ReturnDocument
        updated_document = db_client.books.find_one_and_replace(
            {"_id": ObjectId(id)}, 
            book_dict, 
            return_document=ReturnDocument.AFTER
        )
        
        
        if not updated_document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="No se encontró el libro para actualizar"
            )
            
        return Book(**book_schema(updated_document))
        
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se pudo actualizar el libro. Verifica el ID enviado"
        )
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: str):
    deleted_document = db_client.books.find_one_and_delete({"_id": ObjectId(id)})
    
    if not deleted_document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se encontró el libro que deseas eliminar"
        )