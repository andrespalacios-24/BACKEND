# ============================================================
# DICCIONARIOS EN PYTHON - Referencia completa
# ============================================================

# Un diccionario guarda pares de clave: valor
# Se usa cuando los datos tienen una "etiqueta" (no solo un índice numérico)
# Las claves pueden ser strings, números u otros tipos inmutables
# Los valores pueden ser cualquier tipo, incluso otro diccionario o un set


# ── CREAR ────────────────────────────────────────────────────

my_dict  = dict()   # Diccionario vacío usando dict()
my_dict2 = {}       # Diccionario vacío usando llaves — forma más común

# Con datos desde el inicio:
usuario = {
    "nombre": "Andrés",
    "ciudad": "Bogotá",
    "edad": 20,
    "activo": True,
    "lenguajes": {"Python", "Swift", "Kotlin"},  # El valor puede ser un set
    1: 1.77                                       # La clave también puede ser un número
}

print(type(my_dict))    # <class 'dict'>
print(type(my_dict2))   # <class 'dict'>
print(len(usuario))     # Número de claves del diccionario


# ── LEER ─────────────────────────────────────────────────────

print(usuario["nombre"])                        # "Andrés" — acceso directo por clave
print(usuario[1])                              # 1.77     — las claves numéricas también funcionan
print(usuario.get("ciudad"))                   # "Bogotá" — más seguro: no da error si la clave no existe
print(usuario.get("email", "Sin email"))       # Valor por defecto si no existe la clave


# ── BUSCAR ───────────────────────────────────────────────────

print("nombre" in usuario)           # True  — busca en las CLAVES (comportamiento por defecto)
print("Andrés" in usuario.values())  # True  — busca en los VALORES


# ── AGREGAR / MODIFICAR ──────────────────────────────────────

usuario["email"] = "andres@gmail.com"   # Agrega si la clave no existe
usuario["edad"]  = 21                   # Modifica si la clave ya existe
# No existe .add() en diccionarios — se asigna directamente con la clave

usuario.update({"ciudad": "Medellín", "telefono": "123"})  # Agrega/actualiza varios a la vez


# ── ELIMINAR ─────────────────────────────────────────────────

del usuario["activo"]                   # Elimina la clave directamente
eliminado = usuario.pop("email")        # Elimina Y retorna el valor eliminado
print(eliminado)                        # "andres@gmail.com"

usuario.clear()                         # Vacía el diccionario por completo


# ── RECORRER ─────────────────────────────────────────────────

usuario = {"nombre": "Andrés", "ciudad": "Bogotá", "edad": 21}

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")


# ── MÉTODOS DE CONSULTA ──────────────────────────────────────

print(usuario.items())    # Pares (clave, valor) — tipo dict_items
print(usuario.keys())     # Todas las claves      — tipo dict_keys
print(usuario.values())   # Todos los valores     — tipo dict_values

print(type(usuario.values()))   # <class 'dict_values'>


# ── CONVERSIÓN DE TIPOS ──────────────────────────────────────

print(tuple(usuario))           # Convierte las CLAVES a tupla
print(set(usuario))             # Convierte las CLAVES a set
print(list(usuario.values()))   # Convierte los VALORES a lista


# ── dict.fromkeys() ──────────────────────────────────────────
# Crea un diccionario nuevo a partir de una lista de claves
# Todos los valores serán None por defecto (o el valor que indiques)

mi_lista = ["nombre", 1, "piso"]

nuevo = dict.fromkeys(mi_lista)               # {"nombre": None, 1: None, "piso": None}
print(nuevo)

nuevo = dict.fromkeys(("nombre", 1, "piso"))  # Mismo resultado pero pasando una tupla directa
print(nuevo)

nuevo = dict.fromkeys(usuario)                # Toma las CLAVES de otro diccionario
print(nuevo)

nuevo = dict.fromkeys(usuario, "MoureDev")   # Todas las claves con el mismo valor
print(nuevo)

# Obtener valores únicos de un diccionario (eliminando duplicados):
print(list(dict.fromkeys(list(nuevo.values())).keys()))


# ── COPIA ────────────────────────────────────────────────────

usuario_copia = usuario.copy()   # Copia independiente (como en listas)


# ── DICCIONARIOS ANIDADOS ────────────────────────────────────
# Un valor puede ser otro diccionario — muy común en backend y APIs

usuarios = {
    "user_01": {"nombre": "Andrés", "ciudad": "Bogotá"},
    "user_02": {"nombre": "Laura",  "ciudad": "Medellín"}
}

print(usuarios["user_01"]["nombre"])    # "Andrés"


# ── EN BACKEND ───────────────────────────────────────────────
# Los diccionarios son la base de casi todo en backend:
#
# → Las APIs reciben y responden datos en JSON — que en Python es un diccionario
# → Las filas de una base de datos se representan como diccionarios
# → Las configuraciones de un proyecto (settings, variables de entorno) son diccionarios
#
# Ejemplo: respuesta típica de una API REST
respuesta_api = {
    "status": 200,
    "data": {
        "id": 1,
        "nombre": "Andrés",
        "email": "andres@gmail.com"
    },
    "error": None
}

# ============================================================
# ACCEDER A UNA LISTA DENTRO DE UN DICCIONARIO
# ============================================================

# Cuando un valor de un diccionario es una lista, se accede en dos pasos:
# Paso 1 → entrar al diccionario con la clave
# Paso 2 → operar sobre la lista que está adentro

datos = {
    "nombre": "Andrés",
    "ciudad": "Bogotá",
    "historial": ["buga", "tulua", "popayan"]   # el valor es una lista
}


# ── VER LA LISTA COMPLETA ────────────────────────────────────

print(datos["historial"])           # ['buga', 'tulua', 'popayan']


# ── ACCEDER A UN ELEMENTO ESPECÍFICO ─────────────────────────
# Se encadena el índice de la lista al acceso del diccionario

print(datos["historial"][0])        # 'buga'     → primer elemento
print(datos["historial"][1])        # 'tulua'    → segundo elemento
print(datos["historial"][-1])       # 'popayan'  → último elemento


# ── SABER CUÁNTOS ELEMENTOS TIENE ───────────────────────────

print(len(datos["historial"]))      # 3


# ── BUSCAR SI UN ELEMENTO EXISTE ────────────────────────────

print("buga" in datos["historial"])      # True
print("bogota" in datos["historial"])    # False


# ── USAR MÉTODOS DE LISTA ────────────────────────────────────
# Como el valor ES una lista, puedes usar todos los métodos que ya conoces

datos["historial"].append("cali")        # agrega un elemento
datos["historial"].remove("tulua")       # elimina un elemento
print(datos["historial"])                # ['buga', 'popayan', 'cali']


# ── EN BACKEND ───────────────────────────────────────────────
# Esto es muy común en APIs — los datos llegan como diccionarios
# con listas adentro, por ejemplo:

respuesta_api = {
    "usuario": "Andrés",
    "permisos": ["leer", "escribir", "eliminar"],
    "dispositivos": ["PC Bogotá", "PC Buga"]
}

print(respuesta_api["permisos"][0])      # "leer"   → primer permiso
print(len(respuesta_api["dispositivos"])) # 2       → cuántos dispositivos tiene