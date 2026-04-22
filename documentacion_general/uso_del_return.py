# ============================================================
#  REFERENCIA: EL USO DE return EN PYTHON
#  Para qué sirve, cuándo usarlo y cómo evitar errores comunes
# ============================================================


# ------------------------------------------------------------
# 1. ¿QUÉ ES return?
# ------------------------------------------------------------

# return es la instrucción que usa una función para DEVOLVER un valor
# al código que la llamó. Sin return, la función hace su trabajo
# pero no entrega nada útil al exterior.

# Sin return → la función no devuelve nada útil
def sumar_sin_return(a, b):
    resultado = a + b
    # el resultado existe dentro de la función, pero se pierde

sumar_sin_return(3, 5)         # no pasa nada visible
print(sumar_sin_return(3, 5))  # imprime: None

# Con return → la función entrega el valor
def sumar_con_return(a, b):
    return a + b

resultado = sumar_con_return(3, 5)
print(resultado)  # imprime: 8


# ------------------------------------------------------------
# 2. REGLA CLAVE: return vs print
# ------------------------------------------------------------

# print()  → muestra algo en pantalla. No produce ningún valor.
#            Siempre retorna None.
# return   → entrega un valor al código que llamó la función.
#            Ese valor se puede guardar, imprimir, o usar más adelante.

# ❌ ERROR COMÚN: return print(...)
def mal_ejemplo(a, b):
    return print(a + b)  # print() retorna None → la función retorna None

print(mal_ejemplo(3, 5))
# Salida:
# 8       ← esto lo imprime el print() interno
# None    ← esto lo imprime el print() externo porque la función retornó None

# ✅ CORRECTO: separar el cálculo del print
def buen_ejemplo(a, b):
    return a + b  # la función solo calcula y retorna

resultado = buen_ejemplo(3, 5)
print(resultado)  # quien llama decide qué hacer con el valor


# ------------------------------------------------------------
# 3. LA FUNCIÓN DEBE TENER return EN TODOS SUS CAMINOS
# ------------------------------------------------------------

# Si una función puede terminar por distintos caminos (try/except, if/else),
# cada camino debe tener su propio return. Si algún camino no retorna nada,
# Python retorna None automáticamente → eso causa el "None" inesperado.

# ❌ Solo un camino tiene return
lista_cadenas = ["1", "2", "3", "c", "5"]

def conversor_mal(cadenas):
    try:
        lista_enteros = [int(x) for x in cadenas]
        return lista_enteros        # camino exitoso → retorna la lista
    except ValueError:
        print("error de conversión") # camino de error → no retorna nada → None

print(conversor_mal(lista_cadenas))
# Salida:
# error de conversión
# None    ← porque el except no tenía return

# ✅ Ambos caminos tienen return
def conversor_bien(cadenas):
    try:
        lista_enteros = [int(x) for x in cadenas]
        return lista_enteros                        # camino exitoso
    except ValueError:
        return "uno de los elementos no es un número"  # camino de error

print(conversor_bien(lista_cadenas))
# Salida: uno de los elementos no es un número


# ------------------------------------------------------------
# 4. RESPONSABILIDADES SEPARADAS
# ------------------------------------------------------------

# Una función debe hacer UNA sola cosa. Lo ideal es que:
# - La función calcule/procese → return
# - Quien la llama decida qué hacer con el resultado → print, guardar, etc.

# Esto es importante porque si mañana necesitas ese valor para otra cosa
# (guardarlo en una base de datos, sumarlo, enviarlo por red), puedes hacerlo.
# Si la función lo imprimió y tiró el valor, ya no puedes.

# ❌ La función hace demasiado
def transaccion_mal(saldo, monto):
    if saldo >= monto:
        print(f"Retiro exitoso. Saldo actual: {saldo - monto}")  # imprime y pierde el valor
    else:
        print("Saldo insuficiente")

# ✅ La función calcula, quien llama decide
def transaccion_bien(saldo, monto):
    if saldo >= monto:
        return saldo - monto   # solo calcula y retorna
    else:
        return "Saldo insuficiente"

resultado = transaccion_bien(100, 40)
print(f"Retiro exitoso. Saldo actual: {resultado}")  # quien llama decide el mensaje


# ------------------------------------------------------------
# 5. EJEMPLO REAL: EJERCICIO 8 (excepciones + return)
# ------------------------------------------------------------

class InsufficientFundsError(Exception):
    pass

def monto(saldo, monto):
    if saldo < monto:
        raise InsufficientFundsError(
            f"Saldo insuficiente: tienes {saldo}, intentas retirar {monto}"
        )
    return saldo - monto  # solo retorna el cálculo, sin print

try:
    resultado = monto(100, 40)
    print(f"Retiro exitoso. Saldo actual: {resultado}")  # el print va aquí, fuera
except InsufficientFundsError as error:
    print(f"ERROR DE FONDOS: {error}")

# ¿Por qué el print está fuera?
# Porque si mañana esta función se usa en una API o en una app,
# quien llama a monto() decide cómo mostrar el resultado.
# La función solo hace su trabajo: calcular.


# ------------------------------------------------------------
# RESUMEN RÁPIDO
# ------------------------------------------------------------

# return print(...)  ❌  → siempre devuelve None
# return valor       ✅  → devuelve algo útil

# Si hay try/except o if/else:
#   → cada camino necesita su propio return

# La función calcula → return
# Quien la llama decide qué mostrar → print

# ============================================================