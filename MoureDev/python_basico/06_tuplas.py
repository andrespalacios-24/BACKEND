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