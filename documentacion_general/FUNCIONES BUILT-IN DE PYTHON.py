# ============================================================
# FUNCIONES BUILT-IN DE PYTHON - Las que funcionan en varios tipos
# ============================================================
# Estas funciones vienen incluidas en Python, no hay que importar nada.
# Lo interesante es que muchas funcionan con strings, listas, tuplas, sets y diccionarios.


# ── len() ────────────────────────────────────────────────────
# Retorna el número de elementos de una colección, o caracteres en un string.

print(len("Andrés"))               # 6       → caracteres del string
print(len([1, 2, 3, 4]))           # 4       → elementos de la lista
print(len((10, 20, 30)))           # 3       → elementos de la tupla
print(len({"a", "b", "c"}))       # 3       → elementos del set
print(len({"nombre": "Andrés"}))  # 1       → número de claves del diccionario


# ── type() ───────────────────────────────────────────────────
# Retorna el tipo de dato de cualquier variable.

print(type("hola"))          # <class 'str'>
print(type(28))              # <class 'int'>
print(type(1.77))            # <class 'float'>
print(type(True))            # <class 'bool'>
print(type([1, 2, 3]))       # <class 'list'>
print(type((1, 2, 3)))       # <class 'tuple'>
print(type({1, 2, 3}))       # <class 'set'>
print(type({"a": 1}))        # <class 'dict'>


# ── print() ──────────────────────────────────────────────────
# Imprime cualquier tipo de dato en consola.
# Ya la conoces bien, pero vale saber que acepta todo.

print("Andrés")              # string
print(28)                    # int
print([1, 2, 3])             # lista
print({"nombre": "Andrés"})  # diccionario


# ── input() ──────────────────────────────────────────────────
# Pide datos al usuario. Siempre retorna un STRING, sin importar lo que el usuario escriba.

nombre = input("¿Cómo te llamas? ")   # retorna str
edad   = input("¿Cuántos años tienes? ")  # retorna str — si necesitas número, convertir con int()


# ── int() / float() / str() / bool() ────────────────────────
# Convierten un valor de un tipo a otro (casting).

print(int("28"))         # str  → int     : 28
print(float("1.77"))     # str  → float   : 1.77
print(str(28))           # int  → str     : "28"
print(bool(0))           # int  → bool    : False  (0 es False, cualquier otro número es True)
print(bool(""))          # str  → bool    : False  (string vacío es False)
print(bool([]))          # list → bool    : False  (colección vacía es False)

# Muy útil con input() para convertir lo que escribe el usuario:
# edad = int(input("¿Cuántos años tienes? "))


# ── list() / tuple() / set() ─────────────────────────────────
# Convierten colecciones de un tipo a otro.

mi_tupla = (1, 2, 3)
mi_lista = [4, 5, 6]
mi_set   = {7, 8, 9}

print(list(mi_tupla))    # tupla  → lista  : [1, 2, 3]
print(list(mi_set))      # set    → lista  : [7, 8, 9] (orden no garantizado)
print(tuple(mi_lista))   # lista  → tupla  : (4, 5, 6)
print(set(mi_lista))     # lista  → set    : {4, 5, 6} (elimina duplicados)

# Con diccionarios, convierten solo las CLAVES:
datos = {"nombre": "Andrés", "edad": 28}
print(list(datos))       # ['nombre', 'edad']
print(tuple(datos))      # ('nombre', 'edad')
print(set(datos))        # {'nombre', 'edad'}


# ── max() / min() ────────────────────────────────────────────
# Retornan el valor máximo y mínimo de una colección.

print(max([3, 7, 1, 9, 2]))    # 9
print(min([3, 7, 1, 9, 2]))    # 1
print(max("Andrés"))            # 's' — en strings compara por orden alfabético (ASCII)
print(max((10, 50, 30)))        # 50  — también funciona con tuplas


# ── sum() ────────────────────────────────────────────────────
# Suma todos los elementos de una colección numérica.

print(sum([1, 2, 3, 4, 5]))    # 15
print(sum((10, 20, 30)))        # 60  — también funciona con tuplas


# ── sorted() ─────────────────────────────────────────────────
# Retorna una LISTA ordenada sin modificar la colección original.
# (diferente a .sort() que modifica la lista original)

print(sorted([3, 1, 4, 1, 5]))          # [1, 1, 3, 4, 5]
print(sorted("bcda"))                    # ['a', 'b', 'c', 'd'] — lista de caracteres
print(sorted({3, 1, 2}))                 # [1, 2, 3]
print(sorted({"b": 2, "a": 1}))         # ['a', 'b'] — ordena las CLAVES del diccionario
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1] — orden inverso


# ── reversed() ───────────────────────────────────────────────
# Retorna un iterador invertido — hay que convertirlo a lista para verlo.
# Solo funciona con secuencias (list, tuple, str) — NO con set ni dict.

print(list(reversed([1, 2, 3])))     # [3, 2, 1]
print(list(reversed((1, 2, 3))))     # [3, 2, 1]
print(list(reversed("Andrés")))      # ['s', 'é', 'r', 'd', 'n', 'A']


# ── enumerate() ──────────────────────────────────────────────
# Agrega un índice numérico a cada elemento de una colección.
# Muy útil cuando necesitas el índice y el valor al mismo tiempo.
# (Lo usarás más cuando veas bucles for)

ciudades = ["Bogotá", "Medellín", "Cali"]
print(list(enumerate(ciudades)))     # [(0, 'Bogotá'), (1, 'Medellín'), (2, 'Cali')]


# ── zip() ────────────────────────────────────────────────────
# Une dos listas en pares (como un cierre de cremallera).
# (También lo usarás más con bucles for)

nombres = ["Andrés", "Laura", "Carlos"]
edades  = [28, 25, 30]
print(list(zip(nombres, edades)))    # [('Andrés', 28), ('Laura', 25), ('Carlos', 30)]


# ── in ───────────────────────────────────────────────────────
# No es una función sino un operador, pero funciona con todos los tipos.
# Retorna True o False según si el elemento existe en la colección.

print("a" in "Andrés")                      # True  → busca en string
print(3 in [1, 2, 3, 4])                    # True  → busca en lista
print(10 in (10, 20, 30))                   # True  → busca en tupla
print("x" in {"x", "y", "z"})              # True  → busca en set
print("nombre" in {"nombre": "Andrés"})     # True  → busca en CLAVES del diccionario