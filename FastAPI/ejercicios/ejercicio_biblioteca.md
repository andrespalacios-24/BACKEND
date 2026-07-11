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

---

## Ejercicio 10 — Autorización OAuth2

Creá un nuevo archivo `ejercicios/routers/auth_users.py` con un sistema de autorización OAuth2 básico para usuarios de la biblioteca.

### Estructura del archivo

Creá el router en `routers/auth_users.py` e incluyelo en `main_biblioteca.py`.

### Qué hacer

**1. Modelos** — creá dos modelos Pydantic:

- `BibliotecaUser` con campos: `username`, `full_name`, `email`, `disabled`
- `BibliotecaUserDB` que herede de `BibliotecaUser` y agregue `password`

**2. Base de datos simulada** — creá un diccionario `biblioteca_users_db` con al menos dos usuarios:
- Uno activo (`disabled: False`)
- Uno deshabilitado (`disabled: True`)

**3. Funciones auxiliares** — creá:
- `search_user_db(username)` → devuelve `BibliotecaUserDB` (con password, uso interno)
- `search_user(username)` → devuelve `BibliotecaUser` (sin password, uso externo)

**4. Dependencia de autorización** — creá `current_user(token: str = Depends(oauth2))` que:
- Busque el usuario por token
- Lance `401` si no existe
- Lance `400` si está deshabilitado
- Devuelva el usuario si todo está bien

**5. Endpoints:**

- `POST /auth/login` — recibe form data (`username` + `password`), verifica credenciales, devuelve `access_token`
- `GET /auth/users/me` — protegido con `Depends(current_user)`, devuelve el usuario autenticado

### Flujo de prueba en Postman

    1. POST /auth/login
       Body → form-data: username=tu_usuario / password=tu_password
       → recibís {"access_token": "...", "token_type": "bearer"}

    2. GET /auth/users/me
       Headers: Authorization: Bearer <access_token>
       → devuelve los datos del usuario (sin password)

    3. GET /auth/users/me sin token
       → debe devolver 401

    4. POST /auth/login con el usuario deshabilitado
       GET /auth/users/me con ese token
       → debe devolver 400 "Usuario inactivo"

    5. POST /auth/login con contraseña incorrecta
       → debe devolver 400

### A tener en cuenta

- Usá `prefix="/auth"` en el router para que las rutas queden `/auth/login` y `/auth/users/me`
- El `tokenUrl` de `OAuth2PasswordBearer` debe coincidir con la ruta completa: `"auth/login"`
- El body del login va como **form-data** en Postman, no como JSON
- En `/docs` aparece el botón **Authorize** — podés probarlo ahí también

---

## Ejercicio 11 — Autorización con JWT

Creá un nuevo archivo `ejercicios/routers/jwt_auth_users.py` con el sistema de autorización OAuth2 + JWT para usuarios de la biblioteca. Este ejercicio reemplaza el token en texto plano del ejercicio 10 por un token cifrado con fecha de expiración.

### Instalación previa

```bash
pip install pyjwt
pip install "pwdlib[argon2]"
```

### Estructura del archivo

Creá el router en `routers/jwt_auth_users.py` e incluyelo en `main_biblioteca.py`.

### Qué hacer

**1. Constantes de configuración** — definí al inicio del archivo:

- `ALGORITHM = "HS256"`
- `ACCESS_TOKEN_DURATION` — minutos de validez del token (podés usar 1 para probar la expiración)
- `SECRET` — generá una clave con `secrets.token_hex(32)` desde la terminal Python

**2. Modelos** — igual que en el ejercicio 10 pero con nombres distintos para no colisionar:
- `JWTBibliotecaUser` con campos: `username`, `full_name`, `email`, `disabled`
- `JWTBibliotecaUserDB` que herede de `JWTBibliotecaUser` y agregue `password`

**3. Base de datos simulada** — creá `jwt_biblioteca_users_db` con al menos dos usuarios. Las contraseñas deben estar hasheadas con `pwdlib`. Para generarlas:

```python
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
print(password_hash.hash("tu_contraseña"))
```

**4. Funciones auxiliares** — igual que antes:
- `search_user_db(username)` → devuelve `JWTBibliotecaUserDB`
- `search_user(username)` → devuelve `JWTBibliotecaUser`

**5. Dependencias de autorización** — en JWT son dos funciones encadenadas:
- `auth_user(token)` → decodifica el JWT, extrae el `sub`, busca el usuario
- `current_user(user)` → verifica que el usuario no esté deshabilitado

**6. Endpoints:**
- `POST /jwt/login` — verifica credenciales con `password_hash.verify`, genera el token JWT con `sub` y `exp`, lo devuelve
- `GET /jwt/users/me` — protegido con `Depends(current_user)`, devuelve el usuario autenticado

### Cómo generar el SECRET

```python
import secrets
print(secrets.token_hex(32))
```

Copiá el resultado y pegalo como valor de `SECRET` en el archivo.

### Flujo de prueba en Postman

    1. POST /jwt/login
       Body → form-data: username=tu_usuario / password=tu_password
       → recibís {"access_token": "eyJhbGci...", "token_type": "bearer"}
       (el token ahora es un string cifrado largo, no el username)

    2. GET /jwt/users/me
       Headers: Authorization: Bearer eyJhbGci...
       → devuelve los datos del usuario sin password

    3. GET /jwt/users/me sin token
       → debe devolver 401

    4. POST /jwt/login con usuario deshabilitado → GET /jwt/users/me
       → debe devolver 400 "Usuario inactivo"

    5. Esperá que expire el token (según ACCESS_TOKEN_DURATION)
       GET /jwt/users/me con el token expirado
       → debe devolver 401

    6. Pegá el token en https://jwt.io y observá el payload decodificado

### A tener en cuenta

- Usá `prefix="/jwt"` en el router
- El `tokenUrl` de `OAuth2PasswordBearer` debe ser `"jwt/login"`
- El body del login va como **form-data** en Postman, no como JSON
- La diferencia clave con el ejercicio 10: el token es cifrado, las contraseñas están hasheadas y el token expira