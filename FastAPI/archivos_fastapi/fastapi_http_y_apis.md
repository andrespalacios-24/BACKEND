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

### Estructura recomendada de proyecto

Para una API simple de estudio, esta organización es suficiente:

```
FastAPI/
├── main.py          # Punto de entrada, instancia de app, inclusión de routers
├── routers/         # Un archivo por recurso (users.py, products.py)
├── models/          # Modelos Pydantic (esquemas de datos)
└── .venv/           # Entorno virtual
```

### Cómo iniciar la API

```bash
source ~/BACKEND/FastAPI/.venv/bin/activate
uvicorn main:app --reload
```

Referencia: [FastAPI - Tutorial](https://fastapi.tiangolo.com/tutorial/)

---

## 3. Path y Query Parameters

### Qué son

Son las dos formas que tiene un cliente de enviar datos a un endpoint GET sin usar un body.

---

### 3.1 Path Parameters (parámetros de ruta)

#### Qué son

Valores que forman parte de la URL misma, definidos entre llaves `{}` en la ruta.

#### Para qué sirven

Identificar un recurso específico. La convención REST es: cuando querés un elemento concreto de una colección, su identificador va en la ruta.

```
GET /users/42        → usuario con ID 42
GET /products/15     → producto con ID 15
GET /orders/8/items  → ítems del pedido 8
```

#### Cómo se usa en FastAPI

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

# Múltiples path params
@app.get("/users/{user_id}/orders/{order_id}")
async def get_order(user_id: int, order_id: int):
    return {"user_id": user_id, "order_id": order_id}
```

- FastAPI valida automáticamente el tipo. Si `user_id` debe ser `int` y recibe `"abc"`, devuelve `422`.
- El nombre del argumento en la función debe coincidir exactamente con el nombre entre llaves en la ruta.

#### En qué casos usar path params

Cuando el valor **identifica** el recurso. Sin ese valor, la ruta no tiene sentido.

---

### 3.2 Query Parameters (parámetros de consulta)

#### Qué son

Pares `clave=valor` que van al final de la URL después de `?`, separados por `&`.

```
GET /products?category=libros&limit=10&skip=0
```

#### Para qué sirven

Filtrar, paginar u ordenar una colección de recursos. No identifican un recurso único, sino que modifican el comportamiento de la búsqueda.

#### Cómo se usa en FastAPI

Los query params se declaran como argumentos de la función **sin** estar en la ruta:

```python
# Todos opcionales con valores por defecto
@app.get("/products")
async def get_products(category: str = "all", limit: int = 10, skip: int = 0):
    return {"category": category, "limit": limit, "skip": skip}

# Uno obligatorio (sin valor por defecto)
@app.get("/search")
async def search(q: str):
    return {"query": q}
```

- Con valor por defecto → opcional.
- Sin valor por defecto → obligatorio. Si no se envía, FastAPI devuelve `422`.

#### En qué casos usar query params

Cuando el valor **modifica** la búsqueda pero no identifica un recurso. Sin el valor, la ruta sigue siendo válida (devolvería todos los resultados, por ejemplo).

---

### 3.3 Comparación directa

| Aspecto              | Path param                  | Query param                        |
|----------------------|-----------------------------|------------------------------------|
| Posición en la URL   | Dentro de la ruta           | Después de `?`                     |
| Ejemplo              | `/users/42`                 | `/users?role=admin`                |
| Uso principal        | Identificar un recurso      | Filtrar, paginar, ordenar          |
| Obligatorio          | Siempre                     | Depende del default                |
| Declaración FastAPI  | `{nombre}` en la ruta       | Argumento sin llaves en la función |

Referencia: [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) · [FastAPI - Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

---

## 4. Peticiones HTTP: POST, PUT y DELETE

### 4.1 POST — Crear un recurso

#### Qué es

Método para **enviar datos al servidor y crear un nuevo recurso**. Los datos van en el cuerpo (body) de la petición en formato JSON.

#### Para qué sirve

- Crear un nuevo usuario: `POST /users`
- Registrar un pedido: `POST /orders`
- Iniciar sesión (enviar credenciales): `POST /auth/login`

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — modifica datos |
| Idempotente    | No — dos POST iguales crean dos recursos distintos |
| Cuerpo (body)  | Sí — los datos van en el body como JSON |
| Código típico  | `201 Created` |

#### Cómo se usa en FastAPI

FastAPI usa **Pydantic** para definir la estructura del body. Se crea una clase que hereda de `BaseModel`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    nombre: str
    edad: int
    email: str

@app.post("/users", status_code=201)
async def create_user(user: User):
    # user ya es un objeto Python validado
    return {"mensaje": "Usuario creado", "usuario": user}
```

FastAPI valida automáticamente que el body tenga los campos correctos con los tipos correctos. Si falta un campo o el tipo es incorrecto, devuelve `422`.

---

### 4.2 PUT — Actualizar un recurso completo

#### Qué es

Método para **reemplazar completamente** un recurso existente. Se envía el objeto entero con todos sus campos, no solo los que cambian.

#### Para qué sirve

- Actualizar todos los datos de un usuario: `PUT /users/42`
- Reemplazar la información de un producto: `PUT /products/15`

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — modifica datos |
| Idempotente    | Sí — hacer el mismo PUT 10 veces deja el recurso en el mismo estado |
| Cuerpo (body)  | Sí — todos los campos del recurso |
| Código típico  | `200 OK` |

#### Cómo se usa en FastAPI

```python
class User(BaseModel):
    nombre: str
    edad: int
    email: str

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"mensaje": f"Usuario {user_id} actualizado", "datos": user}
```

El `user_id` viene por path param (identifica el recurso a modificar) y el body contiene los nuevos datos completos.

---

### 4.3 DELETE — Eliminar un recurso

#### Qué es

Método para **eliminar un recurso** del servidor.

#### Para qué sirve

- Eliminar un usuario: `DELETE /users/42`
- Cancelar un pedido: `DELETE /orders/8`

#### Características

| Característica | Valor |
|----------------|-------|
| Seguro         | No — elimina datos |
| Idempotente    | Sí — eliminar algo que ya fue eliminado no cambia el estado |
| Cuerpo (body)  | Generalmente no |
| Código típico  | `200 OK` o `204 No Content` |

#### Cómo se usa en FastAPI

```python
@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    # 204: éxito sin contenido en la respuesta
    return
```

---

### 4.4 Resumen de métodos HTTP

| Método | Acción           | Body | Idempotente | Código típico |
|--------|------------------|------|-------------|---------------|
| GET    | Leer             | No   | Sí          | 200           |
| POST   | Crear            | Sí   | No          | 201           |
| PUT    | Reemplazar todo  | Sí   | Sí          | 200           |
| DELETE | Eliminar         | No   | Sí          | 200 / 204     |

> **PATCH** (no siempre cubierto en cursos básicos): actualiza **parcialmente** un recurso. Solo se envían los campos que cambian. A diferencia de PUT, no requiere el objeto completo.

Referencia: [MDN - HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) · [FastAPI - Body](https://fastapi.tiangolo.com/tutorial/body/)

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

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = buscar_usuario(user_id)  # función hipotética
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
```

`HTTPException` interrumpe la ejecución y devuelve la respuesta de error inmediatamente.

Referencia: [FastAPI - HTTPException](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [MDN - Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 6. Routers

### Qué son

Los routers son la forma de **dividir los endpoints en archivos separados** según el recurso que manejan, y luego incluirlos en la aplicación principal.

### Para qué sirven

A medida que una API crece, tener todos los endpoints en `main.py` se vuelve imposible de mantener. Los routers permiten:

- Un archivo por recurso: `users.py`, `products.py`, `orders.py`
- Cada archivo define sus propias rutas con `APIRouter`
- `main.py` solo incluye los routers y configura la app

### Cómo se usa en FastAPI

#### Archivo del router: `routers/users.py`

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",       # todas las rutas empiezan con /users
    tags=["usuarios"]      # agrupa en la documentación
)

@router.get("/")
async def get_users():
    return [{"id": 1, "nombre": "Andrés"}]

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id}

@router.post("/", status_code=201)
async def create_user():
    return {"mensaje": "usuario creado"}

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    return
```

#### Archivo principal: `main.py`

```python
from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)
```

Con `prefix="/users"` en el router, las rutas quedan:

```
GET    /users/
GET    /users/{user_id}
POST   /users/
DELETE /users/{user_id}
```

### Múltiples routers

```python
from routers import users, products, orders

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
```

Cada router es independiente. Podés darles prefijos y tags distintos.

### En qué casos usar routers

Desde el primer momento que tenés más de un recurso en la API. Es una buena práctica desde el inicio, no algo que se agrega después cuando el archivo ya está grande.

Referencia: [FastAPI - Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

---

## 7. Recursos Estáticos, Cookies y Headers

### 7.1 Recursos estáticos

#### Qué son

Archivos que el servidor entrega tal cual están en disco: imágenes, CSS, JavaScript, PDFs, fuentes. No se procesan ni generan dinámicamente.

#### Para qué sirven

En una API pura esto es menos común, pero es útil para servir imágenes de productos, archivos descargables, o una interfaz HTML simple junto a la API.

#### Cómo se usa en FastAPI

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta la carpeta "static" bajo la ruta "/static"
app.mount("/static", StaticFiles(directory="static"), name="static")
```

Estructura de carpetas:
```
FastAPI/
├── main.py
└── static/
    ├── imagen.png
    └── documento.pdf
```

Acceso desde el navegador o cliente HTTP:
```
GET http://127.0.0.1:8000/static/imagen.png
GET http://127.0.0.1:8000/static/documento.pdf
```

Requiere instalar `aiofiles`:
```bash
pip install aiofiles
```

Referencia: [FastAPI - Static Files](https://fastapi.tiangolo.com/tutorial/static-files/)

---

### 7.2 Cookies

#### Qué son

Pequeños fragmentos de datos que el servidor envía al cliente y el cliente almacena y reenvía automáticamente en cada petición siguiente al mismo dominio.

#### Para qué sirven

- Mantener sesiones de usuario sin enviar credenciales en cada petición.
- Guardar preferencias del cliente (idioma, tema).
- Rastreo de estado entre peticiones (HTTP es stateless por naturaleza).

#### Cómo leer cookies en FastAPI

```python
from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

@app.get("/perfil")
async def get_perfil(session_id: Optional[str] = Cookie(default=None)):
    if session_id is None:
        return {"mensaje": "no hay sesión activa"}
    return {"session_id": session_id}
```

#### Cómo escribir cookies en la respuesta

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/login")
async def login():
    response = JSONResponse(content={"mensaje": "sesión iniciada"})
    response.set_cookie(
        key="session_id",
        value="abc123",
        httponly=True,    # no accesible desde JavaScript del navegador
        max_age=3600      # expira en 1 hora (segundos)
    )
    return response
```

| Parámetro  | Para qué sirve                                             |
|------------|------------------------------------------------------------|
| `httponly` | Protege contra XSS — JS no puede leer la cookie           |
| `secure`   | Solo se envía por HTTPS                                    |
| `max_age`  | Segundos hasta que expira                                  |
| `samesite` | Protege contra CSRF (`"lax"`, `"strict"`, `"none"`)       |

Referencia: [FastAPI - Cookie Parameters](https://fastapi.tiangolo.com/tutorial/cookie-params/) · [MDN - Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

---

### 7.3 Headers

#### Qué son

Metadatos que viajan junto a cada petición o respuesta HTTP, fuera del cuerpo. Son pares clave-valor que transmiten información sobre la petición, la respuesta o el cliente.

#### Para qué sirven

- Indicar el tipo de contenido: `Content-Type: application/json`
- Autenticación: `Authorization: Bearer <token>`
- Control de caché, CORS, idioma preferido, y mucho más.
- Enviar metadatos propios de la aplicación entre cliente y servidor.

#### Cómo leer headers de la petición en FastAPI

```python
from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.get("/info")
async def get_info(user_agent: Optional[str] = Header(default=None)):
    return {"user_agent": user_agent}
```

FastAPI convierte automáticamente los guiones de los headers a guiones bajos: `user-agent` → `user_agent`.

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

#### Headers más comunes en APIs

| Header                | Dirección          | Para qué sirve                                      |
|-----------------------|--------------------|-----------------------------------------------------|
| `Content-Type`        | Request / Response | Tipo de dato del body (`application/json`)          |
| `Authorization`       | Request            | Token de autenticación (`Bearer <token>`)           |
| `Accept`              | Request            | Formato que acepta el cliente                       |
| `Cache-Control`       | Response           | Instrucciones de caché                              |
| `X-Request-ID`        | Request / Response | ID para rastrear peticiones en logs                 |

La convención `X-` indica headers personalizados (no estándar). Aunque fue deprecada formalmente por la RFC 6648, sigue siendo muy usada en la práctica.

Referencia: [FastAPI - Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/) · [MDN - HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

---

## Resumen general

```
GET    → leer datos, sin body, idempotente
POST   → crear recurso, con body JSON, código 201
PUT    → reemplazar recurso completo, con body JSON, idempotente
DELETE → eliminar recurso, sin body, código 200 o 204

Path params  → identifican el recurso (/users/42)
Query params → filtran o paginan (/users?role=admin)

Routers      → dividen la API en archivos por recurso

Status codes → 2xx éxito · 4xx error del cliente · 5xx error del servidor

Estáticos    → archivos servidos desde disco (StaticFiles)
Cookies      → estado persistente en el cliente (sesiones)
Headers      → metadatos de la petición/respuesta (auth, content-type)
```