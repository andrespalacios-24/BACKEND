# FastAPI — MongoDB

Fuentes: [FastAPI - SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) · [MongoDB Docs](https://www.mongodb.com/docs/) · [PyMongo Docs](https://pymongo.readthedocs.io/) · [Motor Docs](https://motor.readthedocs.io/)

---

## 1. Qué es MongoDB y por qué usarlo con FastAPI

MongoDB es una base de datos **NoSQL** — en lugar de guardar datos en tablas con filas y columnas como MySQL, guarda **documentos JSON** organizados en colecciones.

```
SQL (MySQL)                     MongoDB
─────────────────────           ─────────────────────
Base de datos                   Base de datos
  └── Tabla: users                └── Colección: users
        ├── fila 1                      ├── documento 1
        ├── fila 2                      ├── documento 2
        └── fila 3                      └── documento 3
```

Un documento en MongoDB luce así:

```json
{
    "_id": ObjectId("64a1b2c3d4e5f6789012345"),
    "username": "andrés",
    "email": "andres@email.com"
}
```

**`_id`** — identificador único que MongoDB genera automáticamente para cada documento. Es de tipo `ObjectId`, no un entero como en SQL.

### Por qué MongoDB con FastAPI

- FastAPI trabaja con JSON nativo — MongoDB también. No hay conversión de formatos.
- Sin esquema rígido — podés agregar campos sin migrar la base de datos.
- Muy usado en proyectos Python modernos junto a FastAPI.

---

## 2. Instalación y configuración

### Instalar MongoDB en WSL

```bash
# Importar clave pública
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

# Agregar repositorio
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Instalar
sudo apt-get update
sudo apt-get install -y mongodb-org
```

### Iniciar MongoDB

```bash
# Crear carpeta de datos si no existe
sudo mkdir -p /data/db

# Iniciar el servidor
sudo mongod --dbpath /data/db
```

Dejás este terminal corriendo — igual que uvicorn. MongoDB queda escuchando en `mongodb://localhost:27017`.

### Instalar PyMongo

```bash
pip install pymongo
```

PyMongo es el driver oficial de Python para conectarse a MongoDB.

### MongoDB Compass

Interfaz gráfica para ver y manejar las bases de datos. Para conectarte:

```
Connection String: mongodb://localhost
```

---

## 3. Estructura de carpetas

MoureDev organiza el proyecto en carpetas separadas por responsabilidad:

```
FastAPI/
└── ejercicios/
    ├── db/
    │   ├── client.py          ← conexión a MongoDB
    │   ├── models/
    │   │   └── user.py        ← modelo Pydantic (esquema de datos)
    │   └── schemas/
    │       └── user.py        ← funciones para convertir documentos MongoDB a dict
    ├── routers/
    │   └── users_db.py        ← endpoints CRUD con MongoDB
    └── main_biblioteca.py     ← punto de entrada
```

---

## 4. `db/client.py` — conexión a MongoDB

### Código de MoureDev

```python
from pymongo import MongoClient

db_client = MongoClient().local
```

### Desglose

**`MongoClient()`** — crea la conexión a MongoDB. Sin argumentos se conecta a `mongodb://localhost:27017` que es la dirección por defecto. En producción se pasa la URL de conexión:

```python
MongoClient("mongodb://usuario:contraseña@host:27017")
```

**`.local`** — selecciona la base de datos llamada `local`. Podés usar cualquier nombre — si no existe, MongoDB la crea automáticamente cuando insertas el primer documento:

```python
MongoClient().mi_biblioteca    # base de datos "mi_biblioteca"
MongoClient().produccion       # base de datos "produccion"
```

**`db_client`** — el objeto que usás en todos los endpoints para hacer operaciones. Desde él accedés a las colecciones:

```python
db_client.users          # colección "users"
db_client.products       # colección "products"
db_client.books          # colección "books"
```

---

## 5. `db/models/user.py` — modelo Pydantic

### Código de MoureDev

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
```

### Desglose

Es un modelo Pydantic igual que los anteriores, con una diferencia importante: **`id: Optional[str] = None`**.

**Por qué `id` es opcional:**

- Al **crear** un usuario (`POST`) no enviás el `id` — MongoDB lo genera automáticamente
- Al **leer** un usuario (`GET`) sí existe el `id` — MongoDB lo devuelve como `_id`

Si el `id` fuera obligatorio, no podrías crear usuarios sin enviarlo manualmente.

**Por qué `str` y no `int`:**

El `_id` de MongoDB es un `ObjectId` — un tipo especial que se convierte a string para manejarlo en Python y JSON:

```python
ObjectId("64a1b2c3d4e5f6789012345")  # tipo ObjectId en MongoDB
"64a1b2c3d4e5f6789012345"            # string en Python/JSON
```

---

## 6. `db/schemas/user.py` — schemas de conversión

### Código de MoureDev

```python
def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
```

### Qué son los schemas y para qué sirven

MongoDB devuelve documentos como diccionarios Python con una clave especial `_id` de tipo `ObjectId`. Pydantic no sabe manejar `ObjectId` directamente, entonces necesitás convertirlo.

Los schemas son funciones que convierten el documento de MongoDB al formato que Pydantic y FastAPI esperan.

**`user_schema`** — convierte un documento MongoDB a dict Python:

```python
# Documento MongoDB (lo que devuelve find_one)
{
    "_id": ObjectId("64a1b2c3..."),
    "username": "andrés",
    "email": "andres@email.com"
}

# Después de user_schema (lo que recibe Pydantic)
{
    "id": "64a1b2c3...",      # _id → id, ObjectId → str
    "username": "andrés",
    "email": "andres@email.com"
}
```

**`users_schema`** — aplica `user_schema` a cada documento de una lista:

```python
[user_schema(user) for user in users]
```

Es una list comprehension que convierte cada documento de la colección.

---

## 7. `routers/users_db.py` — CRUD con MongoDB

### Código de MoureDev

```python
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())


@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)


@router.put("/", response_model=User)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
```

---

### Desglose de operaciones

#### `from bson import ObjectId`

`bson` es el formato binario que usa MongoDB internamente. `ObjectId` es la clase que representa el `_id` de MongoDB. Se usa para convertir el string del `id` al tipo que MongoDB entiende:

```python
ObjectId("64a1b2c3d4e5f6789012345")
```

Sin esta conversión MongoDB no puede buscar por `_id`.

---

#### GET — Leer todos los usuarios

```python
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())
```

**`db_client.users`** — accede a la colección `users` de la base de datos.

**`.find()`** — devuelve todos los documentos de la colección. Equivale a `SELECT * FROM users` en SQL.

**`users_schema(...)`** — convierte cada documento MongoDB al formato que Pydantic espera.

---

#### GET — Leer un usuario por ID

```python
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))
```

El `id` llega como string desde la URL. `ObjectId(id)` lo convierte al tipo que MongoDB usa internamente para buscar.

---

#### POST — Crear un usuario

```python
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)
```

**`dict(user)`** — convierte el objeto Pydantic a diccionario para poder insertarlo en MongoDB.

**`del user_dict["id"]`** — elimina el campo `id` antes de insertar porque MongoDB genera su propio `_id`. Si lo dejás, MongoDB tendría dos IDs.

**`.insert_one(user_dict).inserted_id`** — inserta el documento y devuelve el `_id` generado por MongoDB.

**`find_one({"_id": id})`** — busca el documento recién insertado para devolverlo completo con el `_id` asignado.

---

#### PUT — Actualizar un usuario

```python
@router.put("/", response_model=User)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))
```

**`find_one_and_replace`** — busca el documento por `_id` y lo reemplaza completamente con `user_dict`. Equivale a `UPDATE` en SQL pero reemplaza todo el documento.

El `id` va en el body (igual que en el CRUD anterior) para identificar qué documento reemplazar, pero se elimina del dict antes de insertarlo porque `_id` lo maneja MongoDB.

---

#### DELETE — Eliminar un usuario

```python
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error": "No se ha eliminado el usuario"}
```

**`find_one_and_delete`** — busca el documento por `_id` y lo elimina. Devuelve el documento eliminado si lo encontró, o `None` si no existía.

---

#### `search_user` — función auxiliar

```python
def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
```

**`find_one({field: key})`** — busca un documento donde el campo `field` tenga el valor `key`. Es genérica — sirve para buscar por `_id`, `email` o cualquier campo:

```python
search_user("_id", ObjectId(id))      # busca por ID
search_user("email", user.email)      # busca por email
```

**`User(**user_schema(user))`** — convierte el documento MongoDB → dict (schema) → objeto Pydantic.

---

## 8. Comparación: lista en memoria vs MongoDB

| Aspecto | Lista en memoria | MongoDB |
|---------|-----------------|---------|
| Persistencia | Se pierde al reiniciar | Permanente |
| ID | Lo definís vos | MongoDB lo genera automáticamente |
| Buscar | `filter` + `lambda` | `find_one({campo: valor})` |
| Crear | `lista.append(obj)` | `insert_one(dict)` |
| Actualizar | `lista[index] = obj` | `find_one_and_replace(filtro, dict)` |
| Eliminar | `del lista[index]` | `find_one_and_delete(filtro)` |
| Ver datos | Solo en el código | MongoDB Compass |

---

## 9. Operaciones MongoDB más comunes

```python
# Leer todos
db_client.users.find()

# Leer uno por campo
db_client.users.find_one({"email": "andres@email.com"})
db_client.users.find_one({"_id": ObjectId(id)})

# Crear
db_client.users.insert_one(dict)           # devuelve inserted_id
db_client.users.insert_many([dict1, dict2]) # varios a la vez

# Actualizar
db_client.users.find_one_and_replace({"_id": ObjectId(id)}, nuevo_dict)
db_client.users.update_one({"_id": ObjectId(id)}, {"$set": {"email": "nuevo@email.com"}})

# Eliminar
db_client.users.find_one_and_delete({"_id": ObjectId(id)})
db_client.users.delete_many({})   # elimina todos
```

Referencia: [PyMongo - Tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html) · [MongoDB - CRUD](https://www.mongodb.com/docs/manual/crud/) · [FastAPI - NoSQL](https://fastapi.tiangolo.com/how-to/nosql-databases-couchbase/)

---

## 10. MongoDB Atlas — Base de datos en la nube

### Qué es

MongoDB Atlas es el servicio en la nube de MongoDB. En lugar de correr MongoDB en tu máquina local, los datos se guardan en servidores de MongoDB en internet. Tiene un tier gratuito (M0) suficiente para proyectos de aprendizaje y proyectos pequeños.

### Para qué sirve

- La base de datos está disponible desde cualquier lugar — no depende de que tu máquina esté encendida
- No necesitás correr `sudo mongod` cada vez
- Cuando desplegués la API en producción, la base de datos ya está accesible desde internet
- Múltiples personas pueden conectarse a la misma base de datos

### Cómo conectarse — el único cambio

El único cambio respecto a MongoDB local es la connection string en `client.py`:

```python
from pymongo import MongoClient

# Base de datos local (desarrollo)
# db_client = MongoClient().local

# Base de datos remota MongoDB Atlas (producción o desarrollo en la nube)
db_client = MongoClient(
    "mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test
#              ^^^^^^   ^^^^^^^^   ^^^^^                                   ^^^^
#              usuario  contraseña  URL del cluster                        nombre de la BD
```

**`.test`** al final selecciona la base de datos — reemplazalo con el nombre que quieras usar.

Todo lo demás — modelos, schemas, endpoints — queda exactamente igual. El cambio es solo en `client.py`.

### Cómo obtener la connection string

1. Creá una cuenta en [https://mongodb.com](https://mongodb.com)
2. Creá un cluster gratuito (M0)
3. En **Database Access** → creá un usuario con contraseña
4. En **Network Access** → agregá tu IP o `0.0.0.0/0` para permitir cualquier IP
5. En el cluster → **Connect** → **Connect your application** → copiás la connection string

La connection string tiene este formato:
```
mongodb+srv://usuario:contraseña@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

### Sintaxis para rellenar

```python
from pymongo import MongoClient

# ── SIEMPRE IGUAL ──────────────────────────────────────────
db_client = MongoClient(
    "mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority"
#              ^^^^^^   ^^^^^^^^   ^^^^^
#              ← vos completás estos tres valores con los de tu cluster
).nombre_de_tu_bd   # ← nombre de la base de datos que querés usar
# ───────────────────────────────────────────────────────────
```

### Local vs Atlas

| Aspecto | Local | Atlas |
|---------|-------|-------|
| Dónde corre | Tu máquina | Servidores de MongoDB |
| Connection string | `MongoClient().local` | `MongoClient("mongodb+srv://...")` |
| Requiere iniciar | `sudo mongod` cada vez | No — siempre disponible |
| Acceso desde internet | No | Sí |
| Costo | Gratis | Gratis (tier M0) |
| Uso recomendado | Desarrollo local | Producción o compartir BD |

Referencia: [MongoDB Atlas](https://www.mongodb.com/atlas) · [Atlas Connection String](https://www.mongodb.com/docs/atlas/driver-connection/)