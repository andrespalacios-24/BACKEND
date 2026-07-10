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

### Qué es

JWT (JSON Web Token) es el estándar de la industria para tokens de autenticación. A diferencia del Basic Auth donde el token era el username en texto plano, JWT genera un token cifrado y firmado que contiene información del usuario y tiene fecha de expiración.

Un JWT tiene tres partes separadas por puntos:

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtb3VyZWRldiJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    HEADER                    PAYLOAD                        SIGNATURE
```

- **Header** — algoritmo de firma usado (`HS256`)
- **Payload** — datos del usuario (`sub`, `exp`) — no va información sensible
- **Signature** — firma que garantiza que el token no fue modificado

El servidor puede verificar el token sin consultar la base de datos — solo verifica la firma con la clave secreta.

### Para qué sirve

Agrega tres mejoras sobre el Basic Auth:
- **Token cifrado** — no se puede leer el username directamente del token
- **Fecha de expiración** — el token deja de ser válido automáticamente
- **Contraseñas hasheadas** — las contraseñas nunca se guardan en texto plano

### Librerías necesarias

```bash
pip install pyjwt                    # para generar y verificar JWT
pip install "pwdlib[argon2]"         # para hashear contraseñas con Argon2
```

**`PyJWT`** — librería oficial recomendada por FastAPI para JWT. Más mantenida que `python-jose`.

**`pwdlib[argon2]`** — librería oficial recomendada por FastAPI para hashear contraseñas. El algoritmo **Argon2** es más seguro que bcrypt y es el recomendado actualmente. Los corchetes `[argon2]` instalan el algoritmo junto con la librería.

> **Nota sobre el código de MoureDev** — usa `python-jose` y `passlib[bcrypt]` que son librerías anteriores. El concepto es idéntico, solo cambian los imports y algunos métodos. El documento explica la versión actualizada recomendada por la documentación oficial.

---

### Imports actualizados (versión oficial)

```python
from datetime import datetime, timedelta, timezone
import jwt                                          # PyJWT — antes era from jose import jwt
from jwt.exceptions import InvalidTokenError        # antes era from jose import JWTError
from pwdlib import PasswordHash                     # antes era from passlib.context import CryptContext
```

---

### Configuración del hash de contraseñas

```python
# Con pwdlib (versión oficial actual)
password_hash = PasswordHash.recommended()         # usa Argon2 automáticamente

# Hashear
password_hash.hash("mi_contraseña")
# → "$argon2id$v=19$m=65536,t=3,p=4$..."

# Verificar
password_hash.verify("mi_contraseña", hash_guardado)
# → True o False
```

Con `PasswordHash.recommended()` siempre usás el algoritmo más seguro disponible sin tener que configurarlo manualmente.

---

### El código de MoureDev

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

router = APIRouter(
    prefix="/jwtauth",
    tags=["jwtauth"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    access_token = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
```

---

### Diferencias clave con el Basic Auth

| Aspecto | Basic Auth | JWT |
|---------|-----------|-----|
| Token | Username en texto plano | String cifrado y firmado |
| Contraseña en BD | Texto plano `"123456"` | Hash bcrypt `"$2a$12$..."` |
| Verificación contraseña | `form.password == user.password` | `crypt.verify(form.password, user.password)` |
| Expiración | No tiene | Sí — `exp` en el payload |
| Dependencia auth | `current_user` directa | `auth_user` → `current_user` en cadena |

---

### Desglose de las partes nuevas

#### Constantes de configuración

```python
ALGORITHM = "HS256"           # algoritmo de firma — estándar, no cambia
ACCESS_TOKEN_DURATION = 1     # minutos de validez del token — vos lo definís
SECRET = "clave_secreta_larga" # clave para firmar el token — nunca exponer
```

**`ALGORITHM = "HS256"`** — HMAC con SHA-256. Es el algoritmo estándar para JWT. No cambia en la práctica.

**`SECRET`** — clave secreta con la que se firma el token. Si alguien la conoce puede generar tokens válidos. En producción va en una variable de entorno, nunca en el código.

---

#### `password_hash = PasswordHash.recommended()` — versión oficial actual

```python
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()   # configura Argon2 automáticamente
```

Equivale al `crypt = CryptContext(schemes=["bcrypt"])` de MoureDev pero con `pwdlib` y Argon2. `PasswordHash.recommended()` siempre usa el algoritmo más seguro sin configuración manual.

**Hashear una contraseña:**
```python
password_hash.hash("123456")
# → "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$..."
```

**Verificar:**
```python
password_hash.verify("123456", hash_guardado)
# → True o False
```

El hash siempre es distinto aunque la contraseña sea la misma — Argon2 agrega un "salt" aleatorio. Por eso no podés comparar hashes directamente, siempre se usa `verify`.

> **Con passlib/bcrypt (MoureDev):** `crypt = CryptContext(schemes=["bcrypt"])` → `crypt.verify(password, hash)`
> **Con pwdlib/Argon2 (oficial actual):** `password_hash = PasswordHash.recommended()` → `password_hash.verify(password, hash)`

---

#### `auth_user` — la nueva dependencia de verificación JWT

```python
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    return search_user(username)
```

**`jwt.decode(token, SECRET, algorithms=[ALGORITHM])`** — decodifica el token usando la clave secreta. Si el token fue modificado o la firma no coincide, lanza `JWTError`.

**`.get("sub")`** — extrae el campo `sub` (subject) del payload. Por convención JWT el `sub` contiene el identificador del usuario.

**`try/except JWTError`** — si el token es inválido, expirado o modificado, `jwt.decode` lanza `JWTError` que se captura y devuelve `401`.

En JWT la autorización queda en dos funciones encadenadas:
```
auth_user    → verifica y decodifica el token → devuelve User
current_user → verifica que el usuario esté activo → devuelve User
```

---

#### `POST /login` — generación del token JWT

```python
access_token = {
    "sub": user.username,                                           # identificador del usuario
    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)  # expiración
}
return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}
```

**`"sub": user.username`** — el campo `sub` (subject) es el estándar JWT para identificar al usuario.

**`"exp"`** — fecha de expiración. `datetime.now(timezone.utc)` es la hora actual en UTC y `timedelta(minutes=1)` le suma 1 minuto. Cuando el token expire, `jwt.decode` lanzará `JWTError` automáticamente.

**`jwt.encode(...)`** — genera el token cifrado y firmado. Devuelve el string `eyJhbGci...`.

---

#### Estructura para rellenar — `POST /login` JWT

```python
# Con pwdlib (versión oficial actual)
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = tu_dict.get(form.username)                    # ← nombre de tu dict
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="...")                                    # ← vos definís el mensaje
    user = search_user_db(form.username)                    # ← nombre de tu función
    if not password_hash.verify(form.password, user.password):  # ← pwdlib
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="...")                                    # ← vos definís el mensaje
    access_token = {
        "sub": user.username,                               # ← siempre igual
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

# Con passlib (versión MoureDev)
# if not crypt.verify(form.password, user.password):       # ← passlib
```

#### `auth_user` — estructura para rellenar (versión oficial con PyJWT)

```python
from jwt.exceptions import InvalidTokenError   # antes era from jose import JWTError

# SIEMPRE IGUAL — no cambia nada
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="...",                              # ← vos definís el mensaje
        headers={"WWW-Authenticate": "Bearer"})   # ← siempre igual
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")  # ← siempre igual
        if username is None:
            raise exception
    except InvalidTokenError:                      # ← PyJWT usa InvalidTokenError, no JWTError
        raise exception
    return search_user(username)                   # ← nombre de tu función
```

> **MoureDev usa** `except JWTError` (de `python-jose`) → **versión oficial usa** `except InvalidTokenError` (de `PyJWT`). El comportamiento es idéntico.

---

### Cómo generar contraseñas hasheadas

Las contraseñas en `users_db` deben estar hasheadas. Para generarlas:

```python
# Con pwdlib (versión oficial actual)
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
print(password_hash.hash("tu_contraseña"))
# → "$argon2id$v=19$m=65536,t=3,p=4$..."

# Con passlib (versión MoureDev)
from passlib.context import CryptContext
crypt = CryptContext(schemes=["bcrypt"])
print(crypt.hash("tu_contraseña"))
# → "$2a$12$..."
```

Pegás el resultado en el campo `password` del diccionario.

---

### Cómo probarlo en Postman

**1. Login:**
```
POST http://127.0.0.1:8000/jwtauth/login
Body → form-data:
  username: mouredev
  password: 123456
```

Respuesta:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

**2. Usar el token:**
```
GET http://127.0.0.1:8000/jwtauth/users/me
Headers:
  Authorization: Bearer eyJhbGci...
```

**3. Verificar expiración** — con `ACCESS_TOKEN_DURATION = 1` el token expira en 1 minuto. Esperá y volvé a hacer el GET — debe devolver `401`.

---

### Cómo generar el SECRET en producción

```python
import secrets
print(secrets.token_hex(32))
# → "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"
```

En producción este valor va en una variable de entorno — nunca en el código.

Referencia: [FastAPI - OAuth2 JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) · [JWT.io](https://jwt.io/) · [PyJWT Docs](https://pyjwt.readthedocs.io/) · [pwdlib Docs](https://frankie567.github.io/pwdlib/)