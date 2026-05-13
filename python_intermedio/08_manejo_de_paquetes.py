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
Para qué sirve: hacer peticiones HTTP a APIs externas desde Python.
Cuándo usarlo: consumir APIs REST, descargar datos, interactuar con servicios web.

Instalación: pip install requests
Documentación oficial: https://docs.python-requests.org
Referencia HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


¿QUÉ ES HTTP?
--------------
HTTP (HyperText Transfer Protocol) es el protocolo que define cómo se
comunican cliente y servidor en la web. Cada vez que tu código hace una
petición a una API, está hablando HTTP.

El flujo es siempre:
  Cliente (tu código) → petición → Servidor (la API)
  Servidor            → respuesta (datos + código de estado) → Cliente


MÉTODOS HTTP
-------------
Los métodos indican qué quieres hacer con el recurso:

  GET     → obtener datos          (leer, no modifica nada)
  POST    → enviar/crear datos     (crear un nuevo recurso)
  PUT     → reemplazar datos       (actualizar un recurso completo)
  PATCH   → modificar parcialmente (actualizar solo algunos campos)
  DELETE  → eliminar datos         (borrar un recurso)

En backend con FastAPI definirás endpoints para cada uno de estos métodos.


CÓDIGOS DE ESTADO HTTP
-----------------------
El servidor responde siempre con un código numérico que indica qué pasó.
Se agrupan por rango:

  2xx — Éxito
    200 OK                  → petición exitosa (GET estándar)
    201 Created             → recurso creado correctamente (POST exitoso)
    204 No Content          → éxito pero sin datos que devolver (DELETE exitoso)

  3xx — Redirección
    301 Moved Permanently   → el recurso cambió de URL de forma permanente
    302 Found               → redirección temporal

  4xx — Error del cliente (el problema está en quien hace la petición)
    400 Bad Request         → petición mal formada o con datos inválidos
    401 Unauthorized        → no autenticado (falta token o credenciales)
    403 Forbidden           → autenticado pero sin permisos para ese recurso
    404 Not Found           → el recurso no existe en esa URL
    422 Unprocessable Entity→ datos con formato válido pero contenido inválido
                              (FastAPI lo usa para errores de validación)

  5xx — Error del servidor (el problema está en el servidor)
    500 Internal Server Error → error inesperado en el servidor
    502 Bad Gateway           → el servidor recibió una respuesta inválida
    503 Service Unavailable   → servidor caído o sobrecargado

En tu API FastAPI tú decides qué código devuelve cada endpoint según lo que ocurra.
Por ejemplo: si el usuario pide un recurso que no existe → devuelves 404.


EL OBJETO RESPONSE
-------------------
requests.get() devuelve un objeto Response con toda la información de la respuesta.
Sus atributos más usados:
"""
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")

print(response.status_code)        # código de estado: 200, 404, 500, etc.
print(response.ok)                 # True si status_code está entre 200-299
print(response.json())             # cuerpo de la respuesta como dict/list Python
print(response.text)               # cuerpo de la respuesta como string crudo
print(response.headers)            # cabeceras HTTP de la respuesta
print(response.url)                # URL final de la petición (útil si hubo redirección)

# Buena práctica: verificar status_code antes de usar los datos
if response.status_code == 200:
    datos = response.json()
else:
    print(f"Error: {response.status_code}")

# Forma más pythónica con response.ok
if response.ok:
    datos = response.json()


"""
MÉTODOS HTTP CON REQUESTS
--------------------------
Fuente: https://docs.python-requests.org/en/latest/user/quickstart/
"""

# GET — obtener datos (el más común al consumir APIs)
# response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# GET con parámetros en la URL (query params)
# Los query params son filtros que se pasan en la URL después del '?'
# Se separan con '&' si hay más de uno: ?limit=5&offset=10
#
# limit  → cuántos resultados devuelve la API en una petición
#           sin limit: PokeAPI devuelve 20 por defecto
#           limit=5:   devuelve solo 5
#           limit=151: devuelve los 151 Pokémon originales
#
# offset → desde qué posición empieza a contar
#           offset=0:  desde el primero (por defecto)
#           offset=20: salta los primeros 20, empieza desde el 21
#           Combinado con limit permite paginar resultados
#
# Cuándo se usa en backend:
# - Paginación de endpoints (no devolver miles de registros de golpe)
# - Filtrar desde el origen para no procesar más de lo necesario
# - Optimizar rendimiento y consumo de memoria
#
# Forma 1 — directo en la URL
# response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
#
# Forma 2 — con offset
# response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5&offset=10")
#
# Forma 3 — usando params (recomendada, más limpia)
# params = {"limit": 5, "offset": 0}
# response = requests.get("https://pokeapi.co/api/v2/pokemon", params=params)
# requests construye la URL automáticamente: .../pokemon?limit=5&offset=0
#
# Ejemplo completo: nombres de los primeros 5 Pokémon
# response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
# for pokemon in response.json()["results"]:
#     print(pokemon["name"])

# POST — enviar datos para crear un recurso
# payload = {"username": "andres", "password": "1234"}
# response = requests.post("https://api.ejemplo.com/usuarios", json=payload)

# PUT — reemplazar un recurso completo
# payload = {"username": "andres", "email": "nuevo@email.com"}
# response = requests.put("https://api.ejemplo.com/usuarios/1", json=payload)

# DELETE — eliminar un recurso
# response = requests.delete("https://api.ejemplo.com/usuarios/1")

# Enviar headers personalizados (autenticación con token, por ejemplo)
# headers = {"Authorization": "Bearer mi_token_aqui"}
# response = requests.get("https://api.privada.com/datos", headers=headers)


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
Documentación oficial: https://pandas.pydata.org/docs/


¿QUÉ ES UN DATAFRAME?
-----------------------
Un DataFrame es una tabla de datos bidimensional con filas y columnas nombradas.
Es el equivalente en Python a una hoja de Excel o una tabla de base de datos.

Visualmente, esto es un DataFrame:

  | nombre  | edad | salario |
  |---------|------|---------|
  | Ana     | 28   | 3500    |
  | Carlos  | 34   | 4200    |
  | Beatriz | 25   | 3100    |

Cada columna es una variable (campo).
Cada fila es un registro (un elemento del conjunto de datos).

¿Para qué se usa en backend?
- Leer datos de un CSV o Excel y procesarlos antes de guardarlos en la BD
- Limpiar o transformar datos que vienen de una API externa
- Generar reportes o estadísticas sobre datos almacenados
- Filtrar, ordenar y agrupar conjuntos de datos grandes

pandas importa con el alias 'pd' por convención universal.
"""
# import pandas as pd
#
# # Crear DataFrame desde un diccionario
# # Las keys son los nombres de columna, los values son las listas de datos
# datos = {
#     "nombre": ["Ana", "Carlos", "Beatriz"],
#     "edad": [28, 34, 25],
#     "salario": [3500, 4200, 3100]
# }
# df = pd.DataFrame(datos)
# print(df)                          # muestra la tabla completa
#
# # Operaciones básicas
# print(df["salario"].mean())        # promedio de la columna salario
# print(df["nombre"])                # una sola columna como Serie
# print(df[df["edad"] > 26])         # filtrar filas por condición
# print(df.describe())               # estadísticas generales de columnas numéricas
# print(len(df))                     # número de filas
#
# # Leer desde un archivo CSV (muy común en backend)
# # df = pd.read_csv("datos.csv")
# # df.to_csv("resultado.csv", index=False)   # guardar de vuelta a CSV


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