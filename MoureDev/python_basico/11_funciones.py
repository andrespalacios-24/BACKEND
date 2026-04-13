# ============================================================
# FUNCIONES EN PYTHON
# Basado en MoureDev — con explicación backend incluida
# ============================================================


# ============================================================
# ¿QUÉ ES UNA FUNCIÓN?
# ============================================================
# Una función es un bloque de código con nombre que puedes
# ejecutar ("llamar") cuantas veces quieras.
# En backend se usan para no repetir código:
# por ejemplo, una función que valida un token de usuario
# se llama cada vez que llega una petición, sin reescribirla.

# SINTAXIS:
# def nombre_funcion():
#     código

def my_function():
    print("Esto es una función")

# Para ejecutarla, la llamas por su nombre:
my_function()   # imprime: Esto es una función
my_function()   # la misma función, segunda vez
my_function()   # y una tercera — sin reescribir nada


# ============================================================
# FUNCIÓN CON PARÁMETROS (argumentos de entrada)
# ============================================================
# Los parámetros son variables que la función recibe al llamarla.
# Permiten que la misma función trabaje con datos diferentes.
#
# Uso backend: una función que recibe el nombre de usuario
# y lo registra en un log — siempre la misma función, datos distintos.
#
# El : int después de first_value es una "pista de tipo" (type hint).
# No es obligatorio en Python, pero es buena práctica en backend
# para que el código sea más claro y legible.

def sum_two_values(first_value: int, second_value): #en el caso de int, aplica al (type hint).
    print(first_value + second_value)               # y el type hint es sugerencia pero si no cumple todo se desarrolla igual

sum_two_values(5, 7)            # 12
sum_two_values(54754, 71231)    # suma grande
sum_two_values("5", "7")        # "57" — Python concatena strings
sum_two_values(1.4, 5.2)        # 6.6 — también funciona con decimales


# ============================================================
# FUNCIÓN CON RETORNO (return)
# ============================================================
# return hace que la función devuelva un valor que puedes
# guardar en una variable o usar en otra operación.
#
# Sin return: la función hace algo pero no devuelve nada útil.
# Con return: la función produce un resultado que puedes usar.
#
# Uso backend: una función que calcula el total de una orden
# devuelve el número para guardarlo en la base de datos.

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum   # devuelve el resultado al que llamó la función

# Sin return — el resultado se imprime dentro pero no se puede guardar:
my_result = sum_two_values(1.4, 5.2)
print(my_result)    # None — sum_two_values no retorna nada

# Con return — el resultado se guarda en my_result:
my_result = sum_two_values_with_return(10, 5)
print(my_result)    # 15


# ============================================================
# PARÁMETROS POR CLAVE (keyword arguments)
# ============================================================
# Normalmente los argumentos van en orden.
# Con parámetros por clave puedes pasarlos en cualquier orden
# usando nombre=valor.
#
# Uso backend: útil cuando una función tiene muchos parámetros
# y quieres que el código sea claro al leerlo.

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")   # Brais Moure
# aunque surname va primero, Python sabe cuál es cuál por el nombre


# ============================================================
# PARÁMETROS POR DEFECTO (default arguments)
# ============================================================
# Puedes darle un valor por defecto a un parámetro.
# Si no se pasa ese argumento al llamar la función, usa el valor por defecto.
# Si se pasa, usa el que se envía.
#
# Uso backend: por ejemplo, una función de paginación donde
# por defecto muestra 10 resultados, pero puedes pedir más.
#
# REGLA: los parámetros con valor por defecto siempre van AL FINAL.

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")              # usa el alias por defecto
print_name_with_default("Brais", "Moure", "MoureDev")  # reemplaza el alias por defecto


# ============================================================
# PARÁMETROS ARBITRARIOS (*args)
# ============================================================
# El * antes del parámetro permite enviar cualquier cantidad
# de argumentos. Python los agrupa en una tupla.
#
# Uso backend: por ejemplo, una función que recibe una lista
# variable de errores para registrarlos en un log — no sabes
# cuántos errores vendrán, pueden ser 1 o 100.
#
# type(texts) devuelve <class 'tuple'> — Python lo convierte en tupla

def print_upper_texts(*texts):
    print(type(texts))      # confirma que es una tupla
    for text in texts:
        print(text.upper()) # recorre cada texto y lo pone en mayúscula

print_upper_texts("Hola", "Python", "MoureDev")    # tres argumentos
print_upper_texts("Hola")                           # un solo argumento — también funciona


# ============================================================
# RESUMEN — ¿Cuándo usar cada tipo?
# ============================================================
# Sin parámetros    → cuando la función siempre hace lo mismo
# Con parámetros    → cuando necesita datos externos para trabajar
# Con return        → cuando necesitas usar el resultado afuera
# Por clave         → cuando hay muchos parámetros y quieres claridad
# Por defecto       → cuando un parámetro tiene un valor común
# *args             → cuando no sabes cuántos argumentos vendrán