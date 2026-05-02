### LAMBDAS EN PYTHON ###
# Documentación oficial: https://docs.python.org/3/reference/expressions.html#lambda

# ============================================================
# ¿QUÉ ES UNA LAMBDA?
# ============================================================
# Una lambda es una función anónima (sin nombre) definida en una sola línea.
# Se usa cuando necesitas una función simple, de un solo uso, sin querer
# definirla formalmente con def.

# SINTAXIS:
#   lambda parámetros: expresión
#
# - "lambda"      → palabra clave que la define
# - "parámetros"  → los argumentos que recibe (puede ser 0, 1 o varios)
# - "expresión"   → lo que calcula y retorna automáticamente (NO se escribe return)

# DIFERENCIA CLAVE con def:
# - def  → crea una función con nombre, varias líneas, puede tener lógica compleja
# - lambda → función sin nombre, una sola expresión, más concisa

# ============================================================
# COMPARACIÓN: def vs lambda
# ============================================================

# Con def:
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(sum_two_values(2, 4))  # 6

# La misma función con lambda (asignada a una variable):
sum_lambda = lambda first_value, second_value: first_value + second_value
print(sum_lambda(2, 4))  # 6

# Nota: PEP8 (guía de estilo oficial de Python) recomienda NO asignar
# lambdas a variables como arriba. Para eso es mejor usar def.
# Las lambdas brillan cuando se pasan directamente como argumento.

# ============================================================
# EJEMPLOS BÁSICOS
# ============================================================

# Sin parámetros:
saludo = lambda: "Hola backend"
print(saludo())  # Hola backend

# Un parámetro:
doblar = lambda x: x * 2
print(doblar(5))  # 10

# Dos parámetros:
multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))  # 5

# Con condición (ternario):
mayor_de_edad = lambda edad: "Mayor" if edad >= 18 else "Menor"
print(mayor_de_edad(20))  # Mayor
print(mayor_de_edad(15))  # Menor

# ============================================================
# LAMBDA DENTRO DE OTRA FUNCIÓN (Closure)
# ============================================================
# Aquí está la parte más importante del ejemplo de MoureDev.
# sum_three_values recibe un valor y RETORNA una lambda.
# Esa lambda "recuerda" el valor recibido (closure).

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

# Uso:
print(sum_three_values(5)(2, 4))  # 11  →  2 + 4 + 5

# ¿Por qué funciona sum_three_values(5)(2, 4)?
# sum_three_values(5)     → retorna una lambda que suma + 5
# (2, 4)                  → se la pasan a esa lambda
# Resultado: 2 + 4 + 5 = 11

# También se puede guardar el resultado intermedio:
sumar_con_10 = sum_three_values(10)
print(sumar_con_10(3, 7))   # 20  →  3 + 7 + 10
print(sumar_con_10(1, 1))   # 12  →  1 + 1 + 10

# ============================================================
# USO REAL EN BACKEND: ordenar datos
# ============================================================
# El uso más común de lambdas en backend es como argumento
# de funciones como sorted(), min(), max(), filter(), map().

# Ejemplo 1: ordenar lista de usuarios por edad
usuarios = [
    {"nombre": "Ana",    "edad": 30, "rol": "admin"},
    {"nombre": "Carlos", "edad": 25, "rol": "user"},
    {"nombre": "Laura",  "edad": 28, "rol": "user"},
]

ordenados_por_edad = sorted(usuarios, key=lambda u: u["edad"])
for u in ordenados_por_edad:
    print(u["nombre"], u["edad"])
# Carlos 25 / Laura 28 / Ana 30

# Ejemplo 2: ordenar productos por precio
productos = [
    {"nombre": "Laptop",  "precio": 2500000},
    {"nombre": "Mouse",   "precio": 45000},
    {"nombre": "Monitor", "precio": 800000},
]

mas_barato_primero = sorted(productos, key=lambda p: p["precio"])
for p in mas_barato_primero:
    print(p["nombre"], p["precio"])

# Ejemplo 3: filtrar solo usuarios activos
clientes = [
    {"nombre": "Pedro",   "activo": True},
    {"nombre": "Lucia",   "activo": False},
    {"nombre": "Marcos",  "activo": True},
]

activos = list(filter(lambda c: c["activo"], clientes))
print(activos)  # Solo Pedro y Marcos

# Ejemplo 4: aplicar descuento a precios con map()
precios = [100000, 200000, 350000]
con_descuento = list(map(lambda p: p * 0.9, precios))
print(con_descuento)  # [90000.0, 180000.0, 315000.0]

# ============================================================
# RESUMEN RÁPIDO
# ============================================================
# lambda parámetros: expresión
#
# ✅ Úsala cuando:
#    - Necesitas una función corta de un solo uso
#    - La vas a pasar como argumento (sorted, filter, map)
#    - Quieres retornar una función desde otra función
#
# ❌ No la uses cuando:
#    - La lógica tiene más de una expresión
#    - Necesitas documentar o reutilizar la función
#    - Quieres asignarla a una variable (mejor usa def)