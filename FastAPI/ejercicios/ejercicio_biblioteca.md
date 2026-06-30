# Ejercicios — API Biblioteca

Vas a construir una API completa para gestionar libros.
Cada ejercicio agrega una capa sobre la anterior.
Al final tenés una API funcional con CRUD, búsqueda y manejo de errores.

Trabajá en un solo archivo `biblioteca.py`.
Iniciá el servidor con:

    uvicorn biblioteca:app --reload

Probá cada ejercicio en Thunder Client antes de avanzar al siguiente.

---

## Ejercicio 1 — Modelo y datos

Creá el modelo `Book` con Pydantic con estos campos:
- `id`: entero
- `title`: string
- `author`: string
- `year`: entero
- `available`: booleano

Creá una lista `books_list` con al menos 4 libros de ejemplo.

---

## Ejercicio 2 — GET básico

Creá dos endpoints GET:
- `GET /books` → devuelve todos los libros usando el modelo
- `GET /booksjson` → devuelve los mismos libros como lista de diccionarios escritos a mano

Probá ambos en Thunder Client y comparalos en `/docs`.
Observá la diferencia en el schema que muestra Swagger para cada uno.

---

## Ejercicio 3 — Búsqueda por path y por query

Creá una función auxiliar `search_book(id: int)` que:
- Busque en `books_list` usando `filter` y `lambda`
- Si encuentra el libro, lo retorne
- Si no lo encuentra, lance `HTTPException` con código `404`

Usá esa función en dos endpoints:
- `GET /book/{id}` → búsqueda por path parameter
- `GET /book/` → búsqueda por query parameter

Probá con un ID que exista y con uno que no exista (ej: 99).

---

## Ejercicio 4 — POST

Creá un endpoint `POST /book` que agregue un libro nuevo a `books_list`.

Antes de agregarlo verificá que no exista ya un libro con el mismo `id`:
- Si existe → `HTTPException` código `400`
- Si no existe → agregalo a la lista y devolvelo con código `201`

---

## Ejercicio 5 — PUT

Creá un endpoint `PUT /book/{id}` que reemplace un libro completo.

- Si el libro no existe → `HTTPException` código `404`
- Si existe → reemplazalo en la lista y devolvé el libro actualizado

---

## Ejercicio 6 — DELETE

Creá un endpoint `DELETE /book/{id}` que elimine un libro de la lista.

- Si no existe → `HTTPException` código `404`
- Si existe → eliminalo y devolvé código `204`

---

## Ejercicio 7 — Query con filtro real

Creá un endpoint `GET /books/` que acepte un query parameter opcional
`available` de tipo booleano.

- Si se envía → filtrá y devolvé solo los libros donde `book.available` coincida
- Si no se envía → devolvé todos los libros

Pruebas:

    GET /books/                   → todos los libros
    GET /books/?available=true    → solo los disponibles
    GET /books/?available=false   → solo los no disponibles

---

## Flujo de prueba completo (Thunder Client)

Cuando termines todos los ejercicios, probá este flujo en orden:

    1.  GET  /books                → ver los 4 libros iniciales
    2.  GET  /booksjson            → comparar con /docs
    3.  GET  /book/2               → path param
    4.  GET  /book/?id=2           → query param, mismo resultado
    5.  GET  /book/99              → debe devolver 404
    6.  POST /book  body: {...}    → agregar libro nuevo
    7.  POST /book  body: mismo    → debe devolver 400
    8.  PUT  /book/5  body: {...}  → actualizar el recién creado
    9.  GET  /book/5               → verificar cambios
    10. GET  /books/?available=true → filtrar disponibles
    11. DELETE /book/5             → eliminar
    12. GET  /book/5               → debe devolver 404