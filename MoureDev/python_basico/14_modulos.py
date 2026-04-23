# ============================================================
#  MÓDULOS EN PYTHON — Guía de referencia personal
#  Basado en ejemplos de MoureDev + docs oficiales de Python
# ============================================================


# ¿QUÉ ES UN MÓDULO?
# ------------------
# Un módulo es simplemente un archivo .py que contiene código
# (funciones, variables, clases) que podés reutilizar en otros archivos.
#
# Hay 3 tipos de módulos:
#   1. Los que vienen con Python (módulos estándar) → ej: math, os, random
#   2. Los que instalás con pip (librerías externas)  → ej: fastapi, requests
#   3. Los que vos mismo creás                        → ej: my_module.py


# ============================================================
#  FORMAS DE IMPORTAR UN MÓDULO
# ============================================================

# --- FORMA 1: import <modulo> ---
# Importa el módulo completo. Para usar algo, tenés que escribir
# el nombre del módulo como prefijo.

import math

print(math.pi)          # 3.141592653589793
print(math.pow(2, 8))   # 256.0

# ✅ Ventaja: queda claro de dónde viene cada función.
# ⚠️  Desventaja: hay que escribir "math." cada vez.


# --- FORMA 2: from <modulo> import <nombre> ---
# Importa solo lo que necesitás. Podés usarlo directamente
# sin el prefijo del módulo.

from math import pi

print(pi)   # 3.141592653589793

# ✅ Ventaja: código más corto.
# ⚠️  Riesgo: si tenés otra variable llamada "pi" en tu código, se pisa.


# --- FORMA 3: from <modulo> import <nombre> as <alias> ---
# Igual que la forma 2, pero le ponés un alias (apodo) al nombre importado.
# Útil cuando el nombre es largo o puede generar confusión.

from math import pi as PI_VALUE

print(PI_VALUE)   # 3.141592653589793

# ✅ Ventaja: evitás colisiones de nombres y podés acortar nombres largos.
# Ejemplo clásico en el mundo real:
#   import numpy as np       → np.array(...)
#   import pandas as pd      → pd.DataFrame(...)


# --- FORMA 4: from <modulo> import * ---
# Importa TODO lo que tiene el módulo de una sola vez.

# from math import *
# print(sqrt(16))   # podés usar sqrt directamente

# ❌ NO recomendado: ensucia el espacio de nombres, no sabés qué viene de dónde.
# Solo se usa en contextos muy específicos (ej: scripts rápidos, REPLs).


# ============================================================
#  IMPORTAR UN MÓDULO PROPIO (archivo .py que vos creaste)
# ============================================================

# Supongamos que tenés este archivo en la misma carpeta:
#
# --- my_module.py ---
#
#   def sumValue(numberOne, numberTwo, numberThree):
#       print(numberOne + numberTwo + numberThree)
#
#   def printValue(value):
#       print(value)
#
# --------------------

# Para usarlo, importás igual que cualquier módulo:

# OPCIÓN A: import completo → usás el prefijo
import my_module

my_module.sumValue(5, 3, 1)        # imprime 9
my_module.printValue("Hola!")      # imprime Hola!

# OPCIÓN B: from → importás solo lo que necesitás, sin prefijo
from my_module import sumValue, printValue

sumValue(5, 3, 1)        # imprime 9
printValue("Hola!")      # imprime Hola!

# ⚠️  IMPORTANTE: el archivo my_module.py tiene que estar en la misma
# carpeta que el archivo desde donde lo importás (o en una ruta conocida
# por Python). Si no, vas a ver un ModuleNotFoundError.


# ============================================================
#  ¿CUÁNDO USAR CADA FORMA?
# ============================================================

# import math
#   → Cuando vas a usar varias cosas del módulo.
#     Tener el prefijo "math." hace el código más legible.

# from math import sqrt
#   → Cuando solo necesitás una o dos cosas puntuales.

# from math import sqrt as raiz
#   → Cuando el nombre original es confuso, muy largo, o choca
#     con algo que ya tenés en tu código.

# import my_module
#   → Para tus propios módulos. El prefijo deja en claro
#     que la función viene de un archivo externo tuyo.


# ============================================================
#  MÓDULOS ESTÁNDAR MÁS USADOS (referencia rápida)
# ============================================================

# math      → operaciones matemáticas (pi, sqrt, pow, floor, ceil...)
# random    → números aleatorios (random(), randint(), choice()...)
# os        → interacción con el sistema operativo (rutas, variables de entorno...)
# sys       → información del intérprete de Python
# datetime  → manejo de fechas y horas
# json      → leer y escribir JSON
# re        → expresiones regulares


# ============================================================
#  RESUMEN VISUAL
# ============================================================

# import math                          → math.pi, math.pow()
# from math import pi                  → pi  (sin prefijo)
# from math import pi as PI_VALUE      → PI_VALUE  (con alias)
# import my_module                     → my_module.sumValue()
# from my_module import sumValue       → sumValue()  (sin prefijo)