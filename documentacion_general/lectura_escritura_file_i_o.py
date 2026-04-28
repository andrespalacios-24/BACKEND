# =============================================================
# REFERENCIA: Manejo de archivos en Python (File I/O)
# Andrés Palacios — Python Básico
# Basado en documentación oficial: docs.python.org
# =============================================================

# -------------------------------------------------------------
# ¿QUÉ ES FILE I/O?
# -------------------------------------------------------------
# File I/O = Input/Output de archivos.
# Es la capacidad de Python para leer y escribir archivos
# en tu computador — como un .txt, .csv, etc.
# Es como una base de datos simple: los datos persisten
# aunque el programa se cierre.

# -------------------------------------------------------------
# LA FUNCIÓN PRINCIPAL: open()
# -------------------------------------------------------------
# Sintaxis:
# open("nombre_archivo.txt", "modo")
#
# El MODO le dice a Python qué vas a hacer con el archivo:
#
# Modo   Nombre    ¿Qué hace?
# ─────────────────────────────────────────────────────────────
# "r"    read      Solo leer. Error si el archivo no existe.
# "w"    write     Escribir. Si existe lo BORRA y empieza de cero.
# "a"    append    Agregar al final. Si no existe, lo crea.
# "r+"   read+     Leer Y escribir al mismo tiempo.
#
# REGLA: Si no especificas modo, Python usa "r" por defecto.

# -------------------------------------------------------------
# LA FORMA CORRECTA: with open()
# -------------------------------------------------------------
# Siempre usa "with open()" — cierra el archivo automáticamente
# aunque ocurra un error. Es la práctica recomendada por la
# documentación oficial de Python.
#
# Forma básica:
# with open("archivo.txt", "modo") as f:
#     # aquí trabajas con el archivo
#     # al salir del bloque, se cierra solo

# -------------------------------------------------------------
# 1. ESCRIBIR EN UN ARCHIVO (modo "w")
# -------------------------------------------------------------
# Crea el archivo si no existe.
# OJO: si ya existe, BORRA todo el contenido anterior.
#
# with open("datos.txt", "w") as f:
#     f.write("Hola mundo\n")          # \n = salto de línea
#     f.write("Segunda línea\n")
#
# → Resultado en datos.txt:
#   Hola mundo
#   Segunda línea

# -------------------------------------------------------------
# 2. AGREGAR SIN BORRAR (modo "a" — append)
# -------------------------------------------------------------
# Agrega al final del archivo sin borrar lo que ya había.
# Si el archivo no existe, lo crea.
# Este es el modo que usas en historial.txt del mini banco.
#
# with open("historial.txt", "a") as f:
#     f.write("Andrés,deposito,500\n")
#
# → Cada vez que se llama, agrega una línea nueva al final.
#   El historial crece sin perder registros anteriores.

# -------------------------------------------------------------
# 3. LEER UN ARCHIVO (modo "r")
# -------------------------------------------------------------
# Tres formas de leer:
#
# → read(): lee TODO el archivo como un solo string
# with open("historial.txt", "r") as f:
#     contenido = f.read()
#     print(contenido)
#
# → readline(): lee UNA línea a la vez
# with open("historial.txt", "r") as f:
#     linea = f.readline()
#     print(linea)
#
# → readlines(): lee TODAS las líneas y las devuelve como lista
# with open("historial.txt", "r") as f:
#     lineas = f.readlines()
#     for linea in lineas:
#         print(linea)
#
# REGLA: Para mostrar historial, usa readlines() o un for
#        que recorra línea por línea.

# -------------------------------------------------------------
# 4. MANEJAR EL ERROR SI EL ARCHIVO NO EXISTE
# -------------------------------------------------------------
# Si intentas leer un archivo que no existe, Python lanza:
# FileNotFoundError
#
# Ya lo usaste en el Miniproyecto 1. Se maneja con try/except:
#
# try:
#     with open("historial.txt", "r") as f:
#         for linea in f:
#             print(linea)
# except FileNotFoundError:
#     print("No hay historial guardado todavía.")

# -------------------------------------------------------------
# RESUMEN DE CUÁNDO USAR CADA MODO
# -------------------------------------------------------------
# ¿Quieres GUARDAR registros sin borrar los anteriores? → "a"
# ¿Quieres CREAR un archivo desde cero?                → "w"
# ¿Quieres LEER lo que hay guardado?                   → "r"
#
# En el mini banco:
#   registrar()    → "a"  (agrega cada operación al historial)
#   ver_historial() → "r"  (lee y muestra todo lo guardado)

# -------------------------------------------------------------
# ESTRUCTURA COMPLETA DE REFERENCIA
# -------------------------------------------------------------
#
# ESCRIBIR/AGREGAR:                    LEER:
# ─────────────────────                ────────────────────────
# with open("x.txt", "a") as f:       with open("x.txt", "r") as f:
#     f.write("dato\n")                   for linea in f:
#                                             print(linea)
#
# → \n al final de write()            → el for recorre línea por línea
#   es obligatorio para que cada        automáticamente
#   registro quede en su propia línea