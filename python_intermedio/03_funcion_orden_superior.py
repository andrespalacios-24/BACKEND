# ============================================================
#        FUNCIONES DE ORDEN SUPERIOR EN PYTHON
#        Referencia completa con ejemplos backend
# ============================================================
# Documentación oficial: https://docs.python.org/3/howto/functional.html


# ============================================================
# 1. ¿QUÉ ES UNA FUNCIÓN DE ORDEN SUPERIOR?
# ============================================================

# Una función de orden superior es aquella que cumple al menos una de estas:
#   - Recibe una o más funciones como argumento
#   - Devuelve una función como resultado
#
# Esto es posible porque en Python las funciones son "ciudadanos de primera clase"
# (first-class citizens): se pueden asignar a variables, pasar como argumentos,
# y retornar desde otras funciones, igual que cualquier otro objeto.


# ============================================================
# 2. FUNCIÓN QUE RECIBE OTRA FUNCIÓN COMO ARGUMENTO
# ============================================================

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add(first_value, second_value, f_sum):
    # f_sum es una función que se pasa como argumento
    return f_sum(first_value + second_value)

print(sum_two_values_and_add(5, 2, sum_one))   # 8  → (5+2)+1
print(sum_two_values_and_add(5, 2, sum_five))  # 12 → (5+2)+5

# Caso de uso backend: aplicar diferentes estrategias de descuento
# sin cambiar la lógica principal del carrito de compras.

def apply_discount(price, discount_fn):
    return discount_fn(price)

vip_discount    = lambda price: price * 0.80   # 20% descuento
normal_discount = lambda price: price * 0.90   # 10% descuento

print(apply_discount(100, vip_discount))    # 80.0
print(apply_discount(100, normal_discount)) # 90.0


# ============================================================
# 3. CLOSURES — FUNCIÓN QUE RETORNA OTRA FUNCIÓN
# ============================================================

# Un closure es una función interna que "recuerda" el entorno
# donde fue creada, incluso cuando se llama fuera de ese entorno.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value  # "recuerda" original_value
    return add  # retorna la función, no la ejecuta

add_closure = sum_ten(1)
print(add_closure(5))       # 16 → 5 + 10 + 1
print((sum_ten(5))(1))      # 16 → 1 + 10 + 5

# Caso de uso backend: fábricas de validadores reutilizables.
# Cada validador "recuerda" su límite sin repetir lógica.

def make_min_length_validator(min_length):
    def validate(value):
        return len(value) >= min_length
    return validate

validate_username = make_min_length_validator(4)
validate_password = make_min_length_validator(8)

print(validate_username("ab"))       # False
print(validate_username("andres"))   # True
print(validate_password("1234"))     # False
print(validate_password("segura123"))# True


# ============================================================
# 4. FUNCIONES INTEGRADAS DE ORDEN SUPERIOR
# ============================================================

numbers = [2, 5, 10, 21, 3, 30]


# ------------------------------------------------------------
# 4.1 MAP — Transformar cada elemento de un iterable
# ------------------------------------------------------------
# Sintaxis: map(funcion, iterable)
# Aplica la función a CADA elemento y devuelve un iterador.
# Siempre se convierte a list() para ver el resultado.
# Cuándo usarlo: cuando quieres transformar todos los elementos.

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))              # Con función nombrada
print(list(map(lambda number: number * 2, numbers))) # Con lambda (más común)

# Caso de uso backend: formatear una lista de respuestas de API
users = [
    {"name": "andres", "role": "admin"},
    {"name": "maria",  "role": "user"},
]
formatted = list(map(lambda u: f"{u['name'].capitalize()} ({u['role']})", users))
print(formatted)  # ['Andres (admin)', 'Maria (user)']


# ------------------------------------------------------------
# 4.2 FILTER — Filtrar elementos de un iterable
# ------------------------------------------------------------
# Sintaxis: filter(funcion, iterable)
# Mantiene solo los elementos donde la función devuelve True.
# Cuándo usarlo: cuando quieres un subconjunto de los datos.

def filter_greater_than_ten(number):
    return number > 10  # basta con retornar la condición directamente

print(list(filter(filter_greater_than_ten, numbers)))        # Con función nombrada
print(list(filter(lambda number: number > 10, numbers)))     # Con lambda

# Caso de uso backend: filtrar usuarios activos de una base de datos
users_db = [
    {"name": "andres", "active": True},
    {"name": "maria",  "active": False},
    {"name": "carlos", "active": True},
]
active_users = list(filter(lambda u: u["active"], users_db))
print(active_users)  # [{'name': 'andres', ...}, {'name': 'carlos', ...}]


# ------------------------------------------------------------
# 4.3 REDUCE — Reducir un iterable a un único valor
# ------------------------------------------------------------
# Sintaxis: reduce(funcion, iterable)
# Requiere: from functools import reduce
# Aplica la función acumulativamente: f(f(f(a,b),c),d)...
# Cuándo usarlo: cuando quieres combinar todos los elementos en uno.

from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))              # 71 → suma total
print(reduce(lambda a, b: a + b, numbers))          # 71 → con lambda

# Caso de uso backend: calcular el total de una orden con múltiples items
order_items = [
    {"product": "teclado", "price": 80000},
    {"product": "mouse",   "price": 35000},
    {"product": "monitor", "price": 450000},
]
total = reduce(lambda acc, item: acc + item["price"], order_items, 0)
print(f"Total orden: ${total:,}")  # Total orden: $565,000


# ============================================================
# 5. DIFERENCIAS CLAVE ENTRE MAP, FILTER Y REDUCE
# ============================================================

# | Función | ¿Qué recibe?        | ¿Qué devuelve?          | Uso típico              |
# |---------|---------------------|-------------------------|-------------------------|
# | map     | función + iterable  | iterador (misma longitud)| Transformar elementos   |
# | filter  | función + iterable  | iterador (menor longitud)| Seleccionar elementos   |
# | reduce  | función + iterable  | un único valor           | Acumular/combinar todo  |


# ============================================================
# 6. COMBINANDO TODO — Ejemplo backend real
# ============================================================

# Escenario: procesar una lista de transacciones bancarias.
# - Solo nos interesan las transacciones aprobadas
# - Queremos aplicar una comisión del 2% a cada una
# - Necesitamos el total final

transactions = [
    {"id": 1, "amount": 100000, "status": "approved"},
    {"id": 2, "amount":  50000, "status": "rejected"},
    {"id": 3, "amount": 200000, "status": "approved"},
    {"id": 4, "amount":  75000, "status": "rejected"},
    {"id": 5, "amount": 300000, "status": "approved"},
]

approved    = list(filter(lambda t: t["status"] == "approved", transactions))
with_fee    = list(map(lambda t: t["amount"] * 1.02, approved))
grand_total = reduce(lambda a, b: a + b, with_fee)

print(f"Transacciones aprobadas: {len(approved)}")
print(f"Montos con comisión: {with_fee}")
print(f"Total procesado: ${grand_total:,.0f}")