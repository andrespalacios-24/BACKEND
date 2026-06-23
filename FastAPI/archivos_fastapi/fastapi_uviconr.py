# =============================================================
# FASTAPI + UVICORN — REFERENCIA DE COMANDOS
# Fuentes: fastapi.tiangolo.com | uvicorn.org
# =============================================================

# -------------------------------------------------------------
# 1. ENTORNO VIRTUAL (siempre primero)
# -------------------------------------------------------------

# Crear el entorno virtual dentro de la carpeta del proyecto
# python3 -m venv .venv

# Activar el entorno virtual (WSL / Ubuntu)
# source .venv/bin/activate
# → Verás el prefijo (.venv) en tu terminal

# Desactivar el entorno virtual
# deactivate

# -------------------------------------------------------------
# 2. INSTALACIÓN
# -------------------------------------------------------------

# Instalar FastAPI con todas las dependencias (versión del curso)
# pip install "fastapi[all]"

# Instalar solo las dependencias estándar recomendadas
# pip install "fastapi[standard]"

# Verificar que FastAPI quedó instalado correctamente
# pip show fastapi

# Guardar dependencias del proyecto
# pip freeze > requirements.txt

# Instalar desde requirements.txt (en otra máquina o entorno)
# pip install -r requirements.txt

# -------------------------------------------------------------
# 3. ESTRUCTURA MÍNIMA DE UN PROYECTO
# -------------------------------------------------------------

# ~/BACKEND/FastAPI/
# ├── .venv/              ← entorno virtual (NO se sube a GitHub)
# ├── main.py             ← archivo principal de la API
# ├── .gitignore          ← debe incluir .venv/
# └── requirements.txt

# -------------------------------------------------------------
# 4. CORRER EL SERVIDOR
# -------------------------------------------------------------

# Forma 1 — CLI de FastAPI (más corto, recomendado en el curso)
# Desarrollo con auto-reload:
# fastapi dev main.py

# Producción sin auto-reload:
# fastapi run main.py

# Forma 2 — Uvicorn directo (más control)
# Desarrollo con auto-reload:
# uvicorn main:app --reload

# Producción sin auto-reload (más estable):
# uvicorn main:app

# Con puerto personalizado (si el 8000 está ocupado):
# uvicorn main:app --reload --port 8001

# Con host expuesto (para acceder desde otra máquina en la red):
# uvicorn main:app --reload --host 0.0.0.0

# ¿Qué significa "main:app"?
# main → nombre del archivo Python (main.py) sin la extensión
# app  → nombre de la variable donde creaste la instancia FastAPI()

# -------------------------------------------------------------
# 5. DIFERENCIA ENTRE fastapi dev y uvicorn --reload
# -------------------------------------------------------------

# Son equivalentes en desarrollo, hacen lo mismo:
# auto-reload al guardar cambios y servidor local en puerto 8000.
# fastapi dev main.py    → más corto, busca main.py automáticamente
# uvicorn main:app --reload → más explícito, más control

# IMPORTANTE: --reload es SOLO para desarrollo.
# En producción se usa uvicorn sin --reload (o Gunicorn + Nginx).

# -------------------------------------------------------------
# 6. URLS IMPORTANTES EN DESARROLLO
# -------------------------------------------------------------

# API principal:
# http://127.0.0.1:8000

# Documentación interactiva automática (Swagger UI):
# http://127.0.0.1:8000/docs

# Documentación alternativa (ReDoc):
# http://127.0.0.1:8000/redoc

# -------------------------------------------------------------
# 7. ERRORES COMUNES Y SOLUCIONES
# -------------------------------------------------------------

# ERROR: Address already in use (puerto 8000 ocupado)
# → El servidor ya está corriendo en otra terminal o VSCode lo levantó
# Solución — matar todos los procesos de uvicorn:
# pkill -f uvicorn

# Verificar qué proceso está usando el puerto 8000:
# lsof -i :8000

# Matar por PID (reemplaza 1234 con el número que aparece):
# kill 1234

# Correr en otro puerto para evitar el conflicto:
# uvicorn main:app --reload --port 8001

# ERROR: Could not import module "main"
# → El archivo main.py no existe en la carpeta actual, o tienes
#   un typo en el nombre
# Solución — verificar ubicación y contenido:
# pwd       → confirma en qué carpeta estás
# ls        → confirma que main.py existe ahí

# ERROR: externally-managed-environment
# → Ubuntu no permite instalar paquetes fuera de un entorno virtual
# Solución — activar el .venv antes de instalar:
# source .venv/bin/activate
# pip install "fastapi[all]"

# -------------------------------------------------------------
# 8. CÓDIGO MÍNIMO FUNCIONAL (main.py)
# -------------------------------------------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Hola FastAPI"}

# Luego en la terminal:
# uvicorn main:app --reload
# o bien:
# fastapi dev main.py

# -------------------------------------------------------------
# 9. GITIGNORE RECOMENDADO PARA FASTAPI
# -------------------------------------------------------------

# Contenido sugerido para .gitignore:
# .venv/
# __pycache__/
# *.pyc
# .env

# Agregar .venv al .gitignore desde la terminal:
# echo ".venv/" >> .gitignore