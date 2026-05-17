# ============================================================
# REFERENCIA — VERDAD Y FALSEDAD EN PYTHON (Truthiness)
# Fuente: Python Docs — Truth Value Testing
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
# ============================================================

# En Python, cualquier objeto puede evaluarse como True o False
# en un contexto booleano (if, while, not, and, or).
# Esto se llama "truthiness" (valor de verdad implícito).

# ============================================================
# 1. if not lista — ¿está vacía?
# ============================================================

# FORMA LARGA (evitar):
empleados = []
if len(empleados) == 0:
    print("No hay empleados.")

# FORMA PYTHONICA (preferida):
if not empleados:
    print("No hay empleados.")

# ¿Por qué funciona?
# En Python, una lista vacía [] evalúa como False.
# Una lista con elementos evalúa como True.
# "not empleados" invierte ese valor:
#   - [] → False → not False → True  → entra al if
#   - [x] → True → not True  → False → no entra al if

# Fuente oficial:
# "By default, an object is considered true unless its class defines
#  either a __bool__() method that returns False, or a __len__() method
#  that returns zero." — Python Docs, Truth Value Testing


# ============================================================
# 2. Valores que evalúan como False en Python
# ============================================================

# Estos son FALSY (se comportan como False en un if):

# | Valor          | Tipo        |
# |----------------|-------------|
# | False          | bool        |
# | None           | NoneType    |
# | 0              | int         |
# | 0.0            | float       |
# | ""             | str vacío   |
# | []             | list vacía  |
# | {}             | dict vacío  |
# | ()             | tuple vacía |
# | set()          | set vacío   |

# Todo lo demás evalúa como True (TRUTHY).

# Ejemplo:
valores = [False, None, 0, 0.0, "", [], {}, (), set()]
for v in valores:
    if not v:
        print(f"{repr(v)} → es Falsy")


# ============================================================
# 3. Casos de uso comunes con if not
# ============================================================

# --- Lista vacía ---
resultados = []
if not resultados:
    print("No se encontraron resultados.")

# --- String vacío ---
nombre = ""
if not nombre:
    print("El nombre no puede estar vacío.")

# --- Diccionario vacío ---
datos = {}
if not datos:
    print("No hay datos cargados.")

# --- Variable None ---
archivo = None
if not archivo:
    print("No se cargó ningún archivo.")


# ============================================================
# 4. if variable — verificar que existe y tiene valor
# ============================================================

# En lugar de: if variable != None and variable != "" and len(variable) > 0
# Puedes escribir simplemente:

personal = ["Andrés", "María"]
if personal:
    print("Hay empleados registrados.")

# Esto funciona porque personal tiene elementos → es Truthy → entra al if.


# ============================================================
# 5. Por qué Python cambia esta lógica
# ============================================================

# En otros lenguajes (Java, C) siempre necesitas comparaciones explícitas:
#   if (lista.size() == 0) { ... }
#   if (nombre != null && !nombre.isEmpty()) { ... }

# Python confía en que el programador entiende el valor de verdad implícito.
# Esto hace el código más legible y conciso.
# La filosofía de Python (PEP 20 — Zen of Python):
#   "Readability counts."
#   "Simple is better than complex."

# Por eso la guía oficial de estilo (PEP 8) dice explícitamente:
# "For sequences, (strings, lists, tuples), use the fact that
#  empty sequences are false."
# → Usar "if not lista:" en lugar de "if len(lista) == 0:"

# Fuente: https://peps.python.org/pep-0008/#programming-recommendations


# ============================================================
# 6. Cuándo NO usar truthiness (casos donde ser explícito es mejor)
# ============================================================

# Si la variable puede ser 0 legítimamente y quieres distinguirlo de None:

salario = 0  # salario válido de 0 (raro, pero posible)

# MAL — esto trata 0 igual que None:
if not salario:
    print("Sin salario")  # ← se ejecuta aunque salario sea 0 válido

# BIEN — comparación explícita:
if salario is None:
    print("Salario no definido")

# Regla: usa truthiness cuando vacío/cero significa "no hay nada".
# Usa comparación explícita cuando 0 o "" son valores válidos del dominio.