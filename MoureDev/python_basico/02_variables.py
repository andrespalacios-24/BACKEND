# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un numero entero que represente tu edad.
# height: un numero flotante que represente tu altura.
# Imprime cada variable en una linea separada.
name = "ANDRES"
age = 27
height = 1.76
print(name, age, height, sep="\n")
""" al imprimir hay 2 formas de que el texto quede en lineas individuales en el terminal
1. dandole print() en lineas separadas para cada terminal
2. usando sep="\n" al final de las variables en el print (como se hizo en el ejercicio)"""
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
age = 27
print ("cuantos años tienes" + " " + str(age) + "años")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_student= True
print ("es estudiante" + " " + str (is_student))
""" tambien se podia separar solo con una coma(,) ya que esta no mezcla variables
y asi no poner (+) que los concatena
pero no se tiene control sobre el formato del texto al usar (,)"""
# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
name= "ANDRES FELIPE PALACIOS VIVEROS"
print (len(name))
# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad= "andres", "palacios", "buga" # los valores en texto siempre entre comillas
print (nombre +" " + apellido + " " + ciudad) 
# usando f_string
print(f"Hola, soy {nombre} {apellido} y vivo en {ciudad}")
"""La f antes de las comillas le dice a Python que dentro del texto puede haber variables 
entre {}. Python las reemplaza automáticamente por sus valores.
El f-string produjo exactamente el mismo resultado que con +, 
pero el código queda mucho más limpio y fácil de leer."""
# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color= input ("color favorito")
print ("su color favorito es:", color) 
# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit= "banano"
print (fruit) 
fruit= "pera"
print (fruit) 
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price= 25.596
print (int(price)) 
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len= "carrera quince numero venticiete a catorce"
print (len(address_len))
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone= int(12345678)
print (type(phone))
phone= int(87654321)
print (type(phone))

# =============================================================================
# VARIABLES EN PYTHON — REFERENCIA COMPLETA
# Basado en: documentación oficial Python 3 (docs.python.org)
# =============================================================================


# -----------------------------------------------------------------------------
# ¿QUÉ ES UNA VARIABLE?
# -----------------------------------------------------------------------------

# Una variable es un nombre que apunta a un valor almacenado en memoria.
# Python no "guarda el valor dentro del nombre" — guarda el valor en memoria
# y el nombre es simplemente una etiqueta que apunta a ese lugar.

# Sintaxis básica:
#   nombre_variable = valor

edad = 27           # el nombre "edad" apunta al valor 27 en memoria
nombre = "Andrés"   # el nombre "nombre" apunta a la cadena "Andrés"

# En Python, las variables NO necesitan declararse con un tipo explícito.
# Python infiere el tipo automáticamente según el valor asignado.
# Esto se llama tipado dinámico.

x = 10       # x es int
x = "hola"   # ahora x es str — Python lo permite sin error


# -----------------------------------------------------------------------------
# REGLAS PARA NOMBRAR VARIABLES
# -----------------------------------------------------------------------------

# ✅ PERMITIDO:
nombre = "Andrés"
edad_usuario = 27
_privada = True
miVariable2 = 3.14   # camelCase (válido, pero no es el estilo Python)
mi_variable = 3.14   # snake_case (estilo recomendado en Python)

# ❌ NO PERMITIDO:
# 2variable = 10      → no puede empezar con número
# mi-variable = 10    → el guion (-) no es válido
# class = "algo"      → "class" es una palabra reservada de Python

# Convención oficial (PEP 8):
# - Usar snake_case para variables y funciones: mi_variable, calcular_precio
# - Usar MAYÚSCULAS para constantes: PI = 3.14159
# - Usar CamelCase solo para clases: class MiClase


# -----------------------------------------------------------------------------
# TIPOS DE DATOS BÁSICOS (built-in types)
# -----------------------------------------------------------------------------

# Python tiene tipos de datos integrados. Los más usados al inicio:

# 1. int — números enteros (sin decimales)
edad = 27
temperatura = -5
poblacion = 1_000_000   # el guion bajo es válido como separador visual

print(type(edad))       # <class 'int'>

# 2. float — números decimales (punto flotante)
altura = 1.76
pi = 3.14159
temperatura_f = -2.5

print(type(altura))     # <class 'float'>

# Nota: los floats tienen limitaciones de precisión por cómo se almacenan
# en binario. Ejemplo conocido:
print(0.1 + 0.2)        # 0.30000000000000004 (no es un bug, es IEEE 754)

# 3. str — cadenas de texto (strings)
nombre = "Andrés"
apellido = 'Palacios'           # comillas simples o dobles, ambas válidas
mensaje = "Hola, soy 'Andrés'"  # comillas simples dentro de dobles
parrafo = """Este es un texto
que ocupa varias líneas."""     # triple comilla para texto multilínea

print(type(nombre))     # <class 'str'>

# 4. bool — valores booleanos (True o False)
# Nota: la primera letra SIEMPRE en mayúscula (True, False)
es_estudiante = True
tiene_trabajo = False

print(type(es_estudiante))  # <class 'bool'>

# Los booleanos son subclase de int en Python:
print(True + True)   # 2  (True equivale a 1, False a 0)

# 5. NoneType — representa la ausencia de valor
resultado = None     # variable declarada pero sin valor asignado aún

print(type(resultado))  # <class 'NoneType'>
print(resultado is None)  # True  ← la forma correcta de comparar con None


# -----------------------------------------------------------------------------
# TIPOS DE DATOS COMPUESTOS (para guardar colecciones)
# -----------------------------------------------------------------------------

# Estos se estudian con más profundidad en sus propios temas,
# pero es útil conocerlos como tipos de variable:

# list — colección ordenada, modificable, permite duplicados
frutas = ["manzana", "pera", "banano"]

# tuple — colección ordenada, NO modificable
coordenadas = (4.536, -75.678)

# dict — pares clave:valor
persona = {"nombre": "Andrés", "edad": 27}

# set — colección sin orden, sin duplicados
numeros_unicos = {1, 2, 3, 3, 2}   # guarda {1, 2, 3}


# -----------------------------------------------------------------------------
# CONVERSIÓN DE TIPOS (type casting)
# -----------------------------------------------------------------------------

# Python no convierte tipos automáticamente (en la mayoría de casos).
# Se hace explícitamente con funciones integradas:

edad_texto = "27"
edad_numero = int(edad_texto)    # str → int
print(type(edad_numero))         # <class 'int'>

precio = 25.99
precio_entero = int(precio)      # float → int (trunca, NO redondea)
print(precio_entero)             # 25

numero = 42
numero_texto = str(numero)       # int → str
print("Tengo " + numero_texto + " años")

es_mayor = bool(1)               # cualquier valor distinto de 0 → True
es_menor = bool(0)               # 0, None, "", [], {} → False

# Tabla de conversiones comunes:
# int("27")      → 27           (str numérica a entero)
# float("3.14")  → 3.14         (str numérica a flotante)
# str(100)       → "100"        (cualquier tipo a cadena)
# bool(0)        → False        (0, None, colecciones vacías → False)
# bool("hola")   → True         (cadenas no vacías → True)


# -----------------------------------------------------------------------------
# ASIGNACIÓN MÚLTIPLE Y OTRAS FORMAS
# -----------------------------------------------------------------------------

# Varias variables en una línea (desempaquetado)
nombre, apellido, ciudad = "Andrés", "Palacios", "Buga"

# Mismo valor a varias variables a la vez
a = b = c = 0

# Intercambiar valores sin variable temporal (Pythonic)
x = 10
y = 20
x, y = y, x    # ahora x=20, y=10


# -----------------------------------------------------------------------------
# VERIFICAR TIPO Y PERTENENCIA
# -----------------------------------------------------------------------------

altura = 1.76

print(type(altura))             # <class 'float'>
print(isinstance(altura, float))  # True — forma recomendada para verificar tipo
print(isinstance(altura, int))    # False

# isinstance() es preferida sobre type() == float porque respeta herencia


# -----------------------------------------------------------------------------
# ÁMBITO DE VARIABLES (scope) — introducción
# -----------------------------------------------------------------------------

# Las variables tienen un "ámbito": el lugar del código donde son accesibles.

# Variable global — definida fuera de funciones, accesible en todo el archivo
saludo = "Hola"

def mostrar():
    # Variable local — solo existe dentro de esta función
    mensaje = "Mundo"
    print(saludo + " " + mensaje)   # puede leer la global

mostrar()
# print(mensaje)  → NameError: 'mensaje' no existe fuera de la función

# Regla general para empezar:
# - Las variables definidas dentro de una función son locales (mueren al terminar)
# - Las variables definidas fuera son globales (viven todo el programa)


# -----------------------------------------------------------------------------
# CONSTANTES — convención en Python
# -----------------------------------------------------------------------------

# Python no tiene constantes reales (no hay palabra clave como en otros lenguajes)
# La convención (PEP 8) es usar MAYÚSCULAS para indicar que no debe cambiarse:

PI = 3.14159
IMPUESTO_IVA = 0.19
MAX_INTENTOS = 3

# Python no impide cambiarlas — es una señal para otros programadores


# -----------------------------------------------------------------------------
# RESUMEN RÁPIDO — tabla de tipos
# -----------------------------------------------------------------------------

# Tipo        Ejemplo              Descripción
# -------     -----------------    ----------------------------------------
# int         edad = 27            Números enteros, positivos o negativos
# float       altura = 1.76        Números con decimales
# str         nombre = "Andrés"    Texto entre comillas simples o dobles
# bool        activo = True        Solo True o False (mayúscula obligatoria)
# NoneType    dato = None          Ausencia de valor
# list        items = [1, 2, 3]    Colección ordenada y modificable
# tuple       pos = (x, y)         Colección ordenada e inmutable
# dict        d = {"k": "v"}       Pares clave-valor
# set         s = {1, 2, 3}        Colección sin duplicados ni orden


# -----------------------------------------------------------------------------
# FUENTES
# -----------------------------------------------------------------------------
# - Documentación oficial Python 3: https://docs.python.org/3/library/stdtypes.html
# - PEP 8 (convenciones de estilo): https://peps.python.org/pep-0008/
# - Python Built-in Types: https://docs.python.org/3/library/stdtypes.html