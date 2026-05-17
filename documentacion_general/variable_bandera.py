# ============================================================
# REFERENCIA — VARIABLE BANDERA (FLAG)
# Patrón lógico general de programación
# Fuente: Python Docs — More Control Flow Tools
# https://docs.python.org/3/tutorial/controlflow.html
# Fuente: PEP 8 — Style Guide for Python Code
# https://peps.python.org/pep-0008/
# ============================================================

# La variable bandera no es una función ni un método de Python.
# Es un PATRÓN LÓGICO — una estrategia para rastrear
# si algo ocurrió durante la ejecución de un bloque de código.

# Nombre en inglés: "flag variable" o simplemente "flag".
# En español: bandera, indicador, marcador.


# ============================================================
# 1. ¿Qué es y cómo funciona?
# ============================================================

# Una variable bandera es una variable booleana que:
# 1. Arranca con un valor inicial (casi siempre False)
# 2. Cambia a True si ocurre algo específico durante el código
# 3. Se consulta después para saber qué ocurrió

# Estructura básica:
bandera = False          # 1. Estado inicial: "no ocurrió nada"

# ... código que puede cambiar la bandera ...
condicion = True         # simulando que algo ocurrió
if condicion:
    bandera = True       # 2. Cambio: "sí ocurrió"

if not bandera:          # 3. Consulta: ¿ocurrió o no?
    print("No ocurrió nada.")
else:
    print("Sí ocurrió.")


# ============================================================
# 2. Caso del miniproyecto — eliminar empleado
# ============================================================

empleados = [
    {"nombre": "Andrés",  "salario": 3500000},
    {"nombre": "María",   "salario": 2800000},
    {"nombre": "Carlos",  "salario": 4200000},
]

# Problema: después de recorrer la lista buscando un nombre,
# ¿cómo saber si lo encontré o no?
# El for no avisa si el if se ejecutó alguna vez.

nombre_a_eliminar = "María"
encontrado = False                          # bandera inicial

for x in empleados:
    if x["nombre"] == nombre_a_eliminar:
        empleados.remove(x)
        encontrado = True                   # bandera activada

if not encontrado:
    print(f"{nombre_a_eliminar} no existe en la base de datos.")
else:
    print(f"{nombre_a_eliminar} eliminado correctamente.")

# Sin la bandera, no hay forma de saber si el if
# se ejecutó 0 veces o 1 vez después de que el for termina.


# ============================================================
# 3. ¿Por qué no usar el else del for?
# ============================================================

# Python tiene for/else, pero no hace lo que parece:
# El else del for se ejecuta SIEMPRE que el for termina
# sin un break — no cuando el if no se cumplió.

# Ejemplo del problema:
for x in empleados:
    if x["nombre"] == "Andrés":
        print("Encontrado")
else:
    print("Este print sale SIEMPRE, haya o no coincidencia.")

# Por eso la bandera es más clara y predecible.
# Fuente: https://docs.python.org/3/reference/compound_stmts.html#the-for-statement


# ============================================================
# 4. Casos de uso comunes
# ============================================================

# --- CASO 1: Verificar si existe un elemento en una lista ---
frutas = ["mango", "papaya", "guanábana"]
buscar = "papaya"
existe = False

for fruta in frutas:
    if fruta == buscar:
        existe = True

if existe:
    print(f"{buscar} está en la lista.")
else:
    print(f"{buscar} no está en la lista.")

# Nota: para este caso específico Python tiene "in":
# if buscar in frutas: → más pythónico para listas simples.
# La bandera es útil cuando la lista contiene diccionarios
# y necesitas comparar por una clave específica.


# --- CASO 2: Validar que al menos uno cumple una condición ---
numeros = [4, 7, 2, 9, 1]
hay_par = False

for n in numeros:
    if n % 2 == 0:
        hay_par = True

if hay_par:
    print("Hay al menos un número par.")
else:
    print("No hay números pares.")

# Nota: para este caso Python tiene any():
# any(n % 2 == 0 for n in numeros) → más compacto.
# La bandera es útil cuando la lógica es más compleja
# que una sola condición.


# --- CASO 3: Controlar si una operación fue exitosa ---
def procesar_pago(monto):
    pago_exitoso = False

    if monto <= 0:
        print("Error: monto inválido.")
        return pago_exitoso

    # ... lógica de pago ...
    pago_exitoso = True
    print(f"Pago de {monto} procesado.")
    return pago_exitoso

resultado = procesar_pago(50000)
if resultado:
    print("Continuar con el proceso.")


# --- CASO 4: Evitar operaciones duplicadas ---
# Si en un bucle solo quieres hacer algo UNA vez:
empleados2 = [
    {"nombre": "Andrés", "salario": 3500000},
    {"nombre": "Andrés", "salario": 2800000},  # mismo nombre, distinto registro
]

ya_eliminado = False
nombre_objetivo = "Andrés"

for x in empleados2:
    if x["nombre"] == nombre_objetivo and not ya_eliminado:
        empleados2.remove(x)
        ya_eliminado = True
        print("Primer Andrés eliminado.")


# ============================================================
# 5. Nombres convencionales para banderas
# ============================================================

# No hay regla oficial, pero por convención se usan nombres
# que describen el estado booleano claramente:

encontrado    = False   # ¿se encontró algo?
existe        = False   # ¿existe el elemento?
es_valido     = False   # ¿pasó la validación?
fue_guardado  = False   # ¿se guardó correctamente?
hay_error     = False   # ¿ocurrió un error?
completado    = False   # ¿terminó el proceso?

# Regla práctica: el nombre debe poder leerse como pregunta.
# "¿encontrado?" → si True: sí. Si False: no.


# ============================================================
# 6. ¿Cuándo usar bandera vs alternativas de Python?
# ============================================================

# | Situación                              | Usar                        |
# |----------------------------------------|-----------------------------|
# | Buscar en lista simple                 | if elemento in lista        |
# | Buscar en lista de diccionarios        | bandera + for               |
# | ¿Alguno cumple condición?              | any() o bandera             |
# | ¿Todos cumplen condición?              | all() o bandera             |
# | Confirmar si algo ocurrió en un bucle  | bandera                     |
# | Evitar duplicar una operación          | bandera                     |
# | Controlar flujo entre funciones        | bandera como valor de retorno|

# Regla general:
# Si Python tiene una función built-in que hace lo mismo (in, any, all), úsala — es más legible.
# Si la lógica es compleja o trabaja con diccionarios, la bandera es la herramienta correcta.