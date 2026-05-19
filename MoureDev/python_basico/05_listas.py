### Listas ###

# Una lista es una colección de elementos en un orden específico
# Puede contener cualquier tipo de dato: strings, enteros, floats, booleanos, e incluso otras listas
# Se escribe entre corchetes [] y los elementos se separan con comas

# Ejemplos con contexto backend
usuarios = ["andres", "juan", "maria"]          # lista de strings
codigos_error = [400, 401, 403, 404, 500]       # lista de enteros
precios = [9.99, 19.99, 49.99]                  # lista de floats
mixta = ["andres", 28, True, 9.99]              # lista mixta

# len() cuenta elementos, no caracteres
print(len(usuarios))       # 3 → hay 3 usuarios en la lista
print(len(codigos_error))  # 5 → hay 5 códigos de error

# Acceder a elementos por posición — igual que en strings, empieza desde 0
print(usuarios[0])   # "andres" → primer usuario
print(usuarios[-1])  # "maria"  → último usuario

# Modificar un elemento
usuarios[0] = "andres_palacios"
print(usuarios)  # ["andres_palacios", "juan", "maria"]

# Agregar elementos
usuarios.append("carlos")     # agrega al final
print(usuarios)               # ["andres_palacios", "juan", "maria", "carlos"]

usuarios.insert(1, "pedro")   # inserta en posición específica
print(usuarios)               # ["andres_palacios", "pedro", "juan", "maria", "carlos"]

# Eliminar elementos
usuarios.remove("pedro")      # elimina por valor
print(usuarios)               # ["andres_palacios", "juan", "maria", "carlos"]

ultimo = usuarios.pop()       # elimina y guarda el último elemento
print(ultimo)                 # "carlos"
print(usuarios)               # ["andres_palacios", "juan", "maria"]

# Slicing — igual que en strings
print(usuarios[0:2])          # ["andres_palacios", "juan"] → sin incluir posición 2

# Ordenar y revertir
numeros = [3, 1, 4, 2, 5]
numeros.sort()                # ordena de menor a mayor
print(numeros)                # [1, 2, 3, 4, 5]

numeros.reverse()             # invierte el orden
print(numeros)                # [5, 4, 3, 2, 1]

# Concatenar listas
errores_cliente = [400, 401, 403]
errores_servidor = [500, 502, 503]
todos_los_errores = errores_cliente + errores_servidor
print(todos_los_errores)      # [400, 401, 403, 500, 502, 503]

# Verificar si un elemento está en la lista — operador "in"
print(404 in codigos_error)   # False → 404 no está en la lista
print(400 in codigos_error)   # True  → 400 sí está en la lista

# Método index() saber en que posicion esta lo que se busca
# Devuelve la posición de la primera aparición de un elemento en la lista
# Si el elemento no existe → ValueError
# Muy usado en backend para encontrar la posición de un dato específico

endpoints = ["/login", "/registro", "/perfil", "/admin", "/logout"]
print(endpoints.index("/perfil"))   # 2 → "/perfil" está en posición 2
print(endpoints.index("/login"))    # 0 → "/login" está en posición 0

codigos_error = [404, 500, 403, 401, 500]
print(codigos_error.index(500))     # 1 → primera aparición de 500 está en posición 1
# Si hubiera un 404 repetido, index() siempre devuelve la primera aparición

# Combinar index() con in para evitar el ValueError
codigo = 999
if codigo in codigos_error:
    print(codigos_error.index(codigo))
else:
    print("El código no existe en la lista")


# Copiar listas — método copy()
# copy() crea una copia independiente de la lista original
# Si modificas la copia, la original NO se ve afectada

usuarios = ["andres", "juan", "maria"]
usuarios_backup = usuarios.copy()

usuarios.clear()                # limpia la lista original
print(usuarios)                 # [] → lista original vacía
print(usuarios_backup)          # ["andres", "juan", "maria"] → copia intacta

# ¿Por qué no hacer esto? → usuarios_backup = usuarios
# Si asignas directamente, ambas variables apuntan a la misma lista
# Modificar una afecta a la otra — copy() evita ese problema


# =============================================================================
# LISTAS EN PYTHON — REFERENCIA COMPLETA
# Basado en: documentación oficial Python 3 (docs.python.org)
# =============================================================================


# -----------------------------------------------------------------------------
# ¿QUÉ ES UNA LISTA?
# -----------------------------------------------------------------------------

# Una lista es una colección ordenada y modificable de elementos.
# - Ordenada: los elementos tienen una posición fija (índice).
# - Modificable (mutable): se pueden agregar, eliminar o cambiar elementos.
# - Permite duplicados: el mismo valor puede aparecer más de una vez.
# - Permite mezcla de tipos: strings, enteros, floats, booleanos, otras listas.
#
# Se escribe entre corchetes [] y los elementos se separan con comas.

# Ejemplos con contexto backend:
usuarios       = ["andres", "juan", "maria"]
codigos_error  = [400, 401, 403, 404, 500]
precios        = [9.99, 19.99, 49.99]
mixta          = ["andres", 28, True, 9.99]    # mezcla de tipos, válido
lista_vacia    = []                            # lista sin elementos

# Lista de listas (estructura anidada):
tabla = [[1, "andres", "admin"], [2, "juan", "editor"], [3, "maria", "lector"]]
print(tabla[0])        # [1, "andres", "admin"] → primera fila
print(tabla[0][1])     # "andres" → columna 1 de la primera fila


# =============================================================================
# 1. ACCESO A ELEMENTOS
# =============================================================================

# Igual que en strings, los índices empiezan desde 0.
#
# "andres"  "juan"  "maria"
#    0         1       2      → índices positivos
#   -3        -2      -1      → índices negativos

usuarios = ["andres", "juan", "maria"]

print(usuarios[0])    # "andres" → primer elemento
print(usuarios[2])    # "maria"  → tercer elemento
print(usuarios[-1])   # "maria"  → último elemento
print(usuarios[-2])   # "juan"   → penúltimo elemento

# Slicing — igual que en strings: [inicio:fin:paso]
print(usuarios[0:2])   # ["andres", "juan"] → posiciones 0 y 1 (el 2 no se incluye)
print(usuarios[1:])    # ["juan", "maria"]  → desde posición 1 hasta el final
print(usuarios[::-1])  # ["maria", "juan", "andres"] → lista al revés


# =============================================================================
# 2. MODIFICAR ELEMENTOS
# =============================================================================

# Las listas son mutables: se pueden cambiar sus elementos directamente.
# Strings NO son mutables — las listas SÍ.

usuarios[0] = "andres_palacios"
print(usuarios)   # ["andres_palacios", "juan", "maria"]

# Modificar un rango completo con slicing:
numeros = [1, 2, 3, 4, 5]
numeros[1:3] = [20, 30]    # reemplaza posiciones 1 y 2
print(numeros)             # [1, 20, 30, 4, 5]


# =============================================================================
# 3. AGREGAR ELEMENTOS
# =============================================================================

usuarios = ["andres", "juan", "maria"]

# .append(elemento) — agrega un elemento al final
usuarios.append("carlos")
print(usuarios)   # ["andres", "juan", "maria", "carlos"]

# .insert(posicion, elemento) — inserta en una posición específica
# Los elementos existentes desde esa posición se desplazan hacia la derecha
usuarios.insert(1, "pedro")
print(usuarios)   # ["andres", "pedro", "juan", "maria", "carlos"]

# .extend(otra_lista) — agrega todos los elementos de otra lista al final
nuevos = ["lucia", "sofia"]
usuarios.extend(nuevos)
print(usuarios)   # ["andres", "pedro", "juan", "maria", "carlos", "lucia", "sofia"]

# Diferencia entre .append() y .extend():
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]

lista_a.append([4, 5])    # agrega la lista [4,5] como UN solo elemento
print(lista_a)            # [1, 2, 3, [4, 5]]

lista_b.extend([4, 5])    # agrega 4 y 5 como elementos individuales
print(lista_b)            # [1, 2, 3, 4, 5]

# Concatenación con + — crea una nueva lista (no modifica las originales)
errores_cliente  = [400, 401, 403]
errores_servidor = [500, 502, 503]
todos_los_errores = errores_cliente + errores_servidor
print(todos_los_errores)   # [400, 401, 403, 500, 502, 503]


# =============================================================================
# 4. ELIMINAR ELEMENTOS
# =============================================================================

usuarios = ["andres", "pedro", "juan", "maria", "carlos"]

# .remove(valor) — elimina la primera aparición del valor
# Si el valor no existe → ValueError
usuarios.remove("pedro")
print(usuarios)   # ["andres", "juan", "maria", "carlos"]

# .pop() — elimina y DEVUELVE el último elemento
# Útil cuando necesitas usar el valor eliminado
ultimo = usuarios.pop()
print(ultimo)     # "carlos"
print(usuarios)   # ["andres", "juan", "maria"]

# .pop(indice) — elimina y devuelve el elemento en esa posición
segundo = usuarios.pop(1)
print(segundo)    # "juan"
print(usuarios)   # ["andres", "maria"]

# del — elimina por índice o rango, sin devolver el valor
numeros = [10, 20, 30, 40, 50]
del numeros[2]          # elimina posición 2
print(numeros)          # [10, 20, 40, 50]

del numeros[1:3]        # elimina posiciones 1 y 2
print(numeros)          # [10, 50]

# .clear() — elimina TODOS los elementos, deja la lista vacía
usuarios = ["andres", "juan", "maria"]
usuarios.clear()
print(usuarios)   # []


# =============================================================================
# 5. BÚSQUEDA Y VERIFICACIÓN
# =============================================================================

codigos_error = [404, 500, 403, 401, 500]
endpoints = ["/login", "/registro", "/perfil", "/admin", "/logout"]

# Operador "in" — verifica si un elemento existe en la lista (True/False)
print(404 in codigos_error)     # True
print(999 in codigos_error)     # False
print(999 not in codigos_error) # True

# .index(valor) — devuelve la posición de la primera aparición
# Si el valor no existe → ValueError
print(endpoints.index("/perfil"))    # 2
print(codigos_error.index(500))      # 1 → primera aparición (no la segunda)

# Patrón seguro: siempre verificar con "in" antes de usar .index()
codigo = 999
if codigo in codigos_error:
    print(codigos_error.index(codigo))
else:
    print("El código no existe en la lista")

# .count(valor) — cuántas veces aparece un valor en la lista
print(codigos_error.count(500))   # 2 → aparece dos veces
print(codigos_error.count(404))   # 1

# len() — número de elementos en la lista
print(len(codigos_error))   # 5


# =============================================================================
# 6. ORDENAR Y REVERTIR
# =============================================================================

numeros = [3, 1, 4, 2, 5]

# .sort() — ordena la lista en su lugar (modifica la original), no devuelve nada
numeros.sort()
print(numeros)              # [1, 2, 3, 4, 5]

numeros.sort(reverse=True)  # ordena de mayor a menor
print(numeros)              # [5, 4, 3, 2, 1]

# sorted() — función integrada, devuelve una nueva lista sin modificar la original
original = [3, 1, 4, 2, 5]
nueva = sorted(original)
print(original)   # [3, 1, 4, 2, 5] → sin cambios
print(nueva)      # [1, 2, 3, 4, 5]

# .reverse() — invierte el orden de la lista en su lugar
numeros.reverse()
print(numeros)   # [1, 2, 3, 4, 5]

# Diferencia clave:
# .sort() y .reverse() → modifican la lista original, devuelven None
# sorted() → deja la original intacta, devuelve una nueva lista


# =============================================================================
# 7. COPIAR LISTAS
# =============================================================================

# ⚠️ Error común: asignación directa no crea una copia
usuarios = ["andres", "juan", "maria"]
referencia = usuarios          # ambas variables apuntan a la MISMA lista en memoria

referencia.append("nuevo")
print(usuarios)    # ["andres", "juan", "maria", "nuevo"] ← también cambió

# ✅ Correcto: usar .copy() para una copia independiente
usuarios = ["andres", "juan", "maria"]
backup = usuarios.copy()

usuarios.clear()
print(usuarios)    # []
print(backup)      # ["andres", "juan", "maria"] → intacta

# Otras formas válidas de copiar:
copia_slice = usuarios[:]     # slicing completo → también crea copia
import copy
copia_prof = copy.deepcopy(tabla)  # copia profunda para listas anidadas
# copy.deepcopy() es necesario cuando la lista contiene otras listas
# .copy() solo copia el primer nivel — las listas internas siguen compartidas


# =============================================================================
# 8. OTROS MÉTODOS ÚTILES
# =============================================================================

# min() y max() — valor mínimo y máximo (para listas de números o strings)
precios = [9.99, 49.99, 19.99, 4.99]
print(min(precios))   # 4.99
print(max(precios))   # 49.99
print(sum(precios))   # 84.96 → suma todos los elementos

# list() — convierte otros tipos a lista
letras = list("python")
print(letras)   # ['p', 'y', 't', 'h', 'o', 'n']

rango = list(range(1, 6))
print(rango)    # [1, 2, 3, 4, 5]


# =============================================================================
# 9. USO REAL EN BACKEND
# =============================================================================

# --- Gestión de sesiones activas ---
sesiones_activas = ["token_abc123", "token_xyz789", "token_def456"]

nuevo_token = "token_ghi000"
sesiones_activas.append(nuevo_token)
print(f"Sesiones activas: {len(sesiones_activas)}")   # 4

# Cerrar sesión: eliminar token específico
token_a_cerrar = "token_xyz789"
if token_a_cerrar in sesiones_activas:
    sesiones_activas.remove(token_a_cerrar)
print(sesiones_activas)   # ["token_abc123", "token_def456", "token_ghi000"]

# --- Validación de métodos HTTP permitidos ---
metodos_permitidos = ["GET", "POST", "PUT", "DELETE"]

metodo_recibido = "PATCH"
if metodo_recibido not in metodos_permitidos:
    print(f"Error 405: método {metodo_recibido} no permitido")
# Error 405: método PATCH no permitido

# --- Cola de tareas (job queue) ---
# En backend, las colas procesan tareas una por una en orden de llegada
cola_tareas = ["enviar_email", "generar_reporte", "actualizar_cache"]

cola_tareas.append("notificar_usuario")   # nueva tarea entra al final
tarea_actual = cola_tareas.pop(0)         # procesa la primera (FIFO)
print(f"Procesando: {tarea_actual}")      # "enviar_email"
print(f"Cola restante: {cola_tareas}")    # ["generar_reporte", "actualizar_cache", "notificar_usuario"]

# --- Paginación de resultados ---
productos = ["prod_1", "prod_2", "prod_3", "prod_4", "prod_5",
             "prod_6", "prod_7", "prod_8", "prod_9", "prod_10"]

pagina = 2
por_pagina = 3
inicio = (pagina - 1) * por_pagina    # (2-1)*3 = 3
fin = inicio + por_pagina             # 3+3 = 6
pagina_actual = productos[inicio:fin]
print(pagina_actual)   # ["prod_4", "prod_5", "prod_6"]

# --- Registro de errores (log acumulativo) ---
log_errores = []

def registrar_error(codigo, mensaje):
    log_errores.append({"codigo": codigo, "mensaje": mensaje})

registrar_error(404, "Recurso no encontrado")
registrar_error(500, "Error interno del servidor")

print(f"Total de errores registrados: {len(log_errores)}")   # 2
print(log_errores[0])   # {'codigo': 404, 'mensaje': 'Recurso no encontrado'}

# --- Filtrar resultados válidos ---
# Antes de procesar, se filtran los datos incorrectos
ids_recibidos = [1, -5, 3, 0, 7, -1, 10]
ids_validos = [id for id in ids_recibidos if id > 0]
print(ids_validos)   # [1, 3, 7, 10]
# Nota: esto es una list comprehension — se estudia en Python intermedio


# =============================================================================
# RESUMEN RÁPIDO — métodos más usados
# =============================================================================

# MÉTODO / FUNCIÓN          QUÉ HACE
# -----------------------   --------------------------------------------------
# .append(x)                Agrega x al final
# .insert(i, x)             Inserta x en la posición i
# .extend(lista)            Agrega todos los elementos de lista al final
# .remove(x)                Elimina la primera aparición de x (ValueError si no existe)
# .pop()                    Elimina y devuelve el último elemento
# .pop(i)                   Elimina y devuelve el elemento en posición i
# .clear()                  Elimina todos los elementos
# .index(x)                 Posición de la primera aparición de x
# .count(x)                 Cuántas veces aparece x
# .sort()                   Ordena en su lugar (modifica la original)
# .sort(reverse=True)       Ordena de mayor a menor
# .reverse()                Invierte el orden en su lugar
# .copy()                   Copia independiente de la lista
# sorted(lista)             Nueva lista ordenada sin modificar la original
# len(lista)                Número de elementos
# min(lista)                Valor mínimo
# max(lista)                Valor máximo
# sum(lista)                Suma de todos los elementos
# x in lista                True si x existe en la lista
# x not in lista            True si x NO existe en la lista
# lista[i:j]                Slicing: extrae desde i hasta j (sin incluir j)
# del lista[i]              Elimina el elemento en posición i


# =============================================================================
# FUENTES
# =============================================================================
# - Listas (documentación oficial): https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# - Tipos de secuencia:             https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# - copy vs deepcopy:               https://docs.python.org/3/library/copy.html