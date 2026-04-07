# =============================================================================
# EJERCICIOS DE REPASO INTEGRADOR - Python Básico
# Temas: strings, listas, sets, diccionarios
# Contexto: backend development
# =============================================================================
# Instrucciones:
#   - Intenta resolver cada ejercicio antes de buscar ayuda.
#   - Al terminar: git add . / git commit -m "ejercicios: repaso integrador" / git push
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1 - Inventario de endpoints
# -----------------------------------------------------------------------------
# Tienes una lista de endpoints registrados en una API. Algunos están duplicados.
# 1. Elimina los duplicados (usa set).
# 2. Guarda los únicos en una lista ordenada alfabéticamente.
# 3. Imprime cuántos endpoints únicos hay y cuáles son.

endpoints = [
    "/users",
    "/products",
    "/users",
    "/orders",
    "/products",
    "/auth/login",
    "/auth/login",
    "/health",
]

# Tu código aquí:
lista= set(endpoints)
lista_unicos= list(lista) #se puede acortar un paso con sorted()
lista_unicos.sort() #se acorta asi: lista_unicos = sorted(set(endpoints)) asi ordena y no toca comvertir a lista
cantidad= len(lista_unicos)
print(f"son: {cantidad} endpoint unicos, conformados por: {lista_unicos}")

# -----------------------------------------------------------------------------
# EJERCICIO 2 - Registro de usuarios
# -----------------------------------------------------------------------------
# Simula el registro de un usuario en un sistema backend.
# 1. Pide al usuario: nombre, email, edad (con input()).
# 2. Guarda los datos en un diccionario.
# 3. Agrega al diccionario: "activo": True y "rol": "user".
# 4. Imprime el resumen con un f-string así:
#    "Usuario registrado: Juan | Email: juan@mail.com | Edad: 25 | Rol: user"

# Tu código aquí:
datos_usuario= {}
nombre= input("Ingrese Primer Nombre: ")
correo= input("Ingrese Direccion Email: ")
edad= int(input("Ingrese Edad: "))
datos_usuario["primer nombre"]= nombre
datos_usuario["direccion email"]= correo
datos_usuario["edad"]= edad
datos_usuario.update({"activo":True, "rol": "user"}) #poner las llaves y los boleanos:true van sin comillas
print(f"usuario registrado: {nombre} | Email {correo} | edad: {edad} | Rol:{datos_usuario["rol"]} ") 


# -----------------------------------------------------------------------------
# EJERCICIO 3 - Análisis de logs
# -----------------------------------------------------------------------------
# Tienes una lista de logs de un servidor. Cada log es un string con este formato:
# "2024-01-15 ERROR conexión rechazada"
# 1. Recorre la lista y separa cada log en partes (usa .split()).
# 2. Guarda cada log como diccionario con claves: "fecha", "nivel", "mensaje".
# 3. Guarda todos los diccionarios en una lista llamada `logs_parseados`.
# 4. Imprime cada log parseado.
# PISTA: "ERROR conexión rechazada".split(" ", 1) → ["ERROR", "conexión rechazada"]

logs_raw = [
    "2024-01-15 ERROR conexión rechazada",
    "2024-01-15 INFO servidor iniciado",
    "2024-01-16 WARNING memoria al 80%",
    "2024-01-16 ERROR timeout en base de datos",
    "2024-01-17 INFO backup completado",
]

# Tu código aquí:


# -----------------------------------------------------------------------------
# EJERCICIO 4 - Resumen de base de datos (integrador)
# -----------------------------------------------------------------------------
# Tienes una lista de productos de una tienda online.
# Cada producto es un diccionario con: nombre, precio, categoría, stock.
# 
# 1. Imprime todos los nombres de productos disponibles (stock > 0).
# 2. Obtén un set con todas las categorías únicas y muéstralas.
# 3. Encuentra el producto más caro (precio más alto) e imprímelo completo.
# 4. Calcula el precio promedio de todos los productos.
# 5. Genera un string con los nombres de productos separados por " | " (usa .join()).
#    Ejemplo: "Laptop | Mouse | Teclado"

productos = [
    {"nombre": "Laptop", "precio": 2500000, "categoria": "electronica", "stock": 5},
    {"nombre": "Mouse", "precio": 80000, "categoria": "electronica", "stock": 0},
    {"nombre": "Escritorio", "precio": 950000, "categoria": "muebles", "stock": 3},
    {"nombre": "Teclado", "precio": 150000, "categoria": "electronica", "stock": 8},
    {"nombre": "Silla", "precio": 1200000, "categoria": "muebles", "stock": 2},
    {"nombre": "Monitor", "precio": 1800000, "categoria": "electronica", "stock": 0},
    {"nombre": "Webcam", "precio": 320000, "categoria": "electronica", "stock": 6},
]

# Tu código aquí: