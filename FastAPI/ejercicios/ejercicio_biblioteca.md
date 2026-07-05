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

## Ejercicio 8 — Routers

Reorganizá el código de `biblioteca.py` en la estructura de routers de MoureDev.

### Estructura objetivo

```
FastAPI/
└── ejercicios/
    ├── biblioteca.py          (ya existe, no lo toques)
    ├── main_biblioteca.py     (nuevo — punto de entrada)
    └── routers/
        └── books.py           (nuevo — router de libros)
```

### Qué hacer

**1.** Creá la carpeta `routers/` dentro de `ejercicios/`.

**2.** Creá `routers/books.py` con:
- `router = APIRouter()` con `prefix`, `tags` y `responses` a nivel de router
- El modelo `Book`, la lista `books_list` y la función `search_book` igual que en `biblioteca.py`
- Todos los endpoints adaptados usando `@router` en lugar de `@app`

**3.** Creá `ejercicios/main_biblioteca.py` con:
- La instancia `app = FastAPI()`
- La importación e inclusión del router de books
- Un endpoint raíz `GET /` que devuelva `"API Biblioteca"`

**4.** Iniciá el servidor siempre desde `FastAPI/`:

    uvicorn ejercicios.main_biblioteca:app --reload

**5.** Probá en Thunder Client que todos los endpoints siguen funcionando igual que antes.

### A tener en cuenta antes de escribir

Con `prefix="/book"` en el router, los decoradores ya no llevan el prefijo:

    @router.get("/")        →  GET /book/
    @router.get("/{id}")    →  GET /book/{id}
    @router.post("/")       →  POST /book/
    @router.put("/")        →  PUT /book/
    @router.delete("/{id}") →  DELETE /book/{id}

Pensá cómo quedan las rutas de `/books` y `/booksjson` con el prefijo aplicado antes de escribirlas.

---

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

---

## Ejercicio 9 — Recursos estáticos, Cookies y Headers

Agregá estas funcionalidades al proyecto con routers (`main_biblioteca.py`).

### Parte A — Recursos estáticos

**1.** Creá la carpeta `static/` dentro de `FastAPI/`.

**2.** Ponele adentro cualquier archivo — una imagen, un PDF, un `.txt`.

**3.** En `main_biblioteca.py` montá los archivos estáticos:

```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

**4.** Instalá `aiofiles` si no lo tenés:

    pip install aiofiles

**5.** Probá en el navegador o Postman:

    GET http://127.0.0.1:8000/static/nombre_del_archivo

---

### Parte B — Cookies

En `main_biblioteca.py` creá tres endpoints:

**`POST /login`** — que devuelva una cookie llamada `biblioteca_session` con cualquier valor,
`httponly=True` y `max_age=3600`.

**`GET /perfil`** — que lea la cookie `biblioteca_session`. Si existe devolvé su valor,
si no existe devolvé `HTTPException` código `401`.

**`POST /logout`** — que elimine la cookie `biblioteca_session`.

Probá el flujo en Postman:

    1. POST /login   → recibís la cookie
    2. GET /perfil   → leés la cookie (enviarla en Headers si Postman no la guarda)
    3. POST /logout  → eliminás la cookie
    4. GET /perfil   → debe devolver 401

---

### Parte C — Headers

Creá un endpoint **`GET /headers`** en `main_biblioteca.py` que:
- Lea el header `user-agent` de la petición
- Lea un header personalizado `x-api-key` de la petición
- Devuelva ambos valores en el body
- Agregue un header `X-Biblioteca-Version: 1.0` a la respuesta

Probalo en Postman agregando en la pestaña **Headers**:

    x-api-key: mi-clave-secreta