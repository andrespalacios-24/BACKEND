# =============================================================================
#  BUCLES EN PYTHON  —  while · for · break · continue · else
#  Basado en MoureDev + contexto de backend
# =============================================================================


# -----------------------------------------------------------------------------
# 1. ¿QUÉ ES UN BUCLE?
# -----------------------------------------------------------------------------
# Un bucle repite un bloque de código mientras se cumpla una condición,
# o hasta recorrer todos los elementos de una colección.
#
# Analogía: un cajero escanea productos uno por uno y para cuando ya no hay
# más en la cinta → eso es un for.
# Si espera hasta que el cliente ingrese el PIN correcto → eso es un while.


# -----------------------------------------------------------------------------
# 2. BUCLE while
# -----------------------------------------------------------------------------
# Se repite MIENTRAS una condición sea True.
# ⚠️  Siempre actualiza la condición dentro del bucle o será infinito.
#
# Sintaxis:
#   while condicion:
#       # código
#       # actualizar condición  ← obligatorio

my_condition = 0

while my_condition < 10:
    print(my_condition)   # imprime: 0, 2, 4, 6, 8
    my_condition += 2     # actualiza la condición
else:
    # El else se ejecuta cuando la condición se vuelve False de forma natural.
    # NO se ejecuta si el bucle terminó con break.
    # Es opcional — en la práctica se usa poco.
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


# ¿Cuándo usar while en backend?
#   - Reintentos: intentar conectar a una base de datos hasta que funcione.
#   - Validación: pedir un dato hasta que sea correcto.
#   - Polling: verificar el estado de un proceso hasta que termine.


# -----------------------------------------------------------------------------
# 3. break — salir del bucle antes de tiempo
# -----------------------------------------------------------------------------
# Detiene el bucle inmediatamente, sin importar si la condición sigue siendo True.
# Cuando hay break, el else del bucle NO se ejecuta.

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break          # sale del bucle aquí
    print(my_condition)

print("La ejecución continúa")


# -----------------------------------------------------------------------------
# 4. BUCLE for
# -----------------------------------------------------------------------------
# Recorre uno a uno los elementos de un iterable
# (lista, tupla, set, diccionario, string, range).
# No necesitas controlar un contador manual — Python lo hace por ti.
#
# Sintaxis:
#   for elemento in iterable:
#       # código

# — for sobre una LISTA —
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)   # imprime cada número

# — for sobre una TUPLA —
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

# — for sobre un SET —
my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)   # el orden NO está garantizado en sets

# — for sobre un DICCIONARIO —
# Por defecto itera sobre las CLAVES (keys), no los valores.
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)         # imprime: Nombre, Apellido, Edad, 1
    if element == "Edad":
        break              # sale al llegar a "Edad"
else:
    # No se ejecuta porque el bucle terminó con break
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

# Para obtener clave Y valor al mismo tiempo (lo verás más adelante):
#   for clave, valor in my_dict.items():
#       print(clave, "->", valor)


# -----------------------------------------------------------------------------
# 5. continue — saltar una iteración
# -----------------------------------------------------------------------------
# No sale del bucle completo.
# Solo salta el resto del código de ESA vuelta y pasa a la siguiente.

for element in my_dict:
    print(element)
    if element == "Edad":
        continue       # salta el print de abajo cuando element == "Edad"
    print("Se ejecuta")
else:
    # Sí se ejecuta porque el bucle terminó sin break
    print("El bucle for para diccionario ha finalizado")


# -----------------------------------------------------------------------------
# 6. break vs continue — resumen rápido
# -----------------------------------------------------------------------------
#
#   break    → sale del bucle por completo     | el else NO se ejecuta
#   continue → salta solo esa vuelta           | el else SÍ se ejecuta
#
# Regla: si necesitas parar todo → break. Si necesitas ignorar un caso → continue.


# -----------------------------------------------------------------------------
# 7. ¿while o for? — ¿cuándo usar cada uno?
# -----------------------------------------------------------------------------
#
#   for   → cuando tienes una colección que recorrer
#           (lista de productos, resultados de base de datos, etc.)
#
#   while → cuando dependes de una condición externa que puede cambiar
#           (respuesta del usuario, estado de red, límite de tiempo)
#
# Regla práctica en backend:
#   ¿Tienes lista/diccionario/set?          → for
#   ¿Dependes de algo que puede cambiar?    → while


# -----------------------------------------------------------------------------
# 8. EJEMPLO INTEGRADOR — contexto de backend
# -----------------------------------------------------------------------------

productos = [
    {"nombre": "Laptop",  "precio": 2500000, "stock": 5},
    {"nombre": "Mouse",   "precio": 80000,   "stock": 0},
    {"nombre": "Teclado", "precio": 150000,  "stock": 8},
]

# for: recorrer cada producto y mostrar solo los disponibles
for producto in productos:
    if producto["stock"] > 0:
        print(producto["nombre"])

# while: simular reintentos de conexión
intentos = 0
while intentos < 3:
    print(f"Intento {intentos + 1} de conexión...")
    intentos += 1


# -----------------------------------------------------------------------------
# 9. ERRORES COMUNES
# -----------------------------------------------------------------------------

# ❌ Olvidar actualizar la condición en while → bucle infinito
#    while my_condition < 10:
#        print(my_condition)
#        # ← falta my_condition += algo

# ❌ Confundir break y continue
#    break    = para todo el bucle
#    continue = solo salta esa vuelta

# ❌ El for sobre un dict devuelve CLAVES, no valores
#    for x in my_dict:
#        print(x)           # imprime "Nombre", "Edad"... no "Brais", 35...
#    Para el valor: print(my_dict[x])
#    Para ambos:    use .items() → for clave, valor in my_dict.items()

# =============================================================================
#  Próximo tema: Funciones
# =============================================================================