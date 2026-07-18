def book_schema(book) -> dict:
    return {
        "id": str(book["_id"]),   # Convertimos el ObjectId a un string común y corriente
        "title": book["title"],
        "author": book["author"],
        "year": book["year"],
        "available": book["available"]
    }

def books_schema(books) -> list:
    # Esta línea toma una lista de libros de la base de datos y los traduce uno por uno
    return [book_schema(book) for book in books]