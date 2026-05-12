"""
MANEJO DE PAQUETES EN PYTHON - pip
===================================
Fuentes:
- https://pip.pypa.io/en/stable/
- https://docs.python.org/3/installing/index.html
- https://packaging.python.org/en/latest/tutorials/installing-packages/
- https://pypi.org

¿Qué es pip?
------------
pip es el gestor de paquetes oficial de Python. Permite instalar, actualizar
y eliminar librerías de terceros alojadas en PyPI (Python Package Index).
PyPI es el repositorio central con más de 500.000 paquetes públicos.

¿Qué es un entorno virtual (venv)?
------------------------------------
Un entorno virtual es un directorio aislado que contiene su propio intérprete
de Python y sus propios paquetes. Sirve para que cada proyecto tenga sus
dependencias específicas sin interferir con otros proyectos ni con el sistema.

Ciclo de vida de un entorno virtual:

  1. Crear:   python3 -m venv venv
  2. Activar: source venv/bin/activate          (Linux/macOS/WSL)
              venv\\Scripts\\activate            (Windows)
  3. Usar pip normalmente mientras esté activo
  4. Salir:   deactivate

Una vez activado, el prompt cambia a: (venv) usuario@maquina:~$
Dentro del venv, 'python' y 'pip' apuntan al entorno aislado.

NOTA WSL/Ubuntu: En Ubuntu 24+ pip3 es el comando por defecto del sistema.
Dentro de un venv activado puedes usar simplemente 'pip'.

"""

# =============================================================================
# COMANDOS PIP ESENCIALES (ejecutar en terminal, no en Python)
# =============================================================================

# --- INSTALACIÓN ---
# pip install nombre_paquete             instala la última versión
# pip install nombre_paquete==2.1.0      instala versión exacta
# pip install nombre_paquete>=2.0        instala versión mínima
# pip install -r requirements.txt        instala todo lo del archivo

# --- DESINSTALACIÓN Y ACTUALIZACIÓN ---
# pip uninstall nombre_paquete           desinstala un paquete
# pip install --upgrade nombre_paquete   actualiza a la última versión

# --- INFORMACIÓN ---
# pip list                               lista todos los paquetes instalados
# pip show nombre_paquete                info detallada: versión, autor, dependencias
# pip freeze                             lista con formato nombre==versión (para requirements.txt)
# pip freeze > requirements.txt          guarda las dependencias del proyecto

# --- requirements.txt ---
# Archivo estándar que lista las dependencias de un proyecto.
# Permite reproducir el entorno exacto en otra máquina con:
# pip install -r requirements.txt
# Ejemplo de contenido:
#   requests==2.31.0
#   numpy==1.26.4
#   pandas==2.2.1


# =============================================================================
# PAQUETES CLAVE PARA BACKEND CON PYTHON
# =============================================================================

"""
REQUESTS — cliente HTTP
-----------------------
Para qué sirve: hacer peticiones a APIs externas (GET, POST, PUT, DELETE).
Cuándo usarlo: consumir APIs REST desde tu código.

Instalación: pip install requests
Documentación: https://docs.python-requests.org
"""
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
print(response.status_code)        # 200 = OK
print(response.json())             # respuesta como diccionario Python
print(response.headers)            # cabeceras HTTP de la respuesta

# POST con body JSON (ejemplo típico en backend)
# payload = {"username": "andres", "password": "1234"}
# response = requests.post("https://api.ejemplo.com/login", json=payload)


"""
NUMPY — cálculo numérico
-------------------------
Para qué sirve: operaciones matemáticas y arrays de alto rendimiento.
Cuándo usarlo: procesamiento de datos numéricos, álgebra lineal, estadística.
Relación con backend: base de pandas, scikit-learn, TensorFlow.

Instalación: pip install numpy
Documentación: https://numpy.org/doc/
"""
import numpy

version = numpy.version.version
print(version)

# Arrays numpy vs listas Python
# Las listas Python son flexibles pero lentas para operaciones numéricas.
# Los arrays numpy son de tipo fijo y operan mucho más rápido.

numeros = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numeros))               # <class 'numpy.ndarray'>
print(numeros * 2)                 # operación sobre todos los elementos
print(numeros.mean())              # promedio
print(numeros.max())               # máximo
print(numeros.min())               # mínimo


"""
PANDAS — análisis de datos
---------------------------
Para qué sirve: manipulación de datos tabulares (tablas, CSV, Excel, SQL).
Cuándo usarlo: leer/limpiar/transformar datasets, generar reportes.
Relación con backend: ETL pipelines, procesamiento de datos antes de guardar en BD.

Instalación: pip install pandas
Documentación: https://pandas.pydata.org/docs/
"""
# import pandas as pd
#
# # Crear DataFrame (tabla de datos)
# datos = {
#     "nombre": ["Ana", "Carlos", "Beatriz"],
#     "edad": [28, 34, 25],
#     "salario": [3500, 4200, 3100]
# }
# df = pd.DataFrame(datos)
# print(df)
# print(df["salario"].mean())       # promedio de columna
# print(df[df["edad"] > 26])        # filtrar filas


"""
FASTAPI — framework web moderno (próximo en el roadmap)
--------------------------------------------------------
Para qué sirve: construir APIs REST con Python de forma rápida y con validación automática.
Cuándo usarlo: cuando necesitas crear endpoints para un backend.
Por qué es relevante: es el framework principal del roadmap de Andrés.

Instalación: pip install fastapi uvicorn

Documentación: https://fastapi.tiangolo.com
"""
# Ejemplo básico (ejecutar con: uvicorn main:app --reload)
# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/pokemon/{nombre}")
# def obtener_pokemon(nombre: str):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}")
#     return response.json()


"""
PYDANTIC — validación de datos
-------------------------------
Para qué sirve: validar y serializar datos con tipado estricto.
Cuándo usarlo: definir esquemas de datos (modelos) en APIs.
Relación con FastAPI: FastAPI usa Pydantic internamente para validar requests y responses.

Instalación: pip install pydantic
Documentación: https://docs.pydantic.dev
"""
# from pydantic import BaseModel
#
# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     activo: bool = True
#
# usuario = Usuario(nombre="Andrés", edad=30)
# print(usuario)


"""
PYTHON-DOTENV — variables de entorno
--------------------------------------
Para qué sirve: cargar variables de entorno desde un archivo .env.
Cuándo usarlo: guardar credenciales, claves de API, configuración sensible.
Práctica de seguridad: nunca hardcodear passwords o API keys en el código.

Instalación: pip install python-dotenv

Archivo .env (no se sube a git):
  DATABASE_URL=postgresql://user:pass@localhost/db
  API_KEY=abc123

Uso:
"""
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# api_key = os.getenv("API_KEY")


# =============================================================================
# PAQUETES PERSONALIZADOS (módulos propios)
# =============================================================================

"""
¿Qué es un paquete en Python?
------------------------------
Un paquete es simplemente una carpeta que contiene módulos (.py) y un archivo
especial llamado __init__.py. Ese archivo le indica a Python que la carpeta
debe tratarse como un paquete importable, no como una carpeta cualquiera.

Sin __init__.py → carpeta normal.
Con __init__.py → paquete Python.

Estructura mínima de un paquete personalizado:

  mi_proyecto/
  │
  ├── main.py                  ← tu script principal
  │
  └── mypackage/               ← el paquete (carpeta)
      ├── __init__.py          ← marca la carpeta como paquete (puede estar vacío)
      └── arithmetics.py       ← módulo con funciones


¿Cómo se crea paso a paso?
---------------------------
1. Crear la carpeta del paquete:
   mkdir mypackage

2. Crear el archivo __init__.py (puede estar vacío):
   touch mypackage/__init__.py

3. Crear el módulo con las funciones:
   touch mypackage/arithmetics.py

4. Escribir las funciones dentro de arithmetics.py:

   # mypackage/arithmetics.py

   def sum_two_values(a, b):
       return a + b

   def multiply(a, b):
       return a * b


¿Cómo se importa desde otro archivo?
--------------------------------------
Desde main.py, que está al mismo nivel que la carpeta mypackage:

   from mypackage import arithmetics
   from mypackage.arithmetics import sum_two_values

   print(arithmetics.sum_two_values(3, 4))   # 7
   print(sum_two_values(3, 4))               # 7  (import directo)

La diferencia entre las dos formas:
- 'from mypackage import arithmetics' importa el módulo completo.
  Accedes a sus funciones con: arithmetics.nombre_funcion()
- 'from mypackage.arithmetics import sum_two_values' importa solo esa función.
  La usas directamente por su nombre sin prefijo.


¿Para qué sirve __init__.py más allá de marcar el paquete?
-----------------------------------------------------------
Puede usarse para exponer funciones directamente desde el paquete,
sin que el usuario tenga que conocer en qué módulo interno viven:

   # mypackage/__init__.py
   from .arithmetics import sum_two_values

Con eso, en main.py puedes hacer:
   from mypackage import sum_two_values   ← importa directo sin mencionar arithmetics

En proyectos pequeños __init__.py suele estar vacío. En librerías grandes
se usa para controlar qué expone el paquete al exterior.


Diferencia entre módulo y paquete:
------------------------------------
- Módulo:  un solo archivo .py          → import math
- Paquete: una carpeta con __init__.py  → from mypackage import arithmetics

Un paquete puede contener múltiples módulos organizados por responsabilidad:
   mypackage/
   ├── __init__.py
   ├── arithmetics.py    ← operaciones matemáticas
   ├── strings.py        ← utilidades de texto
   └── validators.py     ← validaciones de datos

Esto es exactamente lo que hacen librerías grandes como requests o pandas
internamente: son paquetes con muchos módulos organizados por tema.
"""


# =============================================================================
# FLUJO COMPLETO: NUEVO PROYECTO CON ENTORNO VIRTUAL
# =============================================================================

"""
Secuencia recomendada al iniciar cualquier proyecto Python:

1. Crear carpeta del proyecto:
   mkdir mi_proyecto && cd mi_proyecto

2. Crear entorno virtual:
   python3 -m venv venv

3. Activar entorno virtual:
   source venv/bin/activate

4. Instalar paquetes necesarios:
   pip install requests fastapi uvicorn

5. Guardar dependencias:
   pip freeze > requirements.txt

6. Agregar venv al .gitignore:
   echo "venv/" >> .gitignore

7. Al clonar el proyecto en otra máquina:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

IMPORTANTE: el directorio venv/ nunca va al repositorio.
Solo se sube requirements.txt para que cualquiera pueda recrear el entorno.
"""