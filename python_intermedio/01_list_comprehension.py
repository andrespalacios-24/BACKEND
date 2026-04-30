# ============================================================
#              LIST COMPREHENSION — Notas de estudio
# ============================================================
# Sintaxis base:
#   [expresion for elemento in iterable]
#   [expresion for elemento in iterable if condicion]
#
# ¿Cuándo usarla?
#   - Cuando quieres crear una lista NUEVA a partir de otra
#     colección o rango, en una sola línea.
#   - Sustituye al patrón clásico:
#       lista = []
#       for x in iterable:
#           lista.append(expresion)
#
# ¿Cuándo NO usarla?
#   - Cuando la lógica es compleja y la línea queda ilegible.
#   - Cuando el objetivo no es construir una lista
#     (para eso existen dict/set comprehensions o generators).
# ============================================================


# ── 1. FORMA BÁSICA ─────────────────────────────────────────
# Crear una lista con los cuadrados de 0 al 7
cuadrados = [i * i for i in range(8)]
print(cuadrados)   # [0, 1, 4, 9, 16, 25, 36, 49]


# ── 2. CON CONDICIÓN (filtro) ────────────────────────────────
# Crear una lista solo con números pares de 0 al 9
pares = [i for i in range(10) if i % 2 == 0]
print(pares)       # [0, 2, 4, 6, 8]

# Filtrar números negativos de una lista existente
temperaturas = [22, -3, 18, -7, 30, 0]
positivas = [t for t in temperaturas if t > 0]
print(positivas)   # [22, 18, 30]


# ── 3. MODIFICAR VALORES DE UNA LISTA EXISTENTE ─────────────
# Cuando ya tienes una lista y quieres transformar cada elemento.
# La comprehension crea una lista NUEVA — no modifica la original.
#
# ¿Por qué es útil en backend?
#   Recibes datos crudos (de una API, BD, formulario) y necesitas
#   aplicar una operación uniforme a todos antes de procesarlos.

numeros = [10, 20, 30, 40, 50]

# Aumentar en 5 cada número
aumentados = [n + 5 for n in numeros]
print(aumentados)     # [15, 25, 35, 45, 55]

# Duplicar cada número
duplicados = [n * 2 for n in numeros]
print(duplicados)     # [20, 40, 60, 80, 100]

# Reducir un 10% (descuento)
con_descuento = [round(n * 0.9, 2) for n in numeros]
print(con_descuento)  # [9.0, 18.0, 27.0, 36.0, 45.0]

# Caso real — aplicar descuento a precios de productos en una tienda:
precios_originales = [150, 89, 320, 45, 210]
precios_rebajados = [round(p * 0.85, 2) for p in precios_originales]
print(precios_rebajados)  # [127.5, 75.65, 272.0, 38.25, 178.5]

# NOTA IMPORTANTE: la lista original nunca cambia
print(precios_originales)  # [150, 89, 320, 45, 210] — intacta


# ── 3b. CON FUNCIÓN EXTERNA ─────────────────────────────────
# Cuando la operación es compleja, se extrae a una función
# definida FUERA de la comprehension y se llama dentro.
# Ventaja: el código queda limpio y la función es reutilizable.

def agregar_impuesto(precio):
    return round(precio * 1.19, 2)

precios = [100, 250, 80, 400]
precios_con_iva = [agregar_impuesto(p) for p in precios]
print(precios_con_iva)  # [119.0, 297.5, 95.2, 476.0]

# Caso real — escalar notas de 0-10 a 0-100:
def escalar_nota(nota):
    return round(nota * 10, 1)

notas_raw = [7.5, 8.2, 6.0, 9.1, 5.5]
notas_escaladas = [escalar_nota(n) for n in notas_raw]
print(notas_escaladas)  # [75.0, 82.0, 60.0, 91.0, 55.0]


# ── 4. TRANSFORMAR STRINGS ──────────────────────────────────
# Normalizar nombres de usuarios (backend: datos de formulario)
nombres_raw = ["  ANDRÉS ", " juanita", "PEDRO  "]
nombres_limpios = [n.strip().capitalize() for n in nombres_raw]
print(nombres_limpios)  # ['Andrés', 'Juanita', 'Pedro']


# ── 4b. ITERAR UN STRING — el string es iterable directamente ──
# Un string se puede recorrer carácter a carácter, igual que una lista.
# NO necesitas range() ni len() para esto.
#
# ¿Por qué es útil?
#   En backend recibes texto: usernames, contraseñas, códigos, emails.
#   Necesitas inspeccionarlo carácter por carácter para validarlo.

nombre = "maykel"
caracteres = [c for c in nombre]
print(caracteres)  # ['m', 'a', 'y', 'k', 'e', 'l']

# Caso real — validar que una contraseña tiene al menos una vocal:
password = "m4ykel99"
vocales_en_password = [c for c in password if c in "aeiouAEIOU"]
print(vocales_en_password)  # ['a', 'e']
# Si la lista está vacía → la contraseña no tiene vocales → rechazarla.

# Caso real — extraer solo los dígitos de un código alfanumérico:
codigo = "AB3C7D1"
digitos = [c for c in codigo if c.isdigit()]
print(digitos)  # ['3', '7', '1']


# ── 4c. TERCER ARGUMENTO DE range() — el paso ───────────────
# range(inicio, fin, paso) — de cuánto en cuánto salta.
# Útil cuando sabes el patrón de salto desde el inicio,
# más eficiente que generar todos los números y filtrar con if.

# Pares del 0 al 20 con paso (más eficiente que usar if i % 2 == 0)
pares_paso = [i for i in range(0, 21, 2)]
print(pares_paso)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Impares del 1 al 19
impares_paso = [i for i in range(1, 20, 2)]
print(impares_paso)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Caso real — paginar resultados de una BD en bloques de 10:
# Si tienes 100 registros y quieres los índices de inicio de cada página:
paginas = [i for i in range(0, 100, 10)]
print(paginas)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


# ── 5. CONTEXTO BACKEND — casos reales ──────────────────────

# 5a. Extraer un campo de una lista de dicts
#     (simula filas de una BD / respuesta de API)
usuarios = [
    {"id": 1, "username": "andres", "activo": True},
    {"id": 2, "username": "maria",  "activo": False},
    {"id": 3, "username": "pedro",  "activo": True},
]

# Obtener solo los usernames activos
activos = [u["username"] for u in usuarios if u["activo"]]
print(activos)  # ['andres', 'pedro']

# Obtener todos los IDs
ids = [u["id"] for u in usuarios]
print(ids)      # [1, 2, 3]


# 5b. Construir un nuevo dict de respuesta (API response)
#     Quieres devolver solo id y username, sin el campo 'activo'
respuesta = [{"id": u["id"], "username": u["username"]} for u in usuarios]
print(respuesta)
# [{'id': 1, 'username': 'andres'}, {'id': 2, 'username': 'maria'}, ...]


# 5c. Validar o transformar datos entrantes
#     Recibiste una lista de emails desde un formulario
emails_raw = ["ANDRES@gmail.com", "  MARIA@outlook.com  ", "pedro@yahoo.com"]
emails_normalizados = [e.strip().lower() for e in emails_raw]
print(emails_normalizados)
# ['andres@gmail.com', 'maria@outlook.com', 'pedro@yahoo.com']


# 5d. Filtrar IDs inválidos antes de consultar la BD
ids_recibidos = [1, -5, 3, 0, 7, -1]
ids_validos = [i for i in ids_recibidos if i > 0]
print(ids_validos)  # [1, 3, 7]


# ── 6. COMPARACIÓN: bucle clásico vs comprehension ──────────

# Bucle clásico
resultado_clasico = []
for i in range(5):
    resultado_clasico.append(i ** 2)

# List comprehension equivalente
resultado_comprension = [i ** 2 for i in range(5)]

print(resultado_clasico == resultado_comprension)  # True
# → Misma lógica, menos código, más legible para casos simples.


# ── 7. LÍMITE: cuándo es mejor el bucle clásico ─────────────
# Si necesitas lógica en múltiples pasos, el bucle es más claro.

# Esto se vuelve difícil de leer:
# complicado = [procesar(x) if condicion_a(x) else transformar(x) for x in datos if validar(x)]

# Mejor así:
# resultado = []
# for x in datos:
#     if validar(x):
#         if condicion_a(x):
#             resultado.append(procesar(x))
#         else:
#             resultado.append(transformar(x))

# ============================================================
# RESUMEN
# ============================================================
# [expresion for x in iterable]              → transformar
# [expresion for x in iterable if condicion] → transformar + filtrar
# Úsala cuando: 1 línea, lógica simple, construyes una lista nueva.
# Evítala cuando: lógica compleja, múltiples condiciones anidadas.
# ============================================================


# ── 8. EXPRESIONES BOOLEANAS EN COMPREHENSION ───────────────
# La expresión al inicio no tiene que ser un número.
# Puede ser cualquier cosa que Python evalúe — incluyendo comparaciones.
# Una comparación como n > 10 devuelve True o False directamente.
#
# Estructura:
#   [expresion   for elemento in iterable]
#   [n > 10      for n       in numeros  ]
#    ↑ esto es lo que se guarda en la lista
#
# ¿Por qué va al inicio?
#   Porque esa es la posición de "lo que quieres que quede en la lista".
#   Antes ponías: n + 5, i ** 2, t * 1.8 + 32 — valores transformados.
#   Ahora pones:  n > 10 — el resultado de una comparación (True/False).
#   La posición es siempre la misma, cambia el tipo de expresión.

lista_numeros = [11, 15, 20, 50, 100, 9, 5, 2, 0, -5]
booleanos = [n > 10 for n in lista_numeros]
print(booleanos)  # [True, True, True, True, True, False, False, False, False, False]

# Caso real — marcar qué productos están por encima del precio promedio:
precios_productos = [30, 120, 85, 200, 15, 95, 60]
promedio = sum(precios_productos) / len(precios_productos)
sobre_promedio = [p > promedio for p in precios_productos]
print(sobre_promedio)  # [False, True, True, True, False, True, False]
# En una API esto sirve para resaltar productos destacados sin filtrarlos:
# conservas todos los elementos, pero sabes cuáles cumplen la condición.

# Caso real — verificar qué usuarios han completado su perfil (tienen email):
usuarios = [
    {"username": "andres", "email": "andres@gmail.com"},
    {"username": "maria",  "email": ""},
    {"username": "pedro",  "email": "pedro@yahoo.com"},
]
perfil_completo = [bool(u["email"]) for u in usuarios]
print(perfil_completo)  # [True, False, True]
# bool("") → False, bool("texto") → True


# ── 9. COMPREHENSION ANIDADA — matriz 3x3 ───────────────────
# Una comprehension anidada es una comprehension DENTRO de otra.
# La expresión del inicio (lo que se guarda) puede ser otra lista.
#
# Estructura:
#   [ [expresion_interna for x in rango_interno] for y in rango_externo ]
#     ↑ esto genera una lista...          ↑ ...repetida N veces
#
# Cómo leerla (de afuera hacia adentro):
#   1. El for externo controla cuántas filas habrá.
#   2. El for interno controla qué números van en cada fila.
#
# ── El problema a resolver ──────────────────────────────────
# Queremos:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Patrón de inicio de cada fila:
#   fila 0 → empieza en 1  →  fila * 3 + 1 = 0 * 3 + 1 = 1
#   fila 1 → empieza en 4  →  fila * 3 + 1 = 1 * 3 + 1 = 4
#   fila 2 → empieza en 7  →  fila * 3 + 1 = 2 * 3 + 1 = 7
#
# Cada fila tiene 3 números seguidos desde ese inicio:
#   range(inicio, inicio + 3)
#
# Solución completa:
matriz = [
    [i for i in range(fila * 3 + 1, fila * 3 + 4)]
    for fila in range(3)
]
print(matriz)       # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])    # [1, 2, 3]  → fila 0
print(matriz[1])    # [4, 5, 6]  → fila 1
print(matriz[2][1]) # 5          → fila 2, columna 1 (índice base 0)

# ── Caso real backend — tabla de horarios ───────────────────
# Imagina que tienes 9 turnos numerados del 1 al 9
# y los necesitas organizados en 3 días con 3 turnos cada uno:
horarios = [
    [turno for turno in range(dia * 3 + 1, dia * 3 + 4)]
    for dia in range(3)
]
print(horarios)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Día 0 → turnos 1, 2, 3
# Día 1 → turnos 4, 5, 6
# Día 2 → turnos 7, 8, 9

# ── Caso real backend — tabla de permisos (roles) ───────────
# En sistemas de usuarios, los permisos suelen organizarse
# como una matriz: filas = roles, columnas = recursos.
# True = tiene acceso, False = no tiene acceso.
roles = ["admin", "editor", "viewer"]
recursos = ["leer", "escribir", "eliminar"]

permisos = [
    [True if rol == "admin" or (rol == "editor" and recurso != "eliminar")
     else False
     for recurso in recursos]
    for rol in roles
]
for rol, fila in zip(roles, permisos):
    print(f"{rol}: {fila}")
# admin:  [True, True, True]
# editor: [True, True, False]
# viewer: [False, False, False]