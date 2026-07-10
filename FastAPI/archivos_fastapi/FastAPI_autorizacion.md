# FastAPI — Autorización

Fuentes: [FastAPI - Security](https://fastapi.tiangolo.com/tutorial/security/) · [FastAPI - Simple OAuth2](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/) · [FastAPI - OAuth2 JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) · [OAuth2](https://oauth.net/2/) · [JWT](https://jwt.io/)

---

## 1. Qué es la autorización y por qué es necesaria

Una API sin autorización está completamente abierta — cualquiera que conozca la URL puede leer, modificar o eliminar datos. La autorización es el mecanismo que controla **quién puede hacer qué**.

En APIs REST el estándar de la industria es **OAuth2 con Bearer tokens**:

```
1. Cliente envía usuario y contraseña → POST /login
2. Servidor verifica → genera un token
3. Servidor devuelve el token
4. Cliente guarda el token
5. En cada petición siguiente el cliente envía el token:
   Authorization: Bearer eyJhbGci...
6. Servidor verifica el token → permite o deniega
```

El cliente nunca vuelve a enviar usuario y contraseña — el token es la prueba de identidad temporal.

---

## 2. OAuth2 con contraseña (Basic Auth)

### Qué es

Es la implementación más simple de OAuth2 — el "password flow". El cliente envía usuario y contraseña directamente al servidor, que los verifica y devuelve un token. En este caso el token es simplemente el nombre de usuario (sin cifrado real) — es didáctico, no seguro para producción.

### Para qué sirve

Aprender el flujo completo de autenticación antes de agregar JWT. Muestra la estructura de los modelos, las funciones auxiliares y el sistema de dependencias de FastAPI.

---

### El código de MoureDev

```python
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
```

---

### Desglose completo

#### Imports nuevos

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
```

**`Depends`** — el sistema de inyección de dependencias de FastAPI. Permite que una función reciba el resultado de otra función automáticamente, sin llamarla manualmente. Es clave para la autorización.

**`status`** — módulo con constantes para los códigos HTTP. En lugar de escribir `401` directamente se usa `status.HTTP_401_UNAUTHORIZED` — más legible y menos propenso a errores.

**`OAuth2PasswordBearer`** — le dice a FastAPI que este endpoint usa autenticación Bearer. Extrae automáticamente el token del header `Authorization: Bearer <token>` de cada petición.

**`OAuth2PasswordRequestForm`** — clase que representa el formulario de login. Extrae automáticamente `username` y `password` del body de la petición como form data (no JSON).

---

#### `oauth2 = OAuth2PasswordBearer(tokenUrl="login")`

Crea el esquema de seguridad. `tokenUrl="login"` le dice a FastAPI dónde está el endpoint de login — esto aparece en `/docs` para que Swagger sepa dónde autenticarse.

---

#### Dos modelos: `User` y `UserDB`

```python
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):     # hereda de User y agrega password
    password: str
```

**`UserDB` hereda de `User`** — tiene todos los campos de `User` más `password`. La separación es intencional: `User` es lo que se devuelve al cliente (sin contraseña), `UserDB` es lo que se usa internamente para verificar credenciales.

Esta es la misma lógica de `response_model` — nunca exponer la contraseña al cliente.

---

#### `users_db` — base de datos simulada

```python
users_db = {
    "mouredev": {
        "username": "mouredev",
        ...
        "password": "123456"    # en producción: hash, nunca texto plano
    }
}
```

Un diccionario que simula una base de datos. La clave es el `username`. En producción esto sería una consulta a MongoDB o PostgreSQL, y la contraseña estaría hasheada.

---

#### Dos funciones auxiliares

```python
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])   # devuelve con password (uso interno)

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])     # devuelve sin password (uso externo)
```

`**users_db[username]` desempaca el diccionario como argumentos del modelo Pydantic — es lo mismo que escribir `User(username="mouredev", full_name="Brais Moure", ...)` pero automáticamente.

- `search_user_db` → devuelve `UserDB` con contraseña → solo se usa en el login para verificar
- `search_user` → devuelve `User` sin contraseña → se usa para devolver datos al cliente

---

#### `current_user` — ejemplo de MoureDev

```python
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user
```

#### `current_user` — estructura para rellenar

```python
# SIEMPRE IGUAL — solo cambian los mensajes de detail
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)                        # ← nombre de tu función auxiliar
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="...",                            # ← vos definís el mensaje
            headers={"WWW-Authenticate": "Bearer"}) # ← siempre igual, estándar OAuth2
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="...")                            # ← vos definís el mensaje
    return user
```

**`token: str = Depends(oauth2)`** — FastAPI extrae automáticamente el token del header `Authorization: Bearer <token>` de la petición y lo pasa como argumento. No hay que leerlo manualmente.

En este ejemplo el token es el `username` — por eso `search_user(token)` busca al usuario con ese nombre. En JWT real el token sería un string cifrado que hay que decodificar.

**`headers={"WWW-Authenticate": "Bearer"}`** — header estándar que le dice al cliente qué tipo de autenticación necesita. Siempre igual — requerido por el estándar OAuth2, nunca cambia.

**`user.disabled`** — verifica que el usuario esté activo. Un usuario puede existir pero estar deshabilitado.

---

#### `POST /login` — ejemplo de MoureDev

```python
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    return {"access_token": user.username, "token_type": "bearer"}
```

#### `POST /login` — estructura para rellenar

```python
# SIEMPRE IGUAL — cambia: nombre del decorador (router/app), nombre del dict, mensajes de detail
@router.post("/login")                                        # ← router o app según el archivo
async def login(form: OAuth2PasswordRequestForm = Depends()): # ← siempre igual
    user_db = biblioteca_users_db.get(form.username)          # ← nombre de tu dict
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,          # ← siempre 400
            detail="...")                                      # ← vos definís el mensaje
    user = search_user_db(form.username)                      # ← nombre de tu función
    if not form.password == user.password:                    # ← siempre igual
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,          # ← siempre 400
            detail="...")                                      # ← vos definís el mensaje
    return {"access_token": user.username, "token_type": "bearer"} # ← siempre igual
```

**`OAuth2PasswordRequestForm = Depends()`** — FastAPI lee automáticamente `username` y `password` del body como form data. El estándar OAuth2 exige que vayan como form data, no como JSON — por eso en Postman el body va como `form-data` y no `raw JSON`.

**`biblioteca_users_db.get(form.username)`** — busca el diccionario del usuario. Si no existe devuelve `None`.

**`return {"access_token": user.username, "token_type": "bearer"}`** — estructura fija exigida por el estándar OAuth2. Siempre debe tener exactamente estas dos claves. En JWT el `access_token` será el token cifrado, no el username.

---

#### `GET /users/me`

```python
@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
```

**`Depends(current_user)`** — antes de ejecutar `me`, FastAPI llama automáticamente a `current_user`. Si `current_user` lanza una excepción (token inválido, usuario deshabilitado), el endpoint nunca se ejecuta. Si pasa todo, `user` contiene el objeto `User` del usuario autenticado.

Este es el patrón para proteger cualquier endpoint — solo agregar `Depends(current_user)` como parámetro.

---

### El sistema `Depends` — clave para entender OAuth2

`Depends` es el mecanismo de **inyección de dependencias** de FastAPI. Permite encadenar funciones:

```
Petición llega a /users/me
    → FastAPI llama a current_user primero
        → current_user llama a oauth2 (extrae el token del header)
        → verifica el token
        → si es válido devuelve el User
    → me recibe el User ya verificado
    → devuelve el User al cliente
```

Sin `Depends` tendrías que repetir la lógica de verificación en cada endpoint protegido.

---

### Cómo probarlo en Postman

**1. Login:**
```
POST http://127.0.0.1:8000/login
Body → form-data:
  username: mouredev
  password: 123456
```

Respuesta:
```json
{"access_token": "mouredev", "token_type": "bearer"}
```

**2. Usar el token:**
```
GET http://127.0.0.1:8000/users/me
Headers:
  Authorization: Bearer mouredev
```

**3. Usuario deshabilitado:**
```
POST /login → username: mouredev2, password: 654321
GET /users/me → Authorization: Bearer mouredev2
→ debe devolver 400 "Usuario inactivo"
```

**4. En `/docs`** — aparece el botón **Authorize** donde podés ingresar usuario y contraseña y Swagger agrega el token automáticamente en cada petición.

---

### Limitación de este enfoque

Este es OAuth2 **sin JWT** — el token es el username en texto plano. Cualquiera que intercepte el token sabe el username del usuario. No hay expiración ni firma.

El siguiente paso es **OAuth2 con JWT** donde el token es un string cifrado con fecha de expiración.

Referencia: [FastAPI - Simple OAuth2](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/) · [FastAPI - Depends](https://fastapi.tiangolo.com/tutorial/dependencies/) · [OAuth2 - Password Flow](https://oauth.net/2/grant-types/password/)

---

## 3. OAuth2 con JWT

*(se completa cuando MoureDev explique el tema)*