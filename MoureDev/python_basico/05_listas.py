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