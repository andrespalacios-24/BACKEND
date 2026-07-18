## 1. Modelo de Datos (models.py u object_model.py)
    Define la estructura que FastAPI y Swagger usarán para validar la información. 

from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    # El id es opcional porque al crear un registro nuevo, MongoDB lo genera solito
    id: Optional[str] = None
    title: str
    author: str
    year: int
    available: bool

## 2. Esquema de Traducción (schemas.py)
Esta función limpia el formato nativo de MongoDB (_id como ObjectId) y lo traduce a un diccionario limpio con un id en texto plano (str).

def book_schema(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "year": book["year"],
        "available": book["available"]
    }

# Opcional: Para el endpoint que lista todo, transforma una lista de registros de MongoDB
def books_schema(books) -> list:
    return [book_schema(book) for book in books]


## 3. El Router Completo con el CRUD (routers/books.py)
Aquí está toda la lógica de tus endpoints. Copia y pega esto en tu archivo de rutas.

from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from pymongo import ReturnDocument

# IMPORTANTE: Asegúrate de importar tu cliente de base de datos, tu modelo y tus schemas
# Ejemplo:
# from ejercicios.db.client import db_client
# from ejercicios.models import Book
# from ejercicios.schemas import book_schema, books_schema

router = APIRouter(
    prefix="/booksdb",
    tags=["booksdb"]
)

# --- FUNCIÓN AUXILIAR DE BÚSQUEDA ---
def search_book(field: str, key):
    try:
        # Busca un solo registro que coincida con el campo y la clave dada
        book = db_client.books.find_one({field: key})
        return book
    except:
        return None


# --- 1. CREATE (Crear un registro) ---
@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    # Transformamos el modelo de Pydantic a un diccionario de Python
    book_dict = dict(book)
    
    # Eliminamos el id para que MongoDB genere su propio '_id' único
    del book_dict["id"]
    
    # Insertamos en la colección de la base de datos
    id = db_client.books.insert_one(book_dict).inserted_id
    
    # Buscamos el registro recién creado usando su nuevo ID
    new_book = search_book("_id", id)
    
    # Lo pasamos por el schema para limpiar el '_id' y lo retornamos validado
    return Book(**book_schema(new_book))


# --- 2. READ ALL (Obtener todos los registros) ---
@router.get("/", response_model=list[Book])
async def get_books():
    # .find() sin parámetros trae absolutamente todos los documentos de la colección
    raw_books = db_client.books.find()
    # Usamos el esquema de lista para transformar todos los registros a JSONs limpios
    return books_schema(raw_books)


# --- 3. READ ONE (Obtener un registro por ID) ---
@router.get("/{id}", response_model=Book)
async def get_book_by_id(id: str):
    # Convertimos la cadena de texto 'id' en un ObjectId nativo de MongoDB
    book = search_book("_id", ObjectId(id))
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El registro no existe"
        )
        
    return Book(**book_schema(book))


# --- 4. UPDATE (Actualizar un registro por ID) ---
@router.put("/{id}", response_model=Book)
async def update_book(id: str, book: Book):
    book_dict = dict(book)
    del book_dict["id"] # Evitamos conflictos de llaves fijas
    
    try:
        # Busca, reemplaza todo el contenido y nos devuelve el documento modificado (AFTER)
        updated_document = db_client.books.find_one_and_replace(
            {"_id": ObjectId(id)}, 
            book_dict, 
            return_document=ReturnDocument.AFTER
        )
        
        if not updated_document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="No se encontró el registro para actualizar"
            )
            
        return Book(**book_schema(updated_document))
        
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se pudo actualizar. Verifica el ID enviado"
        )


# --- 5. DELETE (Eliminar un registro por ID) ---
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: str):
    # Busca el documento, lo elimina y lo devuelve para verificar si existía
    deleted_document = db_client.books.find_one_and_delete({"_id": ObjectId(id)})
    
    if not deleted_document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se encontró el registro que deseas eliminar"
        )
    # Al ser un 204 No Content, FastAPI corta la respuesta de manera exitosa aquí

## Consejos rápidos para cuando vayas a rellenar esta plantilla:
Paso 1: Reemplaza la palabra books en db_client.books por el nombre que quieras que tenga tu nueva tabla/colección en MongoDB.

Paso 2: Cambia los campos dentro de Book(BaseModel) y book_schema por las propiedades de tu nuevo objeto (por ejemplo: si es un usuario, usa username, email, password, etc.).

Paso 3: No olvides registrar tu router en tu archivo principal main.py usando app.include_router(tu_nuevo_router).