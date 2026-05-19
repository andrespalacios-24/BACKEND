### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores LÃ³gicos ###

#Basada en el Álgebra de Boole 
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))

# =============================================================================
# OPERADORES EN PYTHON — REFERENCIA COMPLETA
# Basado en: documentación oficial Python 3 (docs.python.org)
# =============================================================================


# -----------------------------------------------------------------------------
# ¿QUÉ ES UN OPERADOR?
# -----------------------------------------------------------------------------

# Un operador es un símbolo que le dice a Python que realice una operación
# sobre uno o más valores (llamados operandos).
#
# Ejemplo:
#   3 + 4
#   ↑   ↑ → operandos
#     ↑   → operador
#
# Python evalúa la expresión y devuelve un resultado.
# Ese resultado puede imprimirse, guardarse en una variable, o usarse en otra operación.


# =============================================================================
# 1. OPERADORES ARITMÉTICOS
# =============================================================================

# Realizan operaciones matemáticas sobre números (int o float).

# Operador  Símbolo  Ejemplo       Resultado
# --------  -------  -----------   ---------
# Suma         +      3 + 4          7
# Resta        -      3 - 4         -1
# Multiplic.   *      3 * 4          12
# División     /      3 / 4          0.75     ← siempre devuelve float
# Módulo       %      10 % 3         1        ← el residuo de la división
# División //  //     10 // 3        3        ← cociente entero (trunca)
# Potencia     **     2 ** 3         8

print(3 + 4)     # 7
print(3 - 4)     # -1
print(3 * 4)     # 12
print(3 / 4)     # 0.75   ← / siempre devuelve float, incluso 4/2 → 2.0
print(10 % 3)    # 1      ← 10 = 3*3 + 1, el residuo es 1
print(10 // 3)   # 3      ← 10/3 = 3.33..., trunca a 3
print(2 ** 3)    # 8      ← 2 elevado a la 3

# --- Diferencia entre / y // ---
print(7 / 2)     # 3.5   → división real
print(7 // 2)    # 3     → división entera (descarta los decimales)

# --- El módulo % ---
# Devuelve el residuo de dividir dos números.
# Muy usado para saber si un número es par/impar, o para ciclos:
print(10 % 2)    # 0  → par (no hay residuo)
print(11 % 2)    # 1  → impar
print(13 % 5)    # 3  → 13 = 5*2 + 3

# --- Precedencia (orden de evaluación) ---
# Python sigue el orden matemático estándar: PEMDAS / BODMAS
# 1. ** (potencia)
# 2. * / // % (multiplicación, división)
# 3. + - (suma, resta)
# Los paréntesis tienen máxima prioridad.

print(2 ** 3 + 3 - 7 / 1 // 4)
# Paso a paso:
# 2**3 = 8
# 7/1  = 7.0
# 7.0 // 4 = 1.0
# 8 + 3 - 1.0 = 10.0

# --- Operadores aritméticos con strings ---
# + concatena cadenas (las une)
print("Hola " + "Python")       # "Hola Python"
print("Hola " + str(5))         # "Hola 5"  ← str() obligatorio, no mezcla tipos

# * repite una cadena N veces
print("Hola " * 3)              # "Hola Hola Hola "
print("Hola " * (2 ** 3))       # repite 8 veces

my_float = 2.5 * 2              # 5.0
print("Hola " * int(my_float))  # int(5.0) = 5 → repite 5 veces

# --- Asignación con operador (shorthand) ---
# En lugar de escribir: x = x + 1
# Python permite la forma corta:
x = 10
x += 3    # x = x + 3  → 13
x -= 2    # x = x - 2  → 11
x *= 2    # x = x * 2  → 22
x //= 3   # x = x // 3 → 7
x **= 2   # x = x ** 2 → 49
x %= 10   # x = x % 10 → 9


# =============================================================================
# 2. OPERADORES COMPARATIVOS (de comparación)
# =============================================================================

# Comparan dos valores y devuelven siempre True o False (bool).
# Son la base de las condiciones (if, while, filtros).

# Operador  Significado          Ejemplo       Resultado
# --------  -------------------  -----------   ---------
#   >        mayor que           3 > 4          False
#   <        menor que           3 < 4          True
#   >=       mayor o igual que   4 >= 4         True
#   <=       menor o igual que   3 <= 4         True
#   ==       igual a             3 == 4         False  ← dos signos == (no =)
#   !=       diferente de        3 != 4         True

print(3 > 4)    # False
print(3 < 4)    # True
print(3 >= 4)   # False
print(4 <= 4)   # True
print(3 == 4)   # False
print(3 != 4)   # True

# IMPORTANTE: = asigna un valor. == compara dos valores.
# edad = 27    → guarda 27 en edad
# edad == 27   → pregunta: ¿edad es igual a 27? devuelve True o False

# --- Comparación de strings ---
# Python compara strings carácter a carácter usando su valor ASCII/Unicode.
# El orden es: números < mayúsculas < minúsculas (en ASCII estándar)
# "H" tiene valor ASCII 72, "P" tiene valor ASCII 80 → "H" < "P"

print("Hola" > "Python")     # False  ("H" < "P" en ASCII)
print("Hola" < "Python")     # True
print("aaaa" >= "abaa")      # False  (compara 2do carácter: 'a' < 'b')
print(len("aaaa") >= len("abaa"))  # True  (4 >= 4) ← compara longitudes, no contenido
print("Hola" == "Hola")      # True   (mismo contenido exacto)
print("Hola" == "hola")      # False  (mayúscula ≠ minúscula)
print("Hola" != "Python")    # True

# Tip: para comparar strings sin importar mayúsculas usar .lower() o .upper()
nombre = "ANDRES"
print(nombre.lower() == "andres")   # True


# =============================================================================
# 3. OPERADORES LÓGICOS
# =============================================================================

# Combinan condiciones booleanas. Basados en Álgebra de Boole.
# Devuelven True o False.

# Operador  Significado                          Devuelve True cuando...
# --------  -----------------------------------  ---------------------------
#   and      ambas condiciones deben ser True    las DOS son True
#   or       al menos una debe ser True          AL MENOS UNA es True
#   not      invierte el resultado               la condición era False

# --- and ---
# Solo True si AMBAS condiciones son True
print(3 > 4 and "Hola" > "Python")   # False and False → False
print(3 < 4 and "Hola" < "Python")   # True  and True  → True
print(3 < 4 and "Hola" > "Python")   # True  and False → False

# --- or ---
# True si AL MENOS UNA condición es True
print(3 > 4 or "Hola" > "Python")    # False or False → False
print(3 < 4 or "Hola" > "Python")    # True  or False → True

# --- not ---
# Invierte el resultado
print(not (3 > 4))    # not False → True
print(not (3 < 4))    # not True  → False

# --- Combinaciones con paréntesis ---
# Los paréntesis controlan el orden de evaluación (igual que en matemáticas)
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
# Primero evalúa lo de adentro: "Hola" > "Python" → False
# False and 4 == 4 → False and True → False
# 3 < 4 or False → True or False → True

# --- Tabla de verdad completa ---
# A      B      A and B   A or B   not A
# True   True    True      True     False
# True   False   False     True     False
# False  True    False     True     True
# False  False   False     False    True

# --- Short-circuit evaluation ---
# Python es "perezoso": en and, si el primer operando es False, no evalúa el segundo.
# En or, si el primer operando es True, no evalúa el segundo.
# Esto importa cuando la segunda condición podría causar un error.
lista = []
# print(lista[0] > 5)  → IndexError si la lista está vacía
print(len(lista) > 0 and lista[0] > 5)  # False — nunca llega a lista[0]


# =============================================================================
# 4. USO REAL EN BACKEND
# =============================================================================

# En desarrollo backend los operadores aparecen constantemente.
# Aquí algunos patrones reales:

# --- Validación de datos de entrada ---
# Al recibir datos de un usuario (formulario, API), se valida antes de procesar.

edad = 17
nombre_usuario = "Andrés"
password = "abc"

es_mayor_de_edad = edad >= 18
nombre_valido = len(nombre_usuario) >= 3 and len(nombre_usuario) <= 50
password_valida = len(password) >= 8

# Condición compuesta para permitir registro
puede_registrarse = es_mayor_de_edad and nombre_valido and password_valida
print(puede_registrarse)   # False (edad < 18 y password muy corta)

# --- Paginación de resultados ---
# Cuando una base de datos devuelve muchos registros, se muestran en páginas.
total_registros = 157
registros_por_pagina = 10

total_paginas = total_registros // registros_por_pagina      # 15
hay_pagina_extra = total_registros % registros_por_pagina    # 7 (no es 0, hay más)
if hay_pagina_extra != 0:
    total_paginas += 1   # la última página tiene solo 7 registros
print(total_paginas)     # 16

# --- Verificar permisos de usuario ---
# Un usuario puede acceder a un recurso si tiene el rol correcto O es admin.
rol_usuario = "editor"
es_admin = False

puede_editar = rol_usuario == "editor" or es_admin
puede_eliminar = es_admin
puede_leer = True   # todos pueden leer

print(puede_editar)    # True
print(puede_eliminar)  # False

# --- Cálculo de precios e impuestos ---
precio_base = 150_000     # COP, sin impuesto
IVA = 0.19
descuento = 0.10          # 10% de descuento

precio_con_descuento = precio_base * (1 - descuento)    # 135_000
precio_final = precio_con_descuento * (1 + IVA)         # 160_650
precio_final_entero = int(precio_final)                  # trunca centavos

print(f"Total a pagar: ${precio_final_entero:,}")  # $160,650

# --- Verificar si un ID es válido ---
# IDs en base de datos son enteros positivos y dentro de un rango.
id_recibido = 304

id_valido = isinstance(id_recibido, int) and id_recibido > 0
print(id_valido)   # True

# --- Número de página actual y offset para query SQL ---
# Cuando se consulta con LIMIT y OFFSET en SQL:
# SELECT * FROM productos LIMIT 10 OFFSET 20  → página 3
pagina_actual = 3
registros_por_pagina = 10
offset = (pagina_actual - 1) * registros_por_pagina   # (3-1)*10 = 20
print(offset)   # 20

# --- Detección de emails duplicados (comparación de strings) ---
email_nuevo = "andres@correo.com"
email_existente = "Andres@Correo.Com"

# Sin normalizar:
print(email_nuevo == email_existente)              # False ← falla

# Con normalización (patrón real en backend):
print(email_nuevo.lower() == email_existente.lower())  # True ← correcto


# =============================================================================
# RESUMEN RÁPIDO — tabla de operadores
# =============================================================================

# ARITMÉTICOS         COMPARATIVOS         LÓGICOS
# +   suma            ==  igual            and  ambas True
# -   resta           !=  diferente        or   al menos una True
# *   multiplicación  >   mayor            not  invierte resultado
# /   división real   <   menor
# //  división entera >=  mayor o igual
# %   módulo/residuo  <=  menor o igual
# **  potencia

# Shorthand: +=  -=  *=  /=  //=  %=  **=


# =============================================================================
# FUENTES
# =============================================================================
# - Operadores en Python:      https://docs.python.org/3/reference/expressions.html#operator-precedence
# - Tipos numéricos:           https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# - Operaciones con strings:   https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# - Álgebra de Boole / bool:   https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not