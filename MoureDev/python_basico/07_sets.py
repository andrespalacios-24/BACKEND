### Sets ###

# Un set es una colección desordenada y sin elementos repetidos
# Se escribe entre llaves {}
# A diferencia de listas y tuplas, los sets NO tienen un orden fijo
# Cada vez que los imprimes pueden aparecer en un orden diferente

# Listas y tuplas → ordenadas, mantienen el orden de inserción
lista = [1, 2, 3, 4]       # siempre imprime [1, 2, 3, 4]
tupla = (1, 2, 3, 4)       # siempre imprime (1, 2, 3, 4)

# Sets → desordenados, no garantizan orden
mi_set = {1, 2, 3, 4}      # puede imprimir {1, 3, 2, 4} o cualquier orden

# Los sets eliminan automáticamente los duplicados
errores = {404, 500, 404, 403, 500, 200}
print(errores)  # {200, 403, 404, 500} → los repetidos desaparecen

# Definición
mi_set = {1, 2, 3, 4, 5}
mi_set_vacio = set()        # set vacío — {} no funciona, eso crea un diccionario
print(type(mi_set))         # <class 'set'>
print(len(mi_set))          # 5

# Agregar y eliminar elementos
mi_set.add(6)               # agrega un elemento
print(mi_set)               # {1, 2, 3, 4, 5, 6}

mi_set.add(3)               # intenta agregar un duplicado
print(mi_set)               # {1, 2, 3, 4, 5, 6} → no cambia nada, ignora el duplicado

mi_set.remove(6)            # elimina un elemento — si no existe → KeyError
mi_set.discard(99)          # elimina un elemento — si no existe NO da error

# Operaciones típicas de sets — muy usadas en backend
roles_usuario = {"admin", "editor", "lector"}
roles_requeridos = {"admin", "superusuario"}

# Unión → todos los elementos de ambos sets sin repetir
print(roles_usuario | roles_requeridos)     # {"admin", "editor", "lector", "superusuario"}

# Intersección → solo los elementos que están en ambos
print(roles_usuario & roles_requeridos)     # {"admin"}

# Diferencia → elementos que están en uno pero no en el otro
print(roles_usuario - roles_requeridos)     # {"editor", "lector"}

# ¿Cuándo usar cada tipo?
# Lista  → cuando el orden importa y los datos pueden repetirse (historial de requests)
# Tupla  → cuando los datos no deben cambiar nunca (configuración, credenciales)
# Set    → cuando necesitas unicidad y no importa el orden (roles, permisos, emails únicos)
# Buscar elementos en un set — operador "in"
# Funciona igual que en listas, tuplas y strings
# Responde True o False

roles_usuario = {"admin", "editor", "lector"}

print("admin" in roles_usuario)      # True  → "admin" está en el set
print("superusuario" in roles_usuario) # False → no está en el set
print("editor" not in roles_usuario) # False → "editor" sí está, entonces "not in" es False

# Caso real: verificar permisos antes de ejecutar una acción
permiso_requerido = "admin"
if permiso_requerido in roles_usuario:
    print("Acceso permitido")
else:
    print("Acceso denegado")
   
   
    # Eliminar contenido de un set — clear() vs del

roles = {"admin", "editor", "lector"}

# clear() → vacía el set pero la variable sigue existiendo
roles.clear()
print(roles)        # set() → set vacío, la variable sigue disponible

# del → elimina completamente la variable de la memoria
roles = {"admin", "editor", "lector"}
del roles
# print(roles)      # NameError: name 'roles' is not defined → la variable ya no existe

# ¿Cuándo usar cada uno?
# clear() → cuando quieres reutilizar la variable más adelante (limpiar permisos de una sesión)
# del    → cuando ya no necesitas la variable para nada (liberar memoria)

# Set → Lista
# Útil cuando necesitas acceder por posición (los sets no tienen índices)
roles = {"admin", "editor", "lector"}
roles_lista = list(roles)
print(roles_lista[0])   # ahora sí puedes acceder por posición

# union() → igual que | pero escrito como método
roles_usuario = {"admin", "editor"}
roles_extra = {"superusuario", "moderador"}
print(roles_usuario.union(roles_extra))         # todos sin repetir

# difference() → igual que - pero escrito como método
print(roles_usuario.difference(roles_extra))    # los que están en uno pero no en el otro

# Resumen: dos formas de escribir lo mismo
# roles_usuario | roles_extra   ==   roles_usuario.union(roles_extra)
# roles_usuario - roles_extra   ==   roles_usuario.difference(roles_extra)

#en caso de que toque ordenar un set
my_set = {"manzana", "naranja", "platano"}
set_list = sorted(list(my_set))  # ordena alfabéticamente
print(set_list[0])               # siempre "manzana"
#si se requiere ordenar un set list toca usar sorted porque si no con cada print darta un orden diferente 
# =============================================================================
# SETS EN PYTHON — REFERENCIA COMPLETA
# Basado en: documentación oficial Python 3 (docs.python.org)
# =============================================================================


# -----------------------------------------------------------------------------
# ¿QUÉ ES UN SET?
# -----------------------------------------------------------------------------

# Un set es una colección desordenada, mutable y sin elementos repetidos.
# - Desordenado: los elementos NO tienen una posición fija. No hay índices.
#   El orden en que se imprimen puede variar entre ejecuciones.
# - Mutable: se pueden agregar y eliminar elementos.
# - Sin duplicados: si intentas agregar un valor que ya existe, lo ignora.
#
# Se escribe entre llaves {} con elementos separados por comas.
# Su razón de existir es garantizar unicidad y hacer operaciones de conjuntos
# (unión, intersección, diferencia) de forma eficiente.

mi_set = {1, 2, 3, 4, 5}
print(type(mi_set))    # <class 'set'>
print(len(mi_set))     # 5

# Los duplicados se eliminan automáticamente al crear el set
errores = {404, 500, 404, 403, 500, 200}
print(errores)   # {200, 403, 404, 500} → repetidos desaparecen, orden no garantizado

# --- Set vacío ---
# ⚠️ {} NO crea un set vacío — crea un diccionario vacío
set_vacio  = set()    # ← correcto
dict_vacio = {}       # ← esto es un dict, no un set
print(type(set_vacio))    # <class 'set'>
print(type(dict_vacio))   # <class 'dict'>


# =============================================================================
# 1. AGREGAR Y ELIMINAR ELEMENTOS
# =============================================================================

roles = {"admin", "editor", "lector"}

# .add(elemento) — agrega un elemento
# Si el elemento ya existe, lo ignora sin error
roles.add("moderador")
print(roles)     # {"admin", "editor", "lector", "moderador"} (orden no garantizado)

roles.add("editor")   # ya existe → no cambia nada, no genera error
print(roles)          # sin cambios

# .remove(elemento) — elimina un elemento
# Si el elemento no existe → KeyError
roles.remove("moderador")

# .discard(elemento) — elimina un elemento
# Si el elemento no existe → no hace nada, no genera error
roles.discard("superusuario")   # no existe, pero no explota

# Patrón seguro con .remove(): verificar antes con "in"
elemento = "admin"
if elemento in roles:
    roles.remove(elemento)

# .pop() — elimina y devuelve un elemento aleatorio (desordenado → no hay "primero")
roles = {"admin", "editor", "lector"}
eliminado = roles.pop()
print(f"Se eliminó: {eliminado}")    # imprime alguno de los tres, no se sabe cuál

# .clear() — vacía el set, la variable sigue existiendo
roles.clear()
print(roles)    # set()

# del — elimina la variable completamente de memoria
roles = {"admin", "editor", "lector"}
del roles
# print(roles)  # NameError: la variable ya no existe

# ¿Cuándo usar cada uno?
# .clear() → cuando vas a reutilizar la variable (limpiar permisos de sesión al cerrar)
# del      → cuando ya no necesitas la variable para nada (liberar memoria)


# =============================================================================
# 2. BÚSQUEDA — operador "in"
# =============================================================================

# Buscar en un set con "in" es más eficiente que en una lista
# Las listas recorren elemento por elemento (O(n))
# Los sets usan una tabla hash — la búsqueda es casi instantánea (O(1))

roles_usuario = {"admin", "editor", "lector"}

print("admin" in roles_usuario)          # True
print("superusuario" in roles_usuario)   # False
print("editor" not in roles_usuario)     # False → "editor" sí está

# Patrón real: verificar permiso antes de ejecutar acción
permiso_requerido = "admin"
if permiso_requerido in roles_usuario:
    print("Acceso permitido")
else:
    print("Acceso denegado")


# =============================================================================
# 3. OPERACIONES DE CONJUNTOS
# =============================================================================

# Los sets implementan las operaciones matemáticas de la teoría de conjuntos.
# Cada operación tiene dos formas equivalentes: operador y método.

roles_usuario    = {"admin", "editor", "lector"}
roles_requeridos = {"admin", "superusuario"}

# --- Unión | → todos los elementos de ambos sets, sin repetir ---
print(roles_usuario | roles_requeridos)
print(roles_usuario.union(roles_requeridos))
# {"admin", "editor", "lector", "superusuario"}

# --- Intersección & → solo los elementos presentes en AMBOS ---
print(roles_usuario & roles_requeridos)
print(roles_usuario.intersection(roles_requeridos))
# {"admin"}

# --- Diferencia - → elementos que están en el primero pero NO en el segundo ---
print(roles_usuario - roles_requeridos)
print(roles_usuario.difference(roles_requeridos))
# {"editor", "lector"}

# --- Diferencia simétrica ^ → elementos que están en uno u otro, pero NO en ambos ---
print(roles_usuario ^ roles_requeridos)
print(roles_usuario.symmetric_difference(roles_requeridos))
# {"editor", "lector", "superusuario"}

# --- Subconjunto y superconjunto ---
permisos_basicos = {"lector"}
print(permisos_basicos.issubset(roles_usuario))     # True → permisos_basicos ⊆ roles_usuario
print(roles_usuario.issuperset(permisos_basicos))   # True → roles_usuario ⊇ permisos_basicos
print(roles_usuario.isdisjoint({"superusuario"}))   # True → no comparten ningún elemento

# Resumen operadores vs métodos:
# set_a | set_b    ==  set_a.union(set_b)
# set_a & set_b    ==  set_a.intersection(set_b)
# set_a - set_b    ==  set_a.difference(set_b)
# set_a ^ set_b    ==  set_a.symmetric_difference(set_b)


# =============================================================================
# 4. CONVERSIÓN ENTRE TIPOS
# =============================================================================

# Set → Lista (cuando necesitas índices u orden)
roles = {"admin", "editor", "lector"}
roles_lista = list(roles)
print(roles_lista[0])    # ahora sí puedes acceder por posición (orden no predecible)

# Set → Lista ordenada (cuando necesitas orden consistente)
frutas = {"manzana", "naranja", "platano"}
frutas_ordenadas = sorted(list(frutas))   # sorted() devuelve una lista
print(frutas_ordenadas)                   # ['manzana', 'naranja', 'platano'] — siempre igual
print(frutas_ordenadas[0])               # 'manzana' — ahora sí predecible

# ⚠️ sorted() sobre un set directamente también funciona:
print(sorted(frutas))    # mismo resultado, más conciso

# Lista → Set (para eliminar duplicados de una lista)
emails_con_duplicados = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com"]
emails_unicos = list(set(emails_con_duplicados))
print(emails_unicos)    # ['a@mail.com', 'b@mail.com', 'c@mail.com'] (orden no garantizado)

# Tupla → Set
codigos = (404, 500, 404, 200, 500)
codigos_unicos = set(codigos)
print(codigos_unicos)    # {200, 404, 500}

# frozenset — versión inmutable del set (no se puede modificar)
# Útil cuando necesitas usar un set como clave de diccionario
permisos_fijos = frozenset({"leer", "escribir"})
# permisos_fijos.add("eliminar")  # AttributeError — no se puede modificar


# =============================================================================
# 5. CUÁNDO USAR CADA COLECCIÓN
# =============================================================================

# LISTA  → cuando el orden importa y los datos pueden repetirse
#           historial de requests, resultados paginados, logs de errores

# TUPLA  → cuando los datos no deben cambiar nunca
#           configuración, credenciales, constantes, coordenadas

# SET    → cuando necesitas unicidad y las operaciones de conjunto
#           roles y permisos, emails únicos, IPs vistas, etiquetas

# DICT   → cuando necesitas asociar una clave con un valor
#           usuario → rol, endpoint → handler, id → registro


# =============================================================================
# 6. USO REAL EN BACKEND
# =============================================================================

# --- Control de acceso por roles ---
roles_usuario    = {"editor", "lector"}
roles_requeridos = {"admin", "editor"}

# ¿El usuario tiene AL MENOS UNO de los roles requeridos?
tiene_acceso = bool(roles_usuario & roles_requeridos)
print(tiene_acceso)    # True → comparten "editor"

# ¿Le faltan roles para acceso completo?
roles_faltantes = roles_requeridos - roles_usuario
print(f"Roles faltantes: {roles_faltantes}")   # {"admin"}

# --- Eliminar duplicados de emails recibidos ---
# Un formulario puede enviar el mismo email varias veces
emails_recibidos = ["a@c.com", "b@c.com", "a@c.com", "d@c.com", "b@c.com"]
emails_a_notificar = list(set(emails_recibidos))
print(f"Enviando a {len(emails_a_notificar)} destinatarios únicos")   # 3

# --- Tracking de IPs que ya hicieron una acción (rate limiting) ---
ips_que_votaron = set()

def registrar_voto(ip):
    if ip in ips_que_votaron:
        return (429, "Ya votaste desde esta IP")
    ips_que_votaron.add(ip)
    return (200, "Voto registrado")

print(registrar_voto("192.168.1.1"))   # (200, 'Voto registrado')
print(registrar_voto("192.168.1.1"))   # (429, 'Ya votaste desde esta IP')
print(registrar_voto("10.0.0.5"))      # (200, 'Voto registrado')

# --- Validar que los campos requeridos estén presentes en una solicitud ---
campos_requeridos = {"nombre", "email", "password"}
campos_recibidos  = {"nombre", "email"}

campos_faltantes = campos_requeridos - campos_recibidos
if campos_faltantes:
    print(f"Error 400: faltan campos: {campos_faltantes}")   # {"password"}

# --- Encontrar permisos comunes entre dos usuarios ---
permisos_user1 = {"leer", "escribir", "eliminar", "exportar"}
permisos_user2 = {"leer", "escribir", "publicar"}

permisos_compartidos = permisos_user1 & permisos_user2
print(f"Ambos pueden: {permisos_compartidos}")   # {"leer", "escribir"}

permisos_exclusivos_u1 = permisos_user1 - permisos_user2
print(f"Solo user1 puede: {permisos_exclusivos_u1}")   # {"eliminar", "exportar"}


# =============================================================================
# RESUMEN RÁPIDO
# =============================================================================

# OPERACIÓN                  OPERADOR    MÉTODO
# -------------------------  ---------   ----------------------------------
# Unión                      a | b       a.union(b)
# Intersección               a & b       a.intersection(b)
# Diferencia                 a - b       a.difference(b)
# Diferencia simétrica       a ^ b       a.symmetric_difference(b)
# ¿Es subconjunto?           a <= b      a.issubset(b)
# ¿Es superconjunto?         a >= b      a.issuperset(b)
# ¿No comparten elementos?   —           a.isdisjoint(b)

# MÉTODO              QUÉ HACE
# ---------------     ---------------------------------------------------
# .add(x)             Agrega x (ignora si ya existe)
# .remove(x)          Elimina x (KeyError si no existe)
# .discard(x)         Elimina x (silencioso si no existe)
# .pop()              Elimina y devuelve un elemento aleatorio
# .clear()            Vacía el set
# .copy()             Copia independiente
# len(set)            Número de elementos
# x in set            True si x está en el set (búsqueda O(1))
# sorted(set)         Lista ordenada sin modificar el set


# =============================================================================
# FUENTES
# =============================================================================
# - Sets (documentación oficial): https://docs.python.org/3/tutorial/datastructures.html#sets
# - Tipo set:                     https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
# - frozenset:                    https://docs.python.org/3/library/stdtypes.html#frozenset