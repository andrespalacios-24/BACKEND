# ============================================================
# EXPRESIONES REGULARES EN PYTHON — regex_backend.py
# Módulo: re (built-in, no necesita instalación)
# Documentación oficial: https://docs.python.org/3/library/re.html
# Para practicar patrones: https://regex101.com
# ============================================================

import re

# ============================================================
# ¿QUÉ ES UNA EXPRESIÓN REGULAR?
# ============================================================
# Una expresión regular (RegEx) es un patrón de texto que describes
# para buscar, validar o manipular cadenas.
# Ejemplo: quieres saber si un string tiene un email → defines el patrón
# de cómo se ve un email y lo comparas contra el string.
#
# En Python, el módulo `re` es quien maneja todo esto.
# Siempre que trabajes con patrones, los escribes con r"..." (raw string)
# para que Python no interprete los \ como secuencias de escape normales.


# ============================================================
# LAS 5 FUNCIONES PRINCIPALES DE re
# ============================================================

texto = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
otro  = "Esta no es la lección número 6: Manejo de ficheros"


# ------------------------------------------------------------
# 1. re.match(pattern, string, flags=0)
# ------------------------------------------------------------
# Busca el patrón SOLO desde el INICIO del string.
# Si el string no empieza exactamente con el patrón → retorna None.
# Retorna un Match object si encuentra, None si no.
#
# ¿Cuándo usarlo?
# → Cuando quieres validar que un string EMPIEZA con algo concreto.
# → Validar que una línea de log empieza con una fecha, un comando, etc.
#
# .span()       → retorna (inicio, fin) de la coincidencia
# .group()      → retorna el texto que coincidió
# .start()      → posición de inicio
# .end()        → posición de fin
# .groups()     → tupla con grupos capturados (ver sección de grupos)

resultado = re.match(r"Esta es la lección", texto, re.IGNORECASE)
print(resultado)                    # <re.Match object ...>
print(resultado.group())            # "Esta es la lección"
print(resultado.span())             # (0, 18)
print(resultado.start())            # 0
print(resultado.end())              # 18

# re.match falla si el patrón no está al inicio
sin_match = re.match(r"Expresiones Regulares", texto)
print(sin_match)                    # None  ← está al final, no al inicio

# Siempre verifica antes de usar el resultado para no crashear:
if sin_match is not None:
    print(sin_match.group())
else:
    print("No hubo coincidencia al inicio")


# ------------------------------------------------------------
# 2. re.search(pattern, string, flags=0)
# ------------------------------------------------------------
# Busca el patrón en CUALQUIER PARTE del string.
# Retorna el PRIMER match que encuentra, no todos.
# Retorna un Match object si encuentra, None si no.
#
# ¿Cuándo usarlo?
# → Cuando quieres saber si un patrón existe en algún lugar del string.
# → Buscar si un log contiene un código de error, si un texto menciona
#   una palabra clave, si un string tiene al menos un dígito, etc.
#
# Mismos métodos del Match object: .group(), .span(), .start(), .end()

resultado = re.search(r"lección", texto, re.IGNORECASE)
print(resultado)                    # <re.Match object ...>
print(resultado.group())            # "lección"
print(resultado.span())             # (11, 18) ← posición en el string

# Diferencia clave match vs search:
# re.match(r"lección", texto)   → None  (no está al inicio)
# re.search(r"lección", texto)  → Match (está en el medio)


# ------------------------------------------------------------
# 3. re.findall(pattern, string, flags=0)
# ------------------------------------------------------------
# Busca TODAS las coincidencias en el string.
# Retorna una LISTA de strings (no Match objects).
# Si no encuentra nada → lista vacía [].
#
# ¿Cuándo usarlo?
# → Extraer todos los emails de un texto, todos los números de una factura,
#   todas las palabras que cumplen un patrón, etc.
# → Es el más usado en backend para extracción de datos.

resultado = re.findall(r"lección", texto, re.IGNORECASE)
print(resultado)    # ['lección', 'Lección']  ← las encontró ambas

# Con grupos capturados, findall retorna lista de tuplas:
resultado_grupos = re.findall(r"(lección|número)", texto, re.IGNORECASE)
print(resultado_grupos)  # ['lección', 'número', 'Lección']


# ------------------------------------------------------------
# 4. re.split(pattern, string, maxsplit=0, flags=0)
# ------------------------------------------------------------
# Divide el string usando el patrón como separador.
# Retorna una LISTA de partes.
# Similar al str.split() pero el separador es un patrón RegEx.
#
# ¿Cuándo usarlo?
# → Parsear líneas de un archivo donde el separador no es siempre igual
#   (puede ser ":", ";", " - ", etc.)
# → Dividir CSVs con separadores variables.
# → Separar texto por cualquier signo de puntuación.
#
# maxsplit → cuántas veces dividir como máximo (0 = todas)

resultado = re.split(r":", texto)
print(resultado)    # ['Esta es la lección número 7', ' Lección llamada Expresiones Regulares']

# Con patrón más flexible — divide por ":" o ";"
texto2 = "nombre:Andrés;rol:backend;nivel:intermedio"
resultado2 = re.split(r"[;:]", texto2)
print(resultado2)   # ['nombre', 'Andrés', 'rol', 'backend', 'nivel', 'intermedio']

# maxsplit: solo divide las primeras N veces
resultado3 = re.split(r"[;:]", texto2, maxsplit=2)
print(resultado3)   # ['nombre', 'Andrés', 'rol:backend;nivel:intermedio']


# ------------------------------------------------------------
# 5. re.sub(pattern, repl, string, count=0, flags=0)
# ------------------------------------------------------------
# Reemplaza las coincidencias del patrón por otro texto.
# Retorna un NUEVO string (no modifica el original).
# Similar a str.replace() pero el patrón es RegEx.
#
# ¿Cuándo usarlo?
# → Sanitizar datos: quitar caracteres especiales, normalizar espacios.
# → Enmascarar información sensible (emails, teléfonos, tarjetas).
# → Reformatear fechas u otros patrones.
#
# count → cuántas sustituciones hacer como máximo (0 = todas)

resultado = re.sub(r"[lL]ección", "LECCIÓN", texto)
print(resultado)    # "Esta es la LECCIÓN número 7: LECCIÓN llamada Expresiones Regulares"

# Enmascarar emails en un texto:
log = "Error del usuario correo@empresa.com en el sistema"
resultado_log = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+", "***EMAIL***", log)
print(resultado_log)  # "Error del usuario ***EMAIL*** en el sistema"

# count: solo reemplaza la primera ocurrencia
resultado_uno = re.sub(r"[lL]ección", "LECCIÓN", texto, count=1)
print(resultado_uno)  # Solo reemplaza la primera


# ------------------------------------------------------------
# BONUS: re.compile(pattern, flags=0)
# ------------------------------------------------------------
# Compila un patrón en un objeto reutilizable.
# No es obligatorio, pero es buena práctica cuando usas el mismo
# patrón muchas veces (mejor rendimiento).
#
# El objeto compilado tiene los mismos métodos: .match(), .search(),
# .findall(), .split(), .sub()
#
# ¿Cuándo usarlo?
# → Cuando el mismo patrón se usa en múltiples validaciones dentro de
#   un loop, un endpoint de API, un procesador de archivos, etc.

patron_email = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$")

emails = ["usuario@gmail.com", "no-es-un-email", "otro@empresa.com.co"]
for e in emails:
    if patron_email.match(e):
        print(f"{e} → válido")
    else:
        print(f"{e} → inválido")


# ============================================================
# PATRONES — LO QUE VA DENTRO DE r"..."
# ============================================================

# ------------------------------------------------------------
# CARACTERES LITERALES y el punto
# ------------------------------------------------------------
# "abc"   → busca exactamente eso
# .       → cualquier carácter EXCEPTO salto de línea
# \.      → un punto literal (el \ escapa el significado especial)

print(re.findall(r".", "ab3"))    # ['a', 'b', '3']  ← cada carácter
print(re.findall(r"\.", "3.14"))  # ['.']             ← solo el punto


# ------------------------------------------------------------
# CLASES DE CARACTERES [ ]
# ------------------------------------------------------------
# [abc]    → exactamente uno de: a, b, o c
# [^abc]   → cualquier carácter EXCEPTO a, b, c
# [a-z]    → cualquier letra minúscula
# [A-Z]    → cualquier letra mayúscula
# [0-9]    → cualquier dígito
# [a-zA-Z] → cualquier letra
# [a-zA-Z0-9] → cualquier letra o dígito

print(re.findall(r"[lL]ección", texto))   # ['lección', 'Lección']
print(re.findall(r"[0-9]", texto))         # ['7', '6'] ← dígitos


# ------------------------------------------------------------
# CLASES ABREVIADAS (shortcuts)
# ------------------------------------------------------------
# \d   → dígito          [0-9]
# \D   → no dígito       [^0-9]
# \w   → palabra         [a-zA-Z0-9_]
# \W   → no palabra      [^a-zA-Z0-9_]
# \s   → espacio blanco  (espacio, tab, salto de línea)
# \S   → no espacio blanco

print(re.findall(r"\d", texto))   # ['7']
print(re.findall(r"\w", "hola_3 mundo"))  # letras, dígitos y _


# ------------------------------------------------------------
# CUANTIFICADORES — cuántas veces se repite algo
# ------------------------------------------------------------
# *     → 0 o más veces
# +     → 1 o más veces
# ?     → 0 o 1 vez (hace el elemento opcional)
# {n}   → exactamente n veces
# {n,m} → entre n y m veces
# {n,}  → n o más veces
#
# Por defecto son GREEDY (codiciosos): atrapan el máximo posible.
# Agrega ? al final para hacerlos LAZY (mínimo posible):
# *? +? ?? {n,m}?

print(re.findall(r"[l].*", texto))     # greedy: desde 'l' hasta el final
print(re.findall(r"[l].*?", texto))    # lazy: solo 'l' (mínimo posible)

# Ejemplo práctico — extraer contenido entre etiquetas HTML:
html = "<b>negrita</b> y <i>cursiva</i>"
print(re.findall(r"<.*>", html))    # greedy: ['<b>negrita</b> y <i>cursiva</i>']
print(re.findall(r"<.*?>", html))   # lazy:   ['<b>', '</b>', '<i>', '</i>']


# ------------------------------------------------------------
# ANCLAS — posición dentro del string
# ------------------------------------------------------------
# ^   → inicio del string (o de línea con re.MULTILINE)
# $   → fin del string (o de línea con re.MULTILINE)
# \b  → límite de palabra (entre \w y \W)
# \B  → NO límite de palabra

# ^ y $ son esenciales para VALIDAR strings completos:
patron = r"^\d{4}-\d{2}-\d{2}$"   # formato fecha YYYY-MM-DD
print(re.match(patron, "2024-05-10"))   # Match
print(re.match(patron, "2024-5-10"))    # None ← no tiene 2 dígitos en mes
print(re.match(patron, "2024-05-10 extra"))  # None ← tiene texto extra

# \b — útil para no matchear palabras dentro de otras:
texto3 = "Python es Pythonista y pythonico"
print(re.findall(r"\bPython\b", texto3, re.I))  # ['Python']  ← solo la palabra exacta


# ------------------------------------------------------------
# GRUPOS ( )
# ------------------------------------------------------------
# (abc)    → captura el grupo, lo puedes extraer con .group(N)
# (?:abc)  → agrupa SIN capturar (más eficiente si no necesitas extraer)
# (a|b)    → alternativa: a o b
#
# ¿Para qué sirven los grupos capturados?
# → Extraer partes específicas de un match (dominio de un email, año de fecha)
# → Reusar en el reemplazo con re.sub usando \1, \2...

email = "usuario@empresa.com"
patron = r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z-.]+)"
m = re.search(patron, email)
if m:
    print(m.group(0))   # match completo: "usuario@empresa.com"
    print(m.group(1))   # primer grupo:  "usuario"
    print(m.group(2))   # segundo grupo: "empresa"
    print(m.group(3))   # tercer grupo:  "com"

# Reusar grupos en re.sub:
fecha = "2024-05-10"
# Reformatear de YYYY-MM-DD a DD/MM/YYYY:
reformateada = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", fecha)
print(reformateada)   # "10/05/2024"

# Alternativa con |:
print(re.findall(r"lección|Expresiones", texto))  # ['lección', 'Lección', 'Expresiones']


# ------------------------------------------------------------
# FLAGS — modificadores del comportamiento
# ------------------------------------------------------------
# re.IGNORECASE  / re.I  → ignora mayúsculas/minúsculas
# re.MULTILINE   / re.M  → ^ y $ aplican a cada línea, no solo al string
# re.DOTALL      / re.S  → el . también coincide con \n
# re.VERBOSE     / re.X  → permite escribir el patrón en varias líneas con comentarios

# re.MULTILINE — útil al procesar archivos línea por línea:
log_multilinea = """ERROR: fallo en conexión
INFO: reintentando
ERROR: timeout"""
print(re.findall(r"^ERROR.*", log_multilinea, re.MULTILINE))
# ['ERROR: fallo en conexión', 'ERROR: timeout']

# re.VERBOSE — para patrones complejos, mejora la legibilidad:
patron_email_verbose = re.compile(r"""
    ^                       # inicio del string
    [a-zA-Z0-9_.+-]+        # parte local (antes del @)
    @                       # arroba
    [a-zA-Z0-9-]+           # dominio
    \.                      # punto
    [a-zA-Z-.]+             # TLD
    $                       # fin del string
""", re.VERBOSE)

print(patron_email_verbose.match("hola@mundo.com"))   # Match
print(patron_email_verbose.match("no-es-email"))       # None


# ============================================================
# CASOS DE USO REALES EN BACKEND
# ============================================================

# --- Validar email ---
def validar_email(email: str) -> bool:
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    return re.match(patron, email) is not None

print(validar_email("andrés@gmail.com"))       # True
print(validar_email("correo-invalido"))         # False

# --- Validar número de teléfono colombiano ---
def validar_telefono(tel: str) -> bool:
    # Acepta: 3001234567 o +573001234567
    patron = r"^(\+57)?[3][0-9]{9}$"
    return re.match(patron, tel) is not None

print(validar_telefono("3001234567"))      # True
print(validar_telefono("+573001234567"))   # True
print(validar_telefono("1234"))            # False

# --- Extraer todos los números de un texto ---
def extraer_numeros(texto: str) -> list:
    return re.findall(r"\d+", texto)

factura = "Subtotal: 150000, IVA: 28500, Total: 178500"
print(extraer_numeros(factura))   # ['150000', '28500', '178500']

# --- Sanitizar input: quitar caracteres no permitidos ---
def sanitizar(texto: str) -> str:
    # Solo letras, números y espacios
    return re.sub(r"[^a-zA-Z0-9 ]", "", texto)

print(sanitizar("Hola! ¿Cómo estás? #backend"))   # "Hola Cmo ests backend"

# --- Enmascarar datos sensibles en logs ---
def enmascarar_email(texto: str) -> str:
    patron = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+"
    return re.sub(patron, "***@***.***", texto)

log = "Usuario correo@empresa.com hizo login fallido"
print(enmascarar_email(log))   # "Usuario ***@***.*** hizo login fallido"

# --- Parsear líneas de log con grupos ---
def parsear_log(linea: str) -> dict | None:
    patron = r"^\[(\d{4}-\d{2}-\d{2})\] \[(\w+)\] (.+)$"
    m = re.match(patron, linea)
    if m:
        return {"fecha": m.group(1), "nivel": m.group(2), "mensaje": m.group(3)}
    return None

linea_log = "[2024-05-10] [ERROR] Conexión a base de datos fallida"
print(parsear_log(linea_log))
# {'fecha': '2024-05-10', 'nivel': 'ERROR', 'mensaje': 'Conexión a base de datos fallida'}


# ============================================================
# RESUMEN RÁPIDO
# ============================================================
# re.match()    → ¿empieza con este patrón?         → Match o None
# re.search()   → ¿existe este patrón en algún lado? → Match o None
# re.findall()  → dame TODAS las coincidencias       → lista de strings
# re.split()    → divide usando el patrón            → lista de partes
# re.sub()      → reemplaza coincidencias            → string nuevo
# re.compile()  → compila patrón para reutilizar     → Pattern object
#
# Match object útiles:
# .group()  → texto que coincidió
# .group(N) → grupo N capturado
# .span()   → (inicio, fin)
# .start()  → posición inicio
# .end()    → posición fin          