# FastAPI — Fundamentos

Fuentes: [FastAPI Docs](https://fastapi.tiangolo.com/) · [Uvicorn Docs](https://www.uvicorn.org/) · [Python asyncio](https://docs.python.org/3/library/asyncio.html)

---

## 1. Instalación

FastAPI necesita dos paquetes: el framework en sí y un servidor ASGI para ejecutarlo.

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

`uvicorn[standard]` incluye extras como recarga automática (`--reload`) y soporte para WebSockets.

> Si usás entornos virtuales (recomendado), activá el venv antes de instalar:
> ```bash
> source ~/BACKEND/FastAPI/.venv/bin/activate
> ```

---

## 2. Importar y configurar FastAPI

```python
from fastapi import FastAPI

app = FastAPI()
```

- `FastAPI` es la clase principal. Al instanciarla se crea la aplicación.
- `app` es el objeto que uvicorn recibe para levantar el servidor.
- Toda la configuración de rutas, middlewares y eventos se hace sobre este objeto.

---

## 3. Iniciar el servidor con Uvicorn

```bash
uvicorn main:app --reload
```

| Parte      | Qué significa                                      |
|------------|----------------------------------------------------|
| `main`     | Nombre del archivo Python (`main.py`)              |
| `app`      | Nombre de la variable que contiene la instancia    |
| `--reload` | Reinicia el servidor automáticamente al guardar    |

El servidor queda disponible en: `http://127.0.0.1:8000`

`--reload` es solo para desarrollo. En producción se omite.

---

## 4. Funciones asíncronas (`async def`)

```python
@app.get("/")
async def root():
    return "Hola FastAPI!"
```

### Por qué `async def` y no `def`

Python ejecuta código en un solo hilo por defecto. Con `def` normal, si una función tarda (por ejemplo, esperar respuesta de una base de datos), el servidor queda bloqueado y no puede atender otras peticiones mientras tanto.

`async def` permite que el servidor **suspenda** la función mientras espera (operaciones de I/O: BD, red, archivos) y atienda otras peticiones en ese intervalo. Cuando la espera termina, retoma la función.

```
Petición A → función espera BD → servidor libre → atiende Petición B → BD responde → termina A
```

### Cuándo usar cada una

| Situación                                      | Usar        |
|------------------------------------------------|-------------|
| Consultas a BD, APIs externas, lectura/escritura de archivos | `async def` |
| Operaciones CPU puras sin esperas de I/O       | `def`       |
| No estás seguro                                | `async def` (más seguro por defecto) |

FastAPI admite ambas, pero `async def` es el estándar para backends modernos.

Referencia: [FastAPI - Concurrency](https://fastapi.tiangolo.com/async/)

---

## 5. Peticiones GET y tipos de respuesta

El decorador `@app.get("/ruta")` registra la función como manejadora de peticiones GET a esa ruta.

FastAPI convierte automáticamente el valor de retorno a JSON.

### Retorno de texto plano

```python
@app.get("/")
async def root():
    return "Hola FastAPI!"
```

Respuesta: `"Hola FastAPI!"` (string serializado como JSON)

### Retorno de JSON (diccionario)

```python
@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
```

Respuesta:
```json
{
  "url": "https://mouredev.com/python"
}
```

FastAPI acepta como retorno: `str`, `int`, `dict`, `list`, modelos Pydantic. Todos se serializan a JSON automáticamente.

Para hacer la petición desde el navegador, simplemente ingresás la URL:

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/url
```

---

## 6. Rutas: raíz vs. rutas específicas

```python
@app.get("/")        # Ruta raíz
@app.get("/url")     # Ruta específica
```

| Concepto        | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Ruta raíz `/`   | Punto de entrada principal. Devuelve información general o un health check. |
| Ruta específica | Cada endpoint tiene una responsabilidad concreta y bien definida.           |

Cada ruta mapea a una función distinta, lo que permite separar responsabilidades. En un backend real cada ruta representa un recurso o acción: `/users`, `/products`, `/login`, etc.

FastAPI evalúa las rutas en orden de definición, por lo que si hay ambigüedad entre rutas, importa el orden en el archivo.

Referencia: [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

---

## 7. Documentación automática de la API

FastAPI genera documentación interactiva automáticamente a partir del código, sin configuración adicional. Esta documentación se basa en el estándar **OpenAPI** (antes llamado Swagger), que es el estándar de la industria para describir APIs REST.

Todo lo que FastAPI necesita para generar la documentación ya está en el código: los decoradores de ruta, los tipos de los parámetros y los tipos de retorno. No hay que escribir nada extra.

Referencia: [FastAPI - Automatic Docs](https://fastapi.tiangolo.com/features/#automatic-docs) · [OpenAPI Specification](https://spec.openapis.org/oas/v3.1.0)

---

### 7.1 Endpoints disponibles

Un **endpoint** es una URL específica de la API a la que se puede hacer una petición para obtener o enviar información. Es el punto de contacto entre el cliente (navegador, app, otro servidor) y el backend.

Cada función decorada con `@app.get(...)`, `@app.post(...)`, etc. define un endpoint.

```python
@app.get("/")        # Endpoint 1: GET /
async def root():
    return "Hola FastAPI!"

@app.get("/url")     # Endpoint 2: GET /url
async def url():
    return {"url": "https://mouredev.com/python"}
```

Un endpoint queda definido por dos cosas juntas: el **método HTTP** (`GET`, `POST`, `PUT`, `DELETE`) y la **ruta** (`/`, `/url`, `/users/1`). La misma ruta con distinto método es un endpoint diferente.

En Swagger UI (`/docs`) cada endpoint aparece como una fila expandible que muestra toda su información. En ReDoc (`/redoc`) aparecen listados en el panel izquierdo como índice navegable.

---

### 7.2 Documentar endpoints con metadatos

FastAPI permite agregar descripción, resumen y etiquetas a cada endpoint directamente en el decorador. Esto enriquece lo que se muestra en Swagger y ReDoc sin afectar el comportamiento.

```python
@app.get(
    "/url",
    summary="Devuelve la URL principal",
    description="Retorna la URL del sitio de MoureDev como ejemplo de respuesta JSON.",
    tags=["recursos"]
)
async def url():
    return {"url": "https://mouredev.com/python"}
```

| Parámetro     | Qué muestra en la documentación                              |
|---------------|--------------------------------------------------------------|
| `summary`     | Título corto del endpoint en Swagger UI                      |
| `description` | Descripción larga, visible al expandir el endpoint           |
| `tags`        | Agrupa endpoints bajo una categoría en el panel lateral      |

También se puede usar el **docstring** de la función como descripción. FastAPI lo lee automáticamente:

```python
@app.get("/url")
async def url():
    """
    Retorna la URL del sitio de MoureDev.

    Útil como ejemplo de endpoint que devuelve JSON.
    """
    return {"url": "https://mouredev.com/python"}
```

Referencia: [FastAPI - Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)

---

### 7.3 Parámetros que aceptan los endpoints

Los parámetros son los datos que el cliente puede enviar al endpoint. FastAPI los detecta automáticamente según dónde estén declarados en la función y los documenta sin configuración extra.

#### Parámetros de ruta (path parameters)

Se definen dentro de la URL entre llaves `{}` y se reciben como argumentos de la función.

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
```

- Obligatorios: si no se incluyen en la URL, FastAPI devuelve error 422.
- El tipo anotado (`int`) hace que FastAPI valide y convierta automáticamente.
- En Swagger aparecen bajo la sección **Parameters** con tipo "path".

#### Parámetros de query (query parameters)

Se declaran como argumentos de la función que **no** están en la ruta. Se envían en la URL después de `?`.

```python
@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Petición: `http://127.0.0.1:8000/items?skip=5&limit=20`

- Si tienen valor por defecto (`= 0`) son opcionales.
- Si no tienen valor por defecto son obligatorios.
- En Swagger aparecen bajo **Parameters** con tipo "query" y muestran si son requeridos u opcionales.

#### Comparación rápida

| Tipo        | Dónde va en la URL           | Ejemplo                        | Obligatorio por defecto |
|-------------|------------------------------|--------------------------------|-------------------------|
| Path param  | Dentro de la ruta            | `/users/42`                    | Sí                      |
| Query param | Después de `?` en la URL     | `/items?skip=0&limit=10`       | Depende del default     |

Referencia: [FastAPI - Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/) · [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

---

### 7.4 Respuestas que devuelven los endpoints

FastAPI serializa automáticamente el valor de retorno de cada función a JSON. Además, permite documentar explícitamente qué respuestas puede devolver un endpoint y bajo qué condiciones.

#### Códigos de estado HTTP

Cada respuesta tiene un código de estado que indica el resultado. Los más comunes en APIs REST:

| Código | Significado               | Cuándo usarlo                                  |
|--------|---------------------------|------------------------------------------------|
| `200`  | OK                        | Petición exitosa (default de FastAPI)          |
| `201`  | Created                   | Recurso creado exitosamente (POST)             |
| `204`  | No Content                | Éxito sin cuerpo de respuesta (DELETE)         |
| `400`  | Bad Request               | El cliente envió datos inválidos               |
| `404`  | Not Found                 | El recurso solicitado no existe                |
| `422`  | Unprocessable Entity      | Error de validación de parámetros (automático) |
| `500`  | Internal Server Error     | Error no manejado en el servidor               |

FastAPI devuelve `200` por defecto. Para cambiar el código de éxito:

```python
@app.post("/items", status_code=201)
async def create_item():
    return {"message": "creado"}
```

#### Documentar las respuestas posibles

El parámetro `responses` del decorador permite declarar todos los posibles códigos de respuesta con su descripción. Esto aparece en Swagger bajo la sección **Responses**.

```python
@app.get(
    "/users/{user_id}",
    responses={
        200: {"description": "Usuario encontrado"},
        404: {"description": "Usuario no encontrado"},
    }
)
async def get_user(user_id: int):
    return {"user_id": user_id}
```

#### `response_model`: documentar la estructura de la respuesta

`response_model` le dice a FastAPI qué forma tiene la respuesta exitosa. Sirve para dos cosas: documentarla en Swagger y filtrar campos no deseados del retorno.

```python
from pydantic import BaseModel

class UrlResponse(BaseModel):
    url: str

@app.get("/url", response_model=UrlResponse)
async def url():
    return {"url": "https://mouredev.com/python"}
```

En Swagger, bajo **Responses → 200**, aparece el schema exacto del objeto con sus campos y tipos. Esto le indica a quien consume la API exactamente qué esperar.

Referencia: [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/) · [FastAPI - Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/) · [FastAPI - Additional Responses](https://fastapi.tiangolo.com/advanced/additional-responses/)

---

### 7.5 Las tres interfaces de documentación

#### Swagger UI — `/docs`

```
http://127.0.0.1:8000/docs
```

Interfaz interactiva. Permite explorar cada endpoint, ver sus parámetros y respuestas documentadas, y ejecutar peticiones reales directamente desde el navegador sin necesidad de herramientas externas. Es la herramienta principal durante el desarrollo.

Lo que muestra por cada endpoint:
- Método HTTP y ruta
- `summary` y `description`
- Sección **Parameters**: path params y query params con sus tipos y si son requeridos
- Sección **Request body**: estructura del cuerpo esperado (para POST/PUT)
- Sección **Responses**: códigos posibles con sus schemas (`response_model`)
- Botón **Try it out**: ejecuta la petición real y muestra la respuesta

#### ReDoc — `/redoc`

```
http://127.0.0.1:8000/redoc
```

Documentación de solo lectura, más limpia visualmente. No permite ejecutar peticiones. Útil para compartir la documentación con otros equipos o como referencia técnica para quien va a consumir la API.

#### OpenAPI Schema — `/openapi.json`

```
http://127.0.0.1:8000/openapi.json
```

El archivo JSON que describe toda la API según el estándar OpenAPI 3.0. Tanto Swagger UI como ReDoc lo leen para generar sus interfaces. Se puede exportar para importarlo en herramientas como Postman o para generar clientes automáticamente en otros lenguajes.

Fragmento de ejemplo de lo que genera FastAPI para el endpoint `/url`:

```json
"/url": {
  "get": {
    "summary": "Url",
    "operationId": "url_url_get",
    "responses": {
      "200": {
        "description": "Successful Response",
        "content": {
          "application/json": {
            "schema": {}
          }
        }
      }
    }
  }
}
```

Referencia: [FastAPI - OpenAPI](https://fastapi.tiangolo.com/how-to/extending-openapi/)

---

## Flujo completo resumido

```
1. pip install fastapi "uvicorn[standard]"
2. Crear main.py con la instancia app = FastAPI()
3. Definir rutas con @app.get("/ruta") + async def
4. Activar venv: source ~/BACKEND/FastAPI/.venv/bin/activate
5. Levantar servidor: uvicorn main:app --reload
6. Probar en navegador: http://127.0.0.1:8000/
7. Explorar docs: http://127.0.0.1:8000/docs
```
