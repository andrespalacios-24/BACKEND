### Tuplas ###

# Una tupla es una colección ordenada e inmutable
# Se escribe con paréntesis () en lugar de corchetes []
# Una vez creada no se puede modificar — no tiene append, remove, insert, etc.

# Definición
mi_tupla = (1, 2, 3)
mi_otra_tupla = (35, 1.77, "Andres", True)

print(type(mi_tupla))       # <class 'tuple'>
print(len(mi_tupla))        # 3

# Acceso — igual que listas, por posición
print(mi_otra_tupla[0])     # 35
print(mi_otra_tupla[-1])    # True

# Slicing — funciona igual que en listas y strings
print(mi_tupla[0:2])        # (1, 2)

# Métodos disponibles — solo dos porque es inmutable
codigos_http = (200, 301, 400, 401, 403, 404, 500)
print(codigos_http.count(404))    # 1 → cuántas veces aparece
print(codigos_http.index(500))    # 6 → posición del elemento

# Desempaquetado — igual que en strings y listas
estado, mensaje = (200, "OK")
print(estado)     # 200
print(mensaje)    # "OK"

# Casos de uso en backend — datos que no deben cambiar nunca
configuracion_db = ("localhost", 5432, "mi_base_de_datos")
coordenadas_servidor = (4.7110, -74.0721)   # Bogotá
metodos_http_permitidos = ("GET", "POST", "PUT", "DELETE")

# Intentar modificar una tupla genera TypeError
# codigos_http[0] = 999  # TypeError: 'tuple' object does not support item assignment

# Conversión entre Tuplas y Listas
# En Python puedes convertir entre ambos tipos usando list() y tuple()
# Útil cuando necesitas modificar datos de una tupla — la conviertes a lista,
# la modificas y la vuelves a convertir a tupla

# Tupla → Lista
# Cuando necesitas modificar datos que estaban protegidos como tupla
configuracion = ("localhost", 5432, "mi_base_de_datos")
configuracion_lista = list(configuracion)
print(configuracion_lista)        # ["localhost", 5432, "mi_base_de_datos"]
print(type(configuracion_lista))  # <class 'list'>

configuracion_lista[1] = 3306     # ahora sí puedes modificar
print(configuracion_lista)        # ["localhost", 3306, "mi_base_de_datos"]

# Lista → Tupla
# Cuando quieres proteger datos de una lista para que no se modifiquen
usuarios_activos = ["andres", "juan", "maria"]
usuarios_activos_tupla = tuple(usuarios_activos)
print(usuarios_activos_tupla)        # ("andres", "juan", "maria")
print(type(usuarios_activos_tupla))  # <class 'tuple'>

# Flujo completo: tupla → lista → modificar → tupla
metodos_http = ("GET", "POST", "DELETE")
temp = list(metodos_http)       # convertir a lista para modificar
temp.append("PUT")              # agregar nuevo método
metodos_http = tuple(temp)      # volver a proteger como tupla
print(metodos_http)             # ("GET", "POST", "DELETE", "PUT")


# =============================================================================
# TUPLAS EN PYTHON — REFERENCIA COMPLETA
# Basado en: documentación oficial Python 3 (docs.python.org)
# =============================================================================


# -----------------------------------------------------------------------------
# ¿QUÉ ES UNA TUPLA?
# -----------------------------------------------------------------------------

# Una tupla es una colección ordenada e inmutable de elementos.
# - Ordenada: los elementos tienen una posición fija (índice), igual que las listas.
# - Inmutable: una vez creada NO se puede modificar — no se pueden agregar,
#   eliminar ni cambiar elementos.
# - Permite duplicados y mezcla de tipos.
#
# Se escribe entre paréntesis () con elementos separados por comas.
# La inmutabilidad es su característica más importante y la razón de su existencia:
# comunica explícitamente que esos datos no deben cambiar.

mi_tupla        = (1, 2, 3)
coordenadas     = (4.7110, -74.0721)          # Bogotá — no tiene sentido modificar esto
config_db       = ("localhost", 5432, "mi_db")
metodos_http    = ("GET", "POST", "PUT", "DELETE")
codigos_http    = (200, 301, 400, 401, 403, 404, 500)
mixta           = (35, 1.77, "Andres", True)  # mezcla de tipos, válido

print(type(mi_tupla))   # <class 'tuple'>
print(len(mi_tupla))    # 3

# --- Tupla de un solo elemento ---
# Requiere una coma al final — sin ella Python lo interpreta como un paréntesis matemático
un_elemento     = (42,)          # ← coma obligatoria
no_es_tupla     = (42)           # esto es solo el entero 42 entre paréntesis
print(type(un_elemento))         # <class 'tuple'>
print(type(no_es_tupla))         # <class 'int'>

# --- Tupla sin paréntesis (empaquetado implícito) ---
# Python permite crear tuplas sin paréntesis separando valores con comas
sin_parentesis = 1, 2, 3
print(type(sin_parentesis))      # <class 'tuple'>
print(sin_parentesis)            # (1, 2, 3)


# =============================================================================
# 1. ACCESO, SLICING Y DESEMPAQUETADO
# =============================================================================

# --- Acceso por índice — igual que listas y strings ---
print(codigos_http[0])    # 200  → primer elemento
print(codigos_http[-1])   # 500  → último elemento

# --- Slicing [inicio:fin:paso] ---
print(codigos_http[0:3])      # (200, 301, 400)
print(codigos_http[::-1])     # (500, 404, 403, 401, 400, 301, 200) → al revés

# --- Desempaquetado ---
# Asigna cada elemento a una variable en orden
# El número de variables debe coincidir exactamente con el número de elementos
estado, mensaje = (200, "OK")
print(estado)     # 200
print(mensaje)    # "OK"

host, puerto, nombre_db = config_db
print(host)       # "localhost"
print(puerto)     # 5432

# Desempaquetado con * (extended unpacking) — captura el resto como lista
primero, *resto = (1, 2, 3, 4, 5)
print(primero)    # 1
print(resto)      # [2, 3, 4, 5]  ← resto es una lista, no una tupla

*inicio, ultimo = (1, 2, 3, 4, 5)
print(inicio)     # [1, 2, 3, 4]
print(ultimo)     # 5


# =============================================================================
# 2. MÉTODOS DISPONIBLES
# =============================================================================

# Las tuplas solo tienen dos métodos porque son inmutables.
# Todos los métodos que modifican datos (append, remove, sort, etc.) no existen.

codigos_http = (200, 301, 400, 401, 403, 404, 500, 404)

# .count(valor) — cuántas veces aparece un valor
print(codigos_http.count(404))    # 2 → aparece dos veces

# .index(valor) — posición de la primera aparición
# Si el valor no existe → ValueError
print(codigos_http.index(500))    # 6
print(codigos_http.index(404))    # 5 → primera aparición, no la segunda

# Patrón seguro antes de usar .index():
codigo = 999
if codigo in codigos_http:
    print(codigos_http.index(codigo))
else:
    print(f"{codigo} no está en la tupla")

# Operadores y funciones que sí funcionan en tuplas:
print(404 in codigos_http)        # True
print(999 not in codigos_http)    # True
print(len(codigos_http))          # 8
print(min(codigos_http))          # 200
print(max(codigos_http))          # 500


# =============================================================================
# 3. INMUTABILIDAD — qué significa en la práctica
# =============================================================================

# Intentar modificar una tupla genera TypeError:
# codigos_http[0] = 999    # TypeError: 'tuple' object does not support item assignment
# codigos_http.append(201) # AttributeError: 'tuple' has no attribute 'append'

# La inmutabilidad tiene ventajas concretas:
# 1. Las tuplas son más rápidas que las listas (menos overhead en memoria).
# 2. Pueden usarse como claves en diccionarios (las listas no pueden).
# 3. Comunican intención: "estos datos no deben cambiar".

# Ejemplo — tupla como clave de diccionario (imposible con lista):
cache = {}
cache[(4.7110, -74.0721)] = "Bogotá"     # coordenadas como clave
cache[(6.2442, -75.5812)] = "Medellín"
print(cache[(4.7110, -74.0721)])          # "Bogotá"

# ⚠️ Inmutabilidad superficial:
# Si una tupla contiene una lista, la lista SÍ se puede modificar
# (la tupla sigue apuntando al mismo objeto lista en memoria)
tupla_con_lista = ([1, 2, 3], "texto")
tupla_con_lista[0].append(4)    # válido — modifica la lista interna
print(tupla_con_lista)          # ([1, 2, 3, 4], "texto")
# tupla_con_lista[0] = [9, 9]   # esto sí genera TypeError


# =============================================================================
# 4. CONVERSIÓN ENTRE TUPLAS Y LISTAS
# =============================================================================

# Cuando necesitas modificar datos de una tupla:
# tupla → list() → modificar → tuple()

# Tupla → Lista
config = ("localhost", 5432, "mi_db")
config_lista = list(config)
config_lista[1] = 3306           # cambiar el puerto
config = tuple(config_lista)     # volver a proteger
print(config)                    # ("localhost", 3306, "mi_db")

# Lista → Tupla (para proteger datos que ya no deben cambiar)
usuarios_activos = ["andres", "juan", "maria"]
usuarios_fijos = tuple(usuarios_activos)
print(usuarios_fijos)            # ("andres", "juan", "maria")

# Otras conversiones útiles:
print(list(range(5)))            # [0, 1, 2, 3, 4]
print(tuple(range(5)))           # (0, 1, 2, 3, 4)
print(tuple("python"))           # ('p', 'y', 't', 'h', 'o', 'n')


# =============================================================================
# 5. TUPLAS VS LISTAS — cuándo usar cada una
# =============================================================================

# Usa LISTA cuando:
# - La colección va a cambiar (agregar usuarios, eliminar registros, etc.)
# - Necesitas ordenar, filtrar o modificar elementos
# - El orden de los elementos puede variar

# Usa TUPLA cuando:
# - Los datos son fijos por naturaleza (coordenadas, configuración, constantes)
# - Quieres proteger datos de modificaciones accidentales
# - Necesitas usarlos como clave de diccionario
# - Quieres comunicar que esos datos no deben cambiar (intención en el código)

# Regla práctica:
# Si te preguntas "¿puede cambiar esto durante la vida del programa?"
# → Sí puede cambiar → lista
# → No debe cambiar → tupla


# =============================================================================
# 6. USO REAL EN BACKEND
# =============================================================================

# --- Configuración de servidor (datos que nunca deben cambiar en ejecución) ---
DB_CONFIG    = ("localhost", 5432, "produccion_db")
ALLOWED_HOSTS = ("miapp.com", "api.miapp.com", "www.miapp.com")

host_solicitado = "api.miapp.com"
if host_solicitado in ALLOWED_HOSTS:
    print(f"Host {host_solicitado} autorizado")

# --- Respuestas HTTP estándar como tuplas ---
# Convención común en frameworks Python: devolver (codigo, mensaje)
def verificar_token(token):
    tokens_validos = ("abc123", "xyz789", "def456")
    if token in tokens_validos:
        return (200, "Autorizado")
    return (401, "Token inválido")

codigo, mensaje = verificar_token("abc123")
print(f"HTTP {codigo}: {mensaje}")    # HTTP 200: Autorizado

# --- Coordenadas y datos geográficos ---
CIUDADES = {
    "bogota":   (4.7110, -74.0721),
    "medellin": (6.2442, -75.5812),
    "buga":     (3.9003, -76.2984),
}
lat, lon = CIUDADES["buga"]
print(f"Buga → Lat: {lat}, Lon: {lon}")

# --- Rutas de endpoints fijas ---
# Los endpoints de una API no cambian durante la ejecución
ENDPOINTS_PUBLICOS  = ("/login", "/registro", "/health")
ENDPOINTS_PRIVADOS  = ("/usuarios", "/productos", "/admin")

ruta = "/admin"
if ruta in ENDPOINTS_PRIVADOS:
    print("Requiere autenticación")

# --- Desempaquetado en procesamiento de datos ---
# Al leer registros de una base de datos, los resultados suelen llegar como tuplas
registros_db = [
    (1, "andres", "admin",  True),
    (2, "juan",   "editor", True),
    (3, "maria",  "lector", False),
]

for id_usuario, nombre, rol, activo in registros_db:
    if activo:
        print(f"[{id_usuario}] {nombre} ({rol}) — activo")
# [1] andres (admin) — activo
# [2] juan (editor) — activo


# =============================================================================
# RESUMEN RÁPIDO — tuplas vs listas
# =============================================================================

# CARACTERÍSTICA          TUPLA              LISTA
# ---------------------   ----------------   ----------------
# Sintaxis                (1, 2, 3)          [1, 2, 3]
# Mutable                 No                 Sí
# Métodos de modificación Ninguno            append, insert, remove, pop, sort...
# Métodos disponibles     .count() .index()  todos los anteriores + .count() .index()
# Velocidad               Más rápida         Más lenta
# Clave de diccionario    Sí ✅              No ❌
# Uso típico              Datos fijos        Datos que cambian
# Desempaquetado          Sí                 Sí


# =============================================================================
# FUENTES
# =============================================================================
# - Tuplas (documentación oficial): https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# - Tipos de secuencia:             https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# - Extended unpacking (PEP 3132):  https://peps.python.org/pep-3132/