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