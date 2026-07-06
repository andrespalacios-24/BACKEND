# HTTP y Desarrollo de APIs con FastAPI

Fuentes: [FastAPI Docs](https://fastapi.tiangolo.com/tutorial/) · [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) · [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)

---

## 1. Peticiones HTTP: operación GET

### Qué es

GET es el método HTTP para **solicitar información** de un servidor sin modificar nada. Es de solo lectura: no crea, no modifica, no elimina datos.

### Para qué sirve

- Obtener un recurso por su identificador: `GET /users/42`
- Listar recursos con filtros opcionales: `GET /products?category=libros&limit=10`
- Leer el estado actual de algo: `GET /orders/15/status`

### Características clave

| Característica | Valor  | Qué significa                                              |
|----------------|--------|------------------------------------------------------------|
| Seguro         | Sí     | No modifica datos en el servidor                           |
| Idempotente    | Sí     | Hacer la misma petición 10 veces da el mismo resultado     |
| Cuerpo (body)  | No     | GET no lleva body; los datos van en la URL                 |
| Cacheable      | Sí     | Los navegadores y proxies pueden guardar la respuesta      |

### Cómo se usa en FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

# GET simple — devuelve todos los usuarios
@app.get("/users")
async def get_users():
    return [{"id": 1, "nombre": "Andrés"}, {"id": 2, "nombre": "Laura"}]

# GET con path parameter — devuelve un usuario específico
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "nombre": "Andrés"}
```

Referencia: [FastAPI - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) · [MDN GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)

---

## 2. Creación de una API con FastAPI

### Qué es

Una API (Application Programming Interface) es un conjunto de endpoints que expone datos o funcionalidad de un backend para que otros sistemas o frontends puedan consumirlos de forma estructurada.

FastAPI permite construir una API REST en Python definiendo funciones decoradas con métodos HTTP.

### Estructura mínima de una API

```python
from fastapi import FastAPI

app = FastAPI(
    title="Mi API",
    description="API de ejemplo con FastAPI",
    version="0.1.0"
)

# Endpoint raíz — health check
@app.get("/")
async def root():
    return {"status": "ok"}
```

Los parámetros `title`, `description` y `version` aparecen en la documentación automática (`/docs`).

---

### Modelos con Pydantic (`BaseModel`)

#### Qué es

Pydantic es la librería de validación de datos que FastAPI usa internamente. Al definir una clase que hereda de `BaseModel`, se crea un **esquema** que describe la estructura de un objeto: sus campos y sus tipos.

#### Para qué sirve

- Validar automáticamente los datos que llegan en el body de una petición.
- Serializar objetos Python a JSON para devolverlos en la respuesta.
- Documentar la estructura de datos en Swagger UI (`/docs`).

#### Cómo se define

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
```

Cada atributo de la clase es un campo con su tipo anotado. Pydantic valida que los datos recibidos cumplan esos tipos. Si no, FastAPI devuelve `422` automáticamente.

---

### Diferencia entre devolver un dict y devolver un modelo Pydantic

El ejemplo de MoureDev muestra los dos enfoques en el mismo archivo:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Datos de prueba en memoria (simula una base de datos)
users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

# Opcion A: devolver lista de dicts escritos a mano
@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
        {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
        {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}
    ]

# Opcion B: devolver lista de objetos User (Pydantic los serializa a JSON)
@app.get("/users")
async def users():
    return users_list
```

| Aspecto          | Dict (`/usersjson`)                          | Modelo Pydantic (`/users`)                    |
|------------------|----------------------------------------------|-----------------------------------------------|
| Validacion       | Ninguna                                      | Automatica por Pydantic                       |
| Documentacion    | Sin schema en `/docs`                        | Schema completo visible en `/docs`            |
| Escalabilidad    | Dificil de mantener al crecer                | Centralizado en la clase                      |
| Serializacion    | Manual                                       | Automatica                                    |
| Uso recomendado  | Pruebas rapidas o respuestas muy simples     | Siempre que el dato tenga estructura definida |

La Opcion A existe para mostrar el contraste. En la practica siempre se usa Pydantic.

---

### Lista en memoria como base de datos temporal

Durante el aprendizaje es comun usar una lista de objetos Pydantic como almacenamiento temporal, antes de conectar una base de datos real. Permite desarrollar y probar todos los endpoints del CRUD sin configurar SQL todavia.

```python
users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    ...
]
```

Es un estado global en memoria: se pierde cada vez que se reinicia el servidor. Suficiente para aprender la logica de los endpoints.

---

### Estructura recomendada de proyecto

```
FastAPI/
├── main.py          # Punto de entrada, instancia de app, inclusion de routers
├── routers/         # Un archivo por recurso (users.py, products.py)
├── models/          # Modelos Pydantic (esquemas de datos)
└── .venv/           # Entorno virtual
```

### Cómo iniciar la API

```bash
source ~/BACKEND/FastAPI/.venv/bin/activate
uvicorn users:app --reload   # si el archivo se llama users.py
uvicorn main:app --reload    # si el archivo se llama main.py
```

Referencia: [FastAPI - Tutorial](https://fastapi.tiangolo.com/tutorial/) · [Pydantic - Models](https://docs.pydantic.dev/latest/concepts/models/)

---

## 3. Path y Query Parameters

### Qué son

Son las dos formas que tiene un cliente de enviar datos a un endpoint GET sin usar un body.

---

### El ejemplo de MoureDev: dos formas de buscar el mismo recurso

MoureDev implementa los dos tipos de parámetros sobre el mismo recurso (`User`) para mostrar el contraste. La lógica de búsqueda es idéntica en ambos casos — lo que cambia es cómo el cliente envía el ID.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

# Path parameter — el ID forma parte de la URL
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query parameter — el ID va como parámetro de consulta
@app.get("/user/")
async def user(id: int):
    return search_user(id)

# Función auxiliar compartida por ambos endpoints
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### 3.1 Path Parameters (parámetros de ruta)

#### Qué son

Valores que forman parte de la URL misma, definidos entre llaves `{}` en la ruta. El cliente los incluye directamente en la dirección.

```
GET /user/1   → busca el usuario con id=1
GET /user/3   → busca el usuario con id=3
```

#### Cómo lo detecta FastAPI

```python
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
```

FastAPI ve `{id}` en la ruta y sabe que el segmento de la URL en esa posición es el valor del parámetro. Lo convierte a `int` automáticamente. Si el cliente envía `/user/abc`, FastAPI devuelve `422` porque `"abc"` no es convertible a `int`.

El nombre del argumento en la función (`id`) debe coincidir exactamente con el nombre entre llaves en la ruta (`{id}`).

#### En qué casos usar path params

Cuando el valor **identifica** un recurso concreto y único. Sin ese valor, la ruta no tiene sentido:

```
/user/        → ¿qué usuario? no tiene sentido sin el ID
/user/1       → usuario 1, claro y directo
```

Convención REST: el identificador del recurso siempre va en la ruta.

---

### 3.2 Query Parameters (parámetros de consulta)

#### Qué son

Pares `clave=valor` que van al final de la URL después de `?`. El cliente los agrega explícitamente como parámetros nombrados.

```
GET /user/?id=1   → busca el usuario con id=1
GET /user/?id=3   → busca el usuario con id=3
```

#### Cómo lo detecta FastAPI

```python
@app.get("/user/")
async def user(id: int):
    return search_user(id)
```

FastAPI ve que `id` no está entre llaves en la ruta, entonces lo busca automáticamente en los query parameters de la URL. Si el cliente no envía `?id=...`, FastAPI devuelve `422` porque el parámetro es obligatorio (no tiene valor por defecto).

Para hacerlo opcional:

```python
from typing import Optional

@app.get("/user/")
async def user(id: Optional[int] = None):
    if id is None:
        return {"error": "Debes proporcionar un ID"}
    return search_user(id)
```

#### En qué casos usar query params

Cuando el parámetro **modifica o filtra** la búsqueda pero no es parte estructural de la ruta. También cuando puede ser opcional:

```
/users/              → todos los usuarios
/users/?role=admin   → solo los admins (filtro opcional)
/user/?id=1          → buscar por ID como filtro (estilo query)
```

---

### 3.3 La función auxiliar `search_user`

Ambos endpoints comparten la misma lógica de búsqueda extraída en una función separada. Esto evita repetir código (principio DRY: Don't Repeat Yourself).

```python
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

#### Qué hace línea por línea

`filter(lambda user: user.id == id, users_list)` — recorre `users_list` y devuelve un iterador con los elementos donde `user.id == id`. `filter` no ejecuta la búsqueda todavía, solo define el criterio.

`list(users)[0]` — convierte el iterador a lista y toma el primer elemento. Si el ID existe, hay exactamente un resultado (los IDs son únicos). Si no existe, la lista está vacía y `[0]` lanza `IndexError`.

`try / except` — captura el `IndexError` cuando la lista está vacía y devuelve un dict de error en lugar de que el servidor explote con `500`.

#### Limitación de este enfoque

Devolver `{"error": "..."}` con código `200 OK` es técnicamente incorrecto: el cliente recibe una respuesta exitosa aunque no se encontró el recurso. La forma correcta es usar `HTTPException`:

```python
from fastapi import HTTPException

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
```

MoureDev usa el dict de error para mantener el ejemplo simple. En una API real siempre se usa `HTTPException`.

---

### 3.4 Comparación directa

| Aspecto             | Path param `/user/{id}`     | Query param `/user/?id=1`          |
|---------------------|-----------------------------|------------------------------------|
| URL del cliente     | `/user/1`                   | `/user/?id=1`                      |
| Posición en la URL  | Dentro de la ruta           | Después de `?`                     |
| Declaración FastAPI | `{id}` en la ruta           | Argumento sin llaves en la función |
| Obligatorio         | Siempre                     | Depende del default                |
| Uso principal       | Identificar un recurso      | Filtrar, paginar, buscar           |
| Convención REST     | Estándar para IDs           | Estándar para filtros opcionales   |

#### Por qué MoureDev muestra los dos

Para dejar claro que **el resultado es idéntico** — ambos endpoints llaman a `search_user(id)` y devuelven lo mismo — pero la forma en que el cliente construye la URL es diferente. En la práctica, para buscar un recurso por ID se usa path param. El query param para ID es menos común pero válido, y aparece en algunas APIs antiguas o con necesidades específicas.

Referencia: [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) · [FastAPI - Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

---

## 4. Peticiones HTTP: POST, PUT y DELETE

### El ejemplo de MoureDev: CRUD completo sobre una lista en memoria

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

@app.post("/user/", response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user

@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### 4.1 POST — Crear un recurso

#### Qué es

Método para **enviar datos al servidor y crear un nuevo recurso**. Los datos van en el cuerpo (body) de la petición en formato JSON.

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — modifica datos |
| Idempotente    | No — dos POST iguales crean dos recursos distintos |
| Cuerpo (body)  | Sí — los datos van en el body como JSON |
| Código típico  | `201 Created` |

#### Cómo lo implementa MoureDev

```python
@app.post("/user/", response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user
```

**`response_model=User`** — le dice a FastAPI que la respuesta exitosa tiene la forma del modelo `User`. Esto aparece como schema en `/docs` y además filtra cualquier campo extra que no esté en el modelo antes de devolver la respuesta.

**`type(search_user(user.id)) == User`** — verifica si el resultado de `search_user` es un objeto `User`. Si lo es, el usuario ya existe y se devuelve el error. Si `search_user` devuelve el dict `{"error": "..."}`, la condición es `False` y se procede a agregar.

Esta es una forma válida para un ejemplo didáctico. En una API real se usaría `HTTPException`:

```python
@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return user
```

**`users_list.append(user)`** — agrega el objeto `User` directamente a la lista. Como `user` ya fue validado por Pydantic al entrar al endpoint, se garantiza que tiene todos los campos con los tipos correctos.

---

### 4.2 PUT — Actualizar un recurso completo

#### Qué es

Método para **reemplazar completamente** un recurso existente. Se envía el objeto entero con todos sus campos, no solo los que cambian.

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — modifica datos |
| Idempotente    | Sí — hacer el mismo PUT 10 veces deja el recurso en el mismo estado |
| Cuerpo (body)  | Sí — todos los campos del recurso |
| Código típico  | `200 OK` |

#### Cómo lo implementa MoureDev

```python
@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user
```

**El ID va en el body, no en la ruta** — a diferencia de la convención REST (`PUT /user/{id}`), MoureDev recibe el objeto completo incluyendo el `id` como parte del body (`PUT /user/`). El ID se usa internamente para encontrar qué elemento reemplazar. Ambos enfoques son válidos; la convención REST con path param es más común en producción.

**`enumerate(users_list)`** — devuelve pares `(índice, elemento)` para poder acceder a la posición y modificar la lista en ese lugar. Sin `enumerate` no tendrías el índice y no podrías hacer `users_list[index] = user`.

**`users_list[index] = user`** — reemplaza el elemento en esa posición con el nuevo objeto `User`. Esto es un reemplazo completo: todos los campos del usuario quedan con los valores del body recibido.

**`found = False` / `found = True`** — bandera para saber si el `for` encontró el usuario. El `if not found` después del `for` solo se ejecuta si ninguna iteración cumplió la condición.

---

### 4.3 DELETE — Eliminar un recurso

#### Qué es

Método para **eliminar un recurso** del servidor.

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — elimina datos |
| Idempotente    | Sí — eliminar algo que ya fue eliminado no cambia el estado |
| Cuerpo (body)  | No — el ID va en la ruta |
| Código típico  | `200 OK` o `204 No Content` |

#### Cómo lo implementa MoureDev

```python
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
```

**`del users_list[index]`** — elimina el elemento en esa posición de la lista. A diferencia de `pop(index)` que devuelve el elemento eliminado, `del` solo lo borra. Para DELETE no necesitamos el elemento eliminado, así que `del` es suficiente.

**Sin `return` en el caso exitoso** — cuando `found` es `True`, la función termina sin retornar nada explícitamente. FastAPI devuelve `200 OK` con body vacío. Para devolver `204 No Content` (más correcto semánticamente) se agrega `status_code=204` al decorador.

**El ID va en la ruta** — a diferencia del PUT, aquí MoureDev sí usa path param (`/user/{id}`). El DELETE no tiene body, así que el identificador del recurso a eliminar necesariamente va en la URL.

---

### 4.4 Patrón con bandera `found`

Los tres métodos de modificación (POST, PUT, DELETE) usan alguna forma de verificar si el recurso existe antes de operar. MoureDev usa el patrón de bandera booleana en PUT y DELETE:

```python
found = False
for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
        # operación
        found = True
if not found:
    return {"error": "..."}
```

Es un patrón claro para aprender. La alternativa con `HTTPException` es más correcta para una API real porque devuelve el código de estado adecuado (`404`) en lugar de un `200` con mensaje de error en el body.

---

### 4.5 Resumen de métodos HTTP

| Método | Acción           | Body | Idempotente | Código típico |
|--------|------------------|------|-------------|---------------|
| GET    | Leer             | No   | Sí          | 200           |
| POST   | Crear            | Sí   | No          | 201           |
| PUT    | Reemplazar todo  | Sí   | Sí          | 200           |
| DELETE | Eliminar         | No   | Sí          | 200 / 204     |

> **PATCH** (no siempre cubierto en cursos básicos): actualiza **parcialmente** un recurso. Solo se envían los campos que cambian. A diferencia de PUT, no requiere el objeto completo.

Referencia: [MDN - HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) · [FastAPI - Body](https://fastapi.tiangolo.com/tutorial/body/) · [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)

---

## 5. HTTP Status Codes

### Qué son

Códigos numéricos de 3 dígitos que el servidor devuelve en cada respuesta para indicar el resultado de la petición. El primer dígito define la categoría.

### Categorías

| Rango | Categoría     | Significado general                              |
|-------|---------------|--------------------------------------------------|
| 1xx   | Informational | La petición fue recibida, procesando             |
| 2xx   | Success       | La petición fue procesada correctamente          |
| 3xx   | Redirection   | El cliente debe ir a otra URL                    |
| 4xx   | Client Error  | El cliente envió algo incorrecto                 |
| 5xx   | Server Error  | El servidor falló al procesar una petición válida|

### Códigos más importantes en desarrollo de APIs

#### 2xx — Éxito

| Código | Nombre       | Cuándo usarlo                                        |
|--------|--------------|------------------------------------------------------|
| `200`  | OK           | GET, PUT, DELETE exitosos con cuerpo en la respuesta |
| `201`  | Created      | POST exitoso — recurso creado                        |
| `204`  | No Content   | DELETE exitoso sin cuerpo en la respuesta            |

#### 4xx — Error del cliente

| Código | Nombre                | Cuándo ocurre                                              |
|--------|-----------------------|------------------------------------------------------------|
| `400`  | Bad Request           | El servidor no entendió la petición por datos malformados  |
| `401`  | Unauthorized          | No hay credenciales o son inválidas                        |
| `403`  | Forbidden             | Las credenciales son válidas pero no tiene permiso         |
| `404`  | Not Found             | El recurso solicitado no existe                            |
| `422`  | Unprocessable Entity  | FastAPI: validación de tipos fallida (automático)          |

#### 5xx — Error del servidor

| Código | Nombre                | Cuándo ocurre                                              |
|--------|-----------------------|------------------------------------------------------------|
| `500`  | Internal Server Error | Error no manejado en el código del servidor                |
| `503`  | Service Unavailable   | El servidor no puede atender peticiones (sobrecarga, caído)|

### Diferencia entre 401 y 403

- `401`: el servidor no sabe **quién sos** (no enviaste token, o el token expiró).
- `403`: el servidor sabe quién sos pero **no tenés permiso** para ese recurso.

### Diferencia entre 400 y 422 en FastAPI

- `400`: error genérico de petición mal formada.
- `422`: específico de FastAPI/Pydantic — los datos llegaron pero no pasaron la validación de tipos. Incluye detalle de qué campo falló.

### Cómo devolver códigos específicos en FastAPI

#### `HTTPException` — lanzar errores HTTP

```python
from fastapi import FastAPI, HTTPException
```

`HTTPException` es una clase de FastAPI que interrumpe la ejecución del endpoint inmediatamente y devuelve una respuesta de error con el código y mensaje indicados. Se lanza con `raise`, no se retorna con `return`.

```python
raise HTTPException(status_code=404, detail="Usuario no encontrado")
```

| Parámetro     | Para qué sirve                                      |
|---------------|-----------------------------------------------------|
| `status_code` | Código HTTP de la respuesta de error                |
| `detail`      | Mensaje descriptivo que recibe el cliente en el body|

La respuesta que recibe el cliente:
```json
{
    "detail": "Usuario no encontrado"
}
```

---

### El ejemplo de MoureDev: HTTPException en el POST

MoureDev introduce `HTTPException` en el endpoint POST para manejar el caso de usuario duplicado:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user
```

**`raise HTTPException(status_code=404, detail="El usuario ya existe")`** — nota que MoureDev usa `404` para usuario duplicado. Técnicamente el código más correcto para "ya existe" sería `400` o `409 Conflict`, pero para el ejemplo didáctico el concepto importante es el uso de `HTTPException`, no el código específico.

**`return` vs `raise`** — esta es la diferencia clave:

| | Comportamiento |
|---|---|
| `return {"error": "..."}` | Devuelve `200 OK` con el dict en el body — el cliente recibe éxito aunque hubo error |
| `raise HTTPException(...)` | Interrumpe la ejecución y devuelve el código correcto — el cliente recibe el error real |

---

### Dónde debería usarse `HTTPException` en el CRUD completo

Aplicando `HTTPException` a todos los endpoints del ejemplo de MoureDev:

```python
# GET — recurso no encontrado
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# POST — recurso duplicado
@app.post("/user/", status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return user

# PUT — recurso no encontrado
@app.put("/user/")
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# DELETE — recurso no encontrado
@app.delete("/user/{id}", status_code=204)
async def delete_user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
```

Con `HTTPException` desaparece el patrón de bandera `found` — si el `for` termina sin encontrar el recurso, el `raise` después del `for` se ejecuta automáticamente.

Referencia: [FastAPI - HTTPException](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [MDN - Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 6. Routers

### Qué son

Los routers son la forma de **dividir los endpoints en archivos separados** según el recurso que manejan, y luego incluirlos en la aplicación principal.

### Para qué sirven

A medida que una API crece, tener todos los endpoints en `main.py` se vuelve imposible de mantener. Los routers permiten:

- Un archivo por recurso: `users.py`, `products.py`, `orders.py`
- Cada archivo define sus propias rutas con `APIRouter`
- `main.py` solo incluye los routers y queda limpio

---

### El ejemplo de MoureDev: tres archivos

MoureDev divide la API en tres archivos: `main.py`, `products.py` y `users.py`, todos dentro de una carpeta `routers/`.

```
FastAPI/
├── main.py
└── routers/
    ├── products.py
    └── users.py
```

---

#### `main.py` — punto de entrada

```python
from fastapi import FastAPI
from routers import products, users

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
```

**`from routers import products, users`** — importa los módulos `products.py` y `users.py` desde la carpeta `routers/`. Python trata la carpeta como un paquete.

**`app.include_router(products.router)`** — registra todas las rutas definidas en `products.py` dentro de la aplicación principal. A partir de este momento FastAPI conoce esos endpoints y los sirve.

`main.py` no tiene lógica de negocio — solo configura la app, incluye los routers y define las rutas globales (`/` y `/url`).

---

#### `routers/products.py` — router con `prefix` y `tags`

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"message": "No encontrado"}}
)

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]
```

**`router = APIRouter(...)`** — crea una instancia del router. Es equivalente a `app = FastAPI()` pero para un recurso específico. Los decoradores de los endpoints usan `@router` en lugar de `@app`.

**`prefix="/products"`** — prefijo que FastAPI agrega automáticamente a todas las rutas del router. `@router.get("/")` se convierte en `GET /products/` y `@router.get("/{id}")` se convierte en `GET /products/{id}`. No hace falta escribir `/products` en cada decorador.

**`tags=["products"]`** — agrupa los endpoints bajo la categoría "products" en `/docs`. Todos los endpoints del router aparecen juntos en Swagger.

**`responses={404: {"message": "No encontrado"}}`** — documenta en `/docs` que todos los endpoints de este router pueden devolver `404`. Se define una vez a nivel de router en lugar de repetirlo en cada endpoint.

**`products_list[id]`** — accede directamente por índice a la lista. Ojo: los índices empiezan en `0`, entonces `products_list[1]` devuelve `"Producto 2"`, no `"Producto 1"`. Es un ejemplo simple, en producción se buscaría por ID real.

---

#### `routers/users.py` — router sin `prefix`

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

@router.get("/usersjson")
async def usersjson():
    return [...]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@router.get("/user/")
async def user(id: int):
    return search_user(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user

@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user

@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

**`router = APIRouter()`** — sin parámetros. A diferencia de `products.py`, este router no tiene `prefix` ni `tags`. Las rutas se definen completas en cada decorador (`/users`, `/user/{id}`, etc.).

**`@router.get` en lugar de `@app.get`** — el único cambio real respecto a tener todo en `main.py`. El modelo, la lista y la lógica son exactamente iguales.

---

### Diferencia entre router con y sin `prefix`

| | `products.py` (con prefix) | `users.py` (sin prefix) |
|---|---|---|
| Definición | `router = APIRouter(prefix="/products")` | `router = APIRouter()` |
| Decorador | `@router.get("/")` | `@router.get("/users")` |
| Ruta final | `GET /products/` | `GET /users` |
| Ventaja | No repetís el prefijo en cada ruta | Más control sobre cada ruta |

Con `prefix` escribís menos — el prefijo se agrega solo. Sin `prefix` escribís la ruta completa en cada decorador pero tenés más flexibilidad si los endpoints del mismo recurso tienen rutas muy distintas.

---

### Cómo inicia el servidor con routers

```bash
uvicorn main:app --reload
```

Siempre desde `main.py` — es el punto de entrada. FastAPI carga los routers automáticamente a través de `include_router`.

---

### Múltiples routers

```python
from routers import users, products, orders

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
```

Cada router es independiente. Podés darles prefijos y tags distintos. El orden de `include_router` no afecta el funcionamiento, solo el orden en que aparecen en `/docs`.

---

### En qué casos usar routers

Desde el primer momento que tenés más de un recurso en la API. Es una buena práctica desde el inicio, no algo que se agrega después cuando el archivo ya está grande.

Referencia: [FastAPI - Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) · [FastAPI - APIRouter](https://fastapi.tiangolo.com/reference/apirouter/)

---

## 7. Recursos Estáticos, Cookies y Headers

### 7.1 Recursos estáticos

#### Qué son

Archivos que el servidor entrega tal cual están en disco: imágenes, CSS, JavaScript, PDFs, fuentes. No se procesan ni generan dinámicamente — el servidor los lee y los envía al cliente sin modificarlos.

#### Para qué sirven

En una API pura esto es menos común, pero es útil para servir imágenes de productos, archivos descargables, o una interfaz HTML simple junto a la API.

---

### El ejemplo de MoureDev

```python
from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
```

---

### Desglose línea por línea

```python
from fastapi.staticfiles import StaticFiles
```

`StaticFiles` es una clase de FastAPI que maneja la entrega de archivos estáticos. Se importa desde `fastapi.staticfiles`.

---

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

`app.mount()` registra una ruta en la aplicación que no es un endpoint normal sino un **montaje** — un punto donde FastAPI delega todas las peticiones a otro manejador, en este caso `StaticFiles`.

| Parámetro | Valor | Para qué sirve |
|-----------|-------|----------------|
| `"/static"` | Ruta de acceso | URL base desde donde se accede a los archivos |
| `StaticFiles(directory="static")` | Manejador | Indica qué carpeta del disco servir |
| `name="static"` | Nombre interno | Identificador para generar URLs internamente |

**`directory="static"`** — nombre de la carpeta en el disco relativa al punto desde donde se ejecuta uvicorn. Si corrés uvicorn desde `~/BACKEND/FastAPI/`, la carpeta `static/` debe estar en `~/BACKEND/FastAPI/static/`.

---

### Estructura de carpetas necesaria

```
FastAPI/
├── main.py
└── static/
    ├── imagen.png
    ├── documento.pdf
    └── styles.css
```

Acceso desde el navegador o Postman:

```
GET http://127.0.0.1:8000/static/imagen.png
GET http://127.0.0.1:8000/static/documento.pdf
GET http://127.0.0.1:8000/static/styles.css
```

FastAPI construye la ruta final sumando la ruta de montaje (`/static`) más el nombre del archivo.

---

### Diferencia entre `mount` y un endpoint normal

| | Endpoint normal | `app.mount` |
|---|---|---|
| Se define con | `@app.get(...)` | `app.mount(...)` |
| Devuelve | Lo que retorna la función | El archivo tal cual está en disco |
| Procesa lógica | Sí | No — entrega directa |
| Aparece en `/docs` | Sí | No |

Los archivos estáticos no aparecen en Swagger porque no son endpoints — son archivos servidos directamente sin pasar por lógica de Python.

---

### Instalación requerida

```bash
pip install aiofiles
```

`aiofiles` permite leer archivos de forma asíncrona. Sin él FastAPI lanza un error al intentar servir archivos estáticos.

---

### En qué casos usar recursos estáticos en una API

- Imágenes de productos o usuarios
- Archivos PDF descargables
- Una interfaz HTML mínima para probar la API
- Assets de un frontend servido junto a la API

En producción con un frontend separado (React, Vue) los archivos estáticos generalmente los sirve un servidor dedicado (Nginx, CDN) y no FastAPI directamente. Pero en proyectos pequeños o durante el desarrollo es completamente válido.

Referencia: [FastAPI - Static Files](https://fastapi.tiangolo.com/tutorial/static-files/) · [Starlette - StaticFiles](https://www.starlette.io/staticfiles/)

---

### 7.1.1 URLs — endpoint vs redirección

#### Qué son

Cuando querés exponer una URL externa desde tu API tenés dos opciones: devolverla como dato para que el cliente decida qué hacer, o redirigir al cliente directamente a esa URL.

---

#### Opción A — Devolver la URL como dato (endpoint normal)

```python
@app.get("/recurso")
async def recurso():
    return {"url": "https://ejemplo.com/algo"}
```

**Para qué sirve** — el cliente recibe la URL en el body JSON y decide qué hacer con ella: mostrarla, abrirla, guardarla. El cliente tiene control.

**En qué momento se usa:**
- Cuando el frontend necesita construir un enlace dinámico
- Cuando devolvés múltiples URLs para que el cliente elija
- Cuando la URL va junto a otros datos que vos definís en el código o sacás de la BD:

```python
@app.get("/recurso")
async def recurso():
    return {
        "url": "https://ejemplo.com/algo",
        "nombre": "Recurso importante",   # vos lo definís
        "tipo": "pdf"                      # vos lo definís
    }
```

---

#### Opción B — Redirección directa (`RedirectResponse`)

```python
from fastapi.responses import RedirectResponse

@app.get("/recurso")
async def recurso():
    return RedirectResponse(url="https://ejemplo.com/algo")
```

**Para qué sirve** — el servidor le dice al cliente "andá a esta URL" y el navegador va automáticamente sin que el usuario haga nada. El cliente no recibe JSON — recibe un código `307 Temporary Redirect` con la URL de destino en el header `Location`.

**En qué momento se usa:**
- Links de descarga que apuntan a otra ubicación
- Después de un login exitoso para redirigir al dashboard
- URLs cortas que redirigen a URLs largas (acortadores de URL)
- Cuando una ruta cambió y querés mantener compatibilidad con la URL anterior

```python
# URL corta que redirige a la documentación completa
@app.get("/docs-externa")
async def docs_externa():
    return RedirectResponse(url="https://fastapi.tiangolo.com/tutorial/")

# Después de login exitoso
@app.post("/login")
async def login():
    # verificar credenciales...
    return RedirectResponse(url="/dashboard", status_code=303)
```

---

#### Códigos de redirección

| Código | Nombre | Cuándo usarlo |
|--------|--------|---------------|
| `301` | Moved Permanently | La URL cambió para siempre |
| `302` | Found | Redirección temporal (default en algunos casos) |
| `303` | See Other | Después de un POST exitoso — redirigir a GET |
| `307` | Temporary Redirect | Redirección temporal manteniendo el método HTTP (default de FastAPI) |

---

#### Comparación directa

| Aspecto | Endpoint normal | `RedirectResponse` |
|---------|----------------|-------------------|
| Qué recibe el cliente | JSON con la URL | Código 3xx + header `Location` |
| El navegador va automáticamente | No | Sí |
| El cliente tiene control | Sí | No |
| Uso típico | Frontend que construye links | Redirecciones transparentes |

Referencia: [FastAPI - Response](https://fastapi.tiangolo.com/advanced/response-directly/) · [MDN - Redirections](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)

---

### 7.2 Cookies

#### Qué son

Pequeños fragmentos de datos que el servidor envía al cliente y el cliente almacena y reenvía automáticamente en cada petición siguiente al mismo dominio.

HTTP es un protocolo **stateless** (sin estado) — cada petición es independiente y el servidor no recuerda las anteriores. Las cookies son el mecanismo que permite mantener estado entre peticiones sin que el cliente tenga que enviar sus credenciales cada vez.

#### Para qué sirven

- Mantener sesiones de usuario activas (login)
- Guardar preferencias del cliente (idioma, tema, carrito de compras)
- Rastreo de actividad entre peticiones

---

#### Flujo completo de una cookie de sesión

```
1. Cliente → POST /login  (envía usuario y contraseña)
2. Servidor verifica credenciales → genera session_id
3. Servidor → respuesta con Set-Cookie: session_id=abc123
4. Cliente almacena la cookie automáticamente
5. Cliente → GET /perfil  (el navegador adjunta la cookie automáticamente)
6. Servidor lee la cookie → identifica al usuario → devuelve su perfil
```

El cliente no necesita reenviar usuario y contraseña en cada petición — la cookie actúa como prueba de identidad temporal.

---

#### Cómo leer cookies en FastAPI

```python
from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

# PERFIL — lee la cookie
@app.get("/perfil")
async def get_perfil(biblioteca_session: Optional[str] = Cookie(default=None)):
    #                 ^^^^^^^^^^^^^^^^^^                          ^^^^^^^^^^^^^^^^
    #                 nombre igual al key del set_cookie          le dice a FastAPI que viene de las cookies
    if biblioteca_session is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"session": biblioteca_session}
```

**`Cookie(default=None)`** — le dice a FastAPI que el parámetro viene de las cookies de la petición, no del body ni de la URL. El `default=None` la hace opcional — si el cliente no envía la cookie, el valor es `None`.

FastAPI lee automáticamente el header `Cookie` de la petición y extrae el valor con el nombre que declaraste.

---

#### Cómo escribir cookies en la respuesta

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# LOGIN — crea y entrega la cookie
@app.post("/login")
async def login():
    # En producción aquí verificarías usuario y contraseña
    response = JSONResponse(content={"mensaje": "sesión iniciada"})
    response.set_cookie(
        key="biblioteca_session",    # nombre de la cookie — vos lo definís
        value="ABC123",              # valor del carnet — en producción sería un token generado
        httponly=True,               # JS del navegador no puede leerla
        max_age=3600,                # expira en 1 hora (segundos)
        samesite="lax"               # protección contra CSRF
        # secure=True               # agregar en producción cuando hay HTTPS
    )
    return response
```

**`JSONResponse`** — en lugar de devolver directamente un dict, creás un objeto de respuesta para poder manipularlo antes de enviarlo. Esto permite agregar cookies, headers personalizados, etc.

**`set_cookie()`** — agrega la cookie al header `Set-Cookie` de la respuesta. El navegador la recibe y la almacena automáticamente.

---

#### Parámetros de `set_cookie`

| Parámetro   | Para qué sirve                                              | Valor recomendado |
|-------------|-------------------------------------------------------------|-------------------|
| `key`       | Nombre de la cookie                                         | `"session_id"`    |
| `value`     | Valor de la cookie                                          | Token generado    |
| `httponly`  | JS del navegador no puede leer la cookie — protege contra XSS | `True`        |
| `secure`    | Solo se envía por HTTPS — protege en tránsito               | `True` en producción |
| `max_age`   | Segundos hasta que expira                                   | `3600` (1 hora)   |
| `samesite`  | Protege contra CSRF                                         | `"lax"`           |

**`samesite` explicado:**
- `"strict"` — la cookie solo se envía si la petición viene del mismo dominio. Máxima protección pero puede romper flujos de redirección.
- `"lax"` — permite enviar la cookie en navegación normal pero no en peticiones cross-site. Balance entre seguridad y usabilidad. Es el valor recomendado.
- `"none"` — sin restricción. Requiere `secure=True`.

---

#### Cómo eliminar una cookie

```python
# LOGOUT — destruye la cookie
@app.post("/logout")
async def logout():
    response = JSONResponse(content={"mensaje": "sesión cerrada"})
    response.delete_cookie(
        key="biblioteca_session"    # mismo nombre que en set_cookie
    )
    return response
```

`delete_cookie()` le dice al navegador que elimine esa cookie. El nombre debe coincidir exactamente con el `key` que usaste en `set_cookie`.

---

#### Los tres endpoints juntos — el flujo completo

```python
from fastapi import FastAPI, Cookie, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

# 1. LOGIN — genera y entrega el carnet
@app.post("/login")
async def login():
    response = JSONResponse(content={"mensaje": "sesión iniciada"})
    response.set_cookie(
        key="biblioteca_session",    # nombre de la cookie
        value="ABC123",              # en producción: token generado automáticamente
        httponly=True,               # JS no puede leerla
        max_age=3600,                # expira en 1 hora
        samesite="lax"               # protección CSRF
    )
    return response

# 2. PERFIL — verifica el carnet
@app.get("/perfil")
async def perfil(biblioteca_session: Optional[str] = Cookie(default=None)):
    #             ^^^^^^^^^^^^^^^^^^                          ^^^^^^^^^^^^^^^^
    #             mismo nombre que el key                     indica que viene de cookies
    if biblioteca_session is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"session": biblioteca_session}

# 3. LOGOUT — destruye el carnet
@app.post("/logout")
async def logout():
    response = JSONResponse(content={"mensaje": "sesión cerrada"})
    response.delete_cookie(key="biblioteca_session")  # mismo nombre siempre
    return response
```

---

#### Cómo probar cookies en Postman

En Postman, la pestaña **Cookies** (arriba a la derecha) muestra las cookies que el servidor devuelve. Para enviar una cookie manualmente:

1. Pestaña **Headers** de la petición
2. Agregás el header: `Cookie` → `session_id=abc123`

O usás el gestor de cookies de Postman que las almacena automáticamente entre peticiones.

Referencia: [FastAPI - Cookie Parameters](https://fastapi.tiangolo.com/tutorial/cookie-params/) · [MDN - Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) · [MDN - Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)

---

### 7.3 Headers

#### Qué son

Metadatos que viajan junto a cada petición o respuesta HTTP, fuera del cuerpo. Son pares clave-valor que transmiten información sobre la petición, la respuesta o el cliente.

Toda petición HTTP tiene headers — aunque no los definas explícitamente, el cliente y el servidor agregan los básicos automáticamente (`Content-Type`, `Accept`, `Host`, etc.).

---

#### Dirección de los headers

| Dirección | Quién los envía | Para qué |
|-----------|----------------|----------|
| Request headers | El cliente | Informar al servidor sobre la petición |
| Response headers | El servidor | Informar al cliente sobre la respuesta |

---

#### Headers más comunes en APIs REST

| Header | Dirección | Para qué sirve | Ejemplo |
|--------|-----------|----------------|---------|
| `Content-Type` | Request / Response | Tipo de dato del body | `application/json` |
| `Authorization` | Request | Token de autenticación | `Bearer eyJhbGci...` |
| `Accept` | Request | Formato que acepta el cliente | `application/json` |
| `Cache-Control` | Response | Instrucciones de caché | `no-cache`, `max-age=3600` |
| `User-Agent` | Request | Identifica el cliente | `Mozilla/5.0...` |
| `X-Request-ID` | Request / Response | ID para rastrear peticiones en logs | `abc-123-def` |

---

#### Cómo leer headers de la petición en FastAPI

```python
from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.get("/info")
async def get_info(user_agent: Optional[str] = Header(default=None)):
    return {"user_agent": user_agent}
```

**`Header(default=None)`** — le dice a FastAPI que el parámetro viene de los headers de la petición. FastAPI convierte automáticamente guiones a guiones bajos: `user-agent` → `user_agent`.

Para leer múltiples headers:

```python
@app.get("/info")
async def get_info(
    user_agent: Optional[str] = Header(default=None),
    accept_language: Optional[str] = Header(default=None),
    authorization: Optional[str] = Header(default=None)
):
    return {
        "user_agent": user_agent,
        "language": accept_language,
        "auth": authorization
    }
```

---

#### Cómo agregar headers a la respuesta

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/datos")
async def get_datos():
    response = JSONResponse(content={"data": "valor"})
    response.headers["X-Custom-Header"] = "mi-valor"
    response.headers["Cache-Control"] = "no-cache"
    return response
```

Igual que con las cookies, usás `JSONResponse` para manipular la respuesta antes de enviarla. Los headers se agregan como un diccionario.

---

#### Headers de autenticación — el más importante en APIs

El header `Authorization` es el estándar para proteger endpoints. El esquema más usado es **Bearer token**:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

En FastAPI se lee así:

```python
@app.get("/protected")
async def protected(authorization: Optional[str] = Header(default=None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    # verificar el token
    return {"mensaje": "acceso permitido"}
```

Esto lo vas a ver en detalle en el tema de **Autorización** que viene más adelante en el curso.

---

#### Diferencia entre headers, cookies y query params para autenticación

| Mecanismo | Cómo viaja | Uso típico |
|-----------|-----------|------------|
| Header `Authorization` | En el header de cada petición | APIs REST — el más común |
| Cookie | Automático en el navegador | Aplicaciones web con sesiones |
| Query param `?token=...` | En la URL | Desaconsejado — queda en logs |

---

#### La convención `X-`

Los headers que empiezan con `X-` son personalizados (no estándar):

```
X-Request-ID: abc-123
X-API-Version: 2.0
X-RateLimit-Remaining: 99
```

Aunque fue deprecada formalmente por la RFC 6648, sigue siendo muy usada en la práctica para headers propios de la aplicación.

---

#### Cómo ver headers en Postman

En la respuesta de cualquier petición, la pestaña **Headers** muestra todos los headers que devolvió el servidor. FastAPI siempre incluye al menos:

```
content-type: application/json
content-length: 42
```

Para enviar headers en una petición, usás la pestaña **Headers** antes de hacer Send — agregás la clave y el valor.

Referencia: [FastAPI - Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/) · [MDN - HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) · [MDN - Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

---

## 8. CRUD

### Qué es

CRUD es el acrónimo de las cuatro operaciones básicas que se pueden hacer sobre cualquier dato:

| Letra | Operación | Método HTTP | Qué hace                        |
|-------|-----------|-------------|---------------------------------|
| C     | Create    | POST        | Crear un nuevo recurso          |
| R     | Read      | GET         | Leer uno o varios recursos      |
| U     | Update    | PUT / PATCH | Modificar un recurso existente  |
| D     | Delete    | DELETE      | Eliminar un recurso             |

Casi toda API REST es, en su base, un CRUD sobre uno o más recursos. Cuando MoureDev habla de "hacer el CRUD de usuarios", significa implementar los cuatro endpoints que permiten crear, leer, actualizar y eliminar usuarios.

### Para qué sirve

Es el patrón de referencia para organizar los endpoints de un recurso. Antes de agregar lógica compleja, una API bien hecha tiene los cuatro endpoints CRUD funcionando correctamente.

---

### El código de MoureDev: CRUD completo

Este es el archivo completo de MoureDev con todos los endpoints. Es la referencia base del curso:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]

# READ — todos
@app.get("/users")
async def users():
    return users_list

# READ — por path param
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# READ — por query param
@app.get("/user/")
async def user(id: int):
    return search_user(id)

# CREATE
@app.post("/user/", response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user

# UPDATE
@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user

# DELETE
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Función auxiliar
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### Desglose de cada operación

#### R — Read

**`GET /users`** devuelve toda la lista directamente.

**`GET /user/{id}` y `GET /user/`** delegan a `search_user`. La función usa `filter` + `lambda` para recorrer la lista y `try/except` para capturar el `IndexError` cuando no hay resultado:

```python
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
```

El `except` devuelve un dict con código `200`. Es suficiente para aprender, pero en producción se usa `HTTPException(status_code=404)` para que el cliente reciba el código correcto.

---

#### C — Create

```python
@app.post("/user/", response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user
```

**`type(search_user(user.id)) == User`** — llama a `search_user` y chequea si lo que devuelve es un objeto `User`. Si lo es, el usuario ya existe. Si devuelve el dict de error, la condición es `False` y se procede.

**`response_model=User`** — le indica a FastAPI que documente la respuesta exitosa con el schema de `User` en `/docs`. También filtra campos extra que no estén en el modelo antes de devolver la respuesta.

Versión con `HTTPException` (más correcta para producción):

```python
@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return user
```

---

#### U — Update

```python
@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user
```

**El ID va en el body**, no en la ruta. MoureDev recibe el objeto `User` completo (incluyendo el `id`) y busca por ese campo internamente. La convención REST estándar sería `PUT /user/{id}` con el ID en la ruta, pero ambos enfoques son válidos.

**`enumerate`** devuelve pares `(índice, elemento)`. Sin él no tendrías el índice y no podrías hacer `users_list[index] = user` para reemplazar en esa posición.

**`found = False` / `found = True`** — bandera booleana. El `if not found` después del `for` solo se ejecuta si ninguna iteración encontró el usuario.

---

#### D — Delete

```python
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
```

**`del users_list[index]`** elimina el elemento en esa posición. A diferencia de `pop(index)` que devuelve el elemento eliminado, `del` solo lo borra sin devolver nada — suficiente para DELETE donde no necesitás el elemento.

**Sin `return` en el caso exitoso** — cuando `found` es `True` la función termina sin retornar nada. FastAPI devuelve `200 OK` con body vacío. Para `204 No Content` (semánticamente más correcto) se agrega `status_code=204` al decorador.

---

### Comparación: estilo MoureDev vs producción

| Aspecto                  | Estilo MoureDev (curso)              | Producción                              |
|--------------------------|--------------------------------------|-----------------------------------------|
| Error "no encontrado"    | `return {"error": "..."}` con `200`  | `raise HTTPException(status_code=404)`  |
| Error "ya existe"        | `return {"error": "..."}` con `200`  | `raise HTTPException(status_code=400)`  |
| Verificar existencia     | `type(search_user(id)) == User`      | `any()` o `next()` con `None`           |
| Buscar elemento          | `filter` + `lambda` + `try/except`   | `next((u for u in lista if ...), None)` |
| Eliminar de lista        | `del lista[index]`                   | `lista.pop(index)`                      |
| DELETE exitoso           | Sin `return`, código `200`           | `return` vacío con `status_code=204`    |

El estilo del curso es más legible para aprender. La versión de producción usa los status codes correctos para que los clientes puedan manejar los errores apropiadamente.

---

### Flujo de prueba del CRUD en Thunder Client / Postman

```
1. GET  /users              → ver los 3 usuarios iniciales
2. POST /users  body: {...} → agregar un usuario nuevo
3. GET  /users              → verificar que aparece el nuevo
4. GET  /users/4            → leer solo el usuario recién creado
5. PUT  /users/4  body: {...} → actualizar sus datos
6. GET  /users/4            → verificar los datos actualizados
7. DELETE /users/4          → eliminar
8. GET  /users/4            → debe devolver 404
```

### Limitación de la lista en memoria

Al reiniciar el servidor (`Ctrl+C` y `uvicorn ... --reload`), `users_list` vuelve a su estado inicial. Los cambios no persisten. Esto es esperado en esta etapa del aprendizaje. La persistencia real se agrega conectando una base de datos (SQLite, PostgreSQL) más adelante en el roadmap.

Referencia: [FastAPI - Body](https://fastapi.tiangolo.com/tutorial/body/) · [FastAPI - HTTPException](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

---

## 9. Parámetros del decorador

Los decoradores `@app.get(...)`, `@app.post(...)`, etc. aceptan varios parámetros que controlan el comportamiento del endpoint y lo que se muestra en `/docs`. El más visto hasta ahora es la ruta, pero hay varios más.

```python
@app.post("/user/", response_model=User, status_code=201)
```

---

### 9.1 `response_model`

#### Qué es

Le dice a FastAPI qué estructura tiene la respuesta exitosa del endpoint.

#### Para qué sirve

Hace dos cosas simultáneamente:

**Documenta** — en `/docs`, bajo ese endpoint, muestra el schema exacto con los campos y tipos que el cliente va a recibir. Sin `response_model` Swagger solo muestra "Successful Response" sin estructura.

**Filtra** — antes de enviar la respuesta, Pydantic elimina cualquier campo que no esté en el modelo. Útil cuando el objeto interno tiene campos que no querés exponer al cliente (por ejemplo una contraseña hasheada).

```python
class UserInterno(BaseModel):
    id: int
    name: str
    password: str       # campo interno, no debe salir

class UserPublico(BaseModel):
    id: int
    name: str           # solo estos dos campos llegan al cliente

@app.get("/users/{id}", response_model=UserPublico)
async def get_user(id: int):
    return UserInterno(id=1, name="Andrés", password="hash_secreto")
    # FastAPI filtra "password" automáticamente antes de responder
```

#### Cuándo usarlo

| Situación | Usar `response_model` |
|-----------|----------------------|
| Querés documentar la estructura en `/docs` | Sí |
| Querés filtrar campos sensibles | Sí |
| Endpoint simple de prueba o aprendizaje | Opcional |
| Devolvés un tipo básico (`str`, `int`) | No es necesario |

#### Tipos que acepta

```python
response_model=User              # un solo objeto
response_model=list[User]        # lista de objetos
response_model=Optional[User]    # puede devolver el objeto o None
response_model=list[str]         # lista de strings
```

En el ejemplo de MoureDev:
```python
@app.post("/user/", response_model=User, status_code=201)
```
Documenta que la respuesta exitosa tiene la forma de `User` y filtra cualquier campo extra.

Referencia: [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)

---

### 9.2 `status_code`

#### Qué es

Define el código HTTP que devuelve el endpoint cuando todo sale bien.

#### Para qué sirve

Sin `status_code`, FastAPI devuelve `200 OK` por defecto en todos los endpoints. Con `status_code` podés devolver el código semánticamente correcto para cada operación.

```python
@app.post("/user/", status_code=201)    # 201 Created
@app.delete("/user/{id}", status_code=204)  # 204 No Content
```

#### Cuándo cambiarlo

| Método | `status_code` recomendado | Por qué |
|--------|--------------------------|---------|
| GET    | `200` (default)          | Lectura exitosa |
| POST   | `201`                    | Recurso creado |
| PUT    | `200` (default)          | Recurso actualizado, devuelve el objeto |
| DELETE | `204`                    | Eliminado sin contenido en la respuesta |

Con `204` la función no debe devolver nada — `204 No Content` significa respuesta sin body:

```python
@app.delete("/user/{id}", status_code=204)
async def delete_user(id: int):
    del users_list[index]
    return   # sin contenido
```

Referencia: [FastAPI - Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/)

---

### 9.3 `summary`, `description` y `tags`

Controlan lo que se muestra en `/docs` para cada endpoint.

```python
@app.get(
    "/users",
    summary="Listar usuarios",
    description="Devuelve todos los usuarios registrados en el sistema.",
    tags=["usuarios"]
)
async def get_users():
    return users_list
```

| Parámetro     | Qué muestra en `/docs`                              |
|---------------|-----------------------------------------------------|
| `summary`     | Título corto del endpoint                           |
| `description` | Descripción larga visible al expandir               |
| `tags`        | Agrupa endpoints bajo una categoría en el panel lateral |

Sin estos parámetros FastAPI usa el nombre de la función como summary y sin tags todos los endpoints aparecen bajo "default".

También podés usar el **docstring** de la función como descripción:

```python
@app.get("/users", tags=["usuarios"])
async def get_users():
    """Devuelve todos los usuarios registrados en el sistema."""
    return users_list
```

Referencia: [FastAPI - Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)

---

### 9.4 `responses`

Documenta los posibles códigos de respuesta del endpoint, incluyendo los de error.

```python
@app.get(
    "/users/{id}",
    responses={
        200: {"description": "Usuario encontrado"},
        404: {"description": "Usuario no encontrado"}
    }
)
async def get_user(id: int):
    ...
```

En `/docs`, bajo la sección **Responses**, aparecen todos los códigos posibles con su descripción. Sin esto solo aparece el `200`.

---

### 9.5 Combinación completa

```python
@app.post(
    "/user/",
    response_model=User,
    status_code=201,
    summary="Crear usuario",
    description="Crea un nuevo usuario. Devuelve 400 si el ID ya existe.",
    tags=["usuarios"],
    responses={
        201: {"description": "Usuario creado exitosamente"},
        400: {"description": "El usuario ya existe"}
    }
)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return user
```

En la práctica del curso solo se usan `response_model` y `status_code`. Los demás se agregan cuando la API va a ser consumida por otros equipos y la documentación importa.

Referencia: [FastAPI - Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/) · [FastAPI - Additional Responses](https://fastapi.tiangolo.com/advanced/additional-responses/)

---

## Resumen general

```
GET    → leer datos, sin body, idempotente
POST   → crear recurso, con body JSON, código 201
PUT    → reemplazar recurso completo, con body JSON, idempotente
DELETE → eliminar recurso, sin body, código 200 o 204

Path params  → identifican el recurso (/users/42)
Query params → filtran o paginan (/users?role=admin)

Pydantic     → BaseModel define esquema, valida tipos, serializa a JSON
CRUD         → Create/Read/Update/Delete = POST/GET/PUT/DELETE sobre un recurso
Lista memoria → almacenamiento temporal durante el aprendizaje (se pierde al reiniciar)

Routers      → dividen la API en archivos por recurso

Status codes → 2xx éxito · 4xx error del cliente · 5xx error del servidor
HTTPException → lanza errores HTTP desde cualquier punto del endpoint

Estáticos    → archivos servidos desde disco (StaticFiles)
Cookies      → estado persistente en el cliente (sesiones)
Headers      → metadatos de la petición/respuesta (auth, content-type)
```