### Error Types - Explicado ###
# Referencia: MoureDev Python Intermedio
# Fuente oficial: https://docs.python.org/3/library/exceptions.html
#
# Todos los errores en Python heredan de la clase base "Exception".
# Python los clasifica por tipo para que puedas identificar QUÉ salió mal
# y dónde, sin tener que adivinar. Cada tipo apunta a una causa distinta.


# =============================================================================
# 1. SyntaxError
# =============================================================================
# QUÉ ES: Error de sintaxis. Python no puede ni leer el código porque viola
#         las reglas del lenguaje. Ocurre ANTES de ejecutar cualquier cosa.
#
# POR QUÉ OCURRE AQUÍ:
#   print "¡Hola comunidad!"   <-- sintaxis de Python 2, no válida en Python 3
#   En Python 3, print es una función y SIEMPRE necesita paréntesis.
#
# CÓMO CORREGIR:
#   print("¡Hola comunidad!")  <-- con paréntesis
#
# REGLA: Si Python ni siquiera arranca a ejecutar tu archivo, sospecha SyntaxError.

from math import pi
import math
print("¡Hola comunidad!")


# =============================================================================
# 2. NameError
# =============================================================================
# QUÉ ES: Intentas usar una variable o nombre que Python no conoce —
#         porque nunca fue definida, o fue escrita con otro nombre.
#
# POR QUÉ OCURRE AQUÍ:
#   Si comentas la línea   language = "Spanish"
#   y luego haces          print(language)
#   Python busca "language" en memoria y no la encuentra.
#
# CÓMO CORREGIR:
#   Asegúrate de definir la variable ANTES de usarla.
#   language = "Spanish"   <-- esta línea debe existir y ejecutarse primero
#
# REGLA: NameError = "no sé qué es eso". Revisa typos y orden de ejecución.

language = "Spanish"
print(language)


# =============================================================================
# 3. IndexError
# =============================================================================
# QUÉ ES: Intentas acceder a una posición de una lista (u otra secuencia)
#         que NO existe. Los índices van de 0 a len(lista)-1.
#
# POR QUÉ OCURRE AQUÍ:
#   my_list tiene 5 elementos → índices válidos: 0, 1, 2, 3, 4 (o -1 a -5)
#   my_list[5]  <-- no existe, el último es [4]. Python lanza IndexError.
#
# CÓMO CORREGIR:
#   Verificar el largo con len(my_list) antes de acceder,
#   o usar índices negativos para acceder desde el final: my_list[-1]
#
# REGLA: IndexError = te pasaste del límite de la secuencia.

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])   # "Python"  → índice 0, válido
print(my_list[4])   # "JavaScript" → índice 4, el último válido
print(my_list[-1])  # "JavaScript" → -1 siempre es el último elemento
# print(my_list[5]) # IndexError: list index out of range


# =============================================================================
# 4. ModuleNotFoundError
# =============================================================================
# QUÉ ES: Intentas importar un módulo que Python no puede encontrar —
#         porque no existe, está mal escrito, o no está instalado.
#         Es una subclase de ImportError (más específica).
#
# POR QUÉ OCURRE AQUÍ:
#   import maths  <-- el módulo se llama "math", no "maths"
#   Python busca en su librería estándar y en los paquetes instalados, y no lo encuentra.
#
# CÓMO CORREGIR:
#   import math   <-- nombre correcto
#   Si el módulo es externo (ej: requests), instalarlo con: pip install requests
#
# REGLA: ModuleNotFoundError = el módulo no existe con ese nombre donde Python lo busca.

# import maths  # ModuleNotFoundError: No module named 'maths'
import math     # Correcto


# =============================================================================
# 5. AttributeError
# =============================================================================
# QUÉ ES: Intentas acceder a un atributo o método que NO existe
#         en ese objeto o módulo.
#
# POR QUÉ OCURRE AQUÍ:
#   math.PI   <-- Python es case-sensitive. El atributo se llama "pi" (minúsculas)
#               "PI" no existe en el módulo math → AttributeError.
#
# CÓMO CORREGIR:
#   math.pi   <-- exactamente como está definido en el módulo
#
# REGLA: AttributeError = el objeto SÍ existe, pero esa propiedad/método NO.
#        Revisa mayúsculas, typos, y la documentación del objeto.

# print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'
print(math.pi)    # 3.141592653589793 → correcto


# =============================================================================
# 6. KeyError
# =============================================================================
# QUÉ ES: Intentas acceder a una clave de un diccionario que NO existe.
#         Similar al IndexError pero para dicts (que usan claves, no índices).
#
# POR QUÉ OCURRE AQUÍ:
#   my_dict["Apelido"]  <-- typo: falta la "l". La clave real es "Apellido"
#   Python busca exactamente "Apelido" y no lo encuentra → KeyError.
#
# CÓMO CORREGIR:
#   Opción 1: Corregir el typo → my_dict["Apellido"]
#   Opción 2: Usar .get() para evitar el error → my_dict.get("Apelido", "No encontrado")
#             .get() devuelve None (o el valor por defecto) si la clave no existe.
#
# REGLA: KeyError = esa clave no está en el diccionario. Ojo con typos y case-sensitivity.

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])       # 35 → clave válida
# print(my_dict["Apelido"])  # KeyError: 'Apelido'
print(my_dict["Apellido"])   # "Moure" → clave correcta
print(my_dict.get("Apelido", "Clave no encontrada"))  # alternativa segura con .get()


# =============================================================================
# 7. TypeError
# =============================================================================
# QUÉ ES: Usas un tipo de dato incorrecto para una operación.
#         Python esperaba un tipo y recibió otro incompatible.
#
# POR QUÉ OCURRE AQUÍ:
#   my_list["0"]  <-- los índices de listas deben ser int, no str.
#                     "0" (string) no es válido como índice → TypeError.
#
# NOTA INTERESANTE:
#   my_list[False] NO lanza error porque bool es subclase de int en Python.
#   False == 0  y  True == 1, por lo que my_list[False] == my_list[0]
#
# CÓMO CORREGIR:
#   Usar siempre enteros como índices: my_list[0]
#
# REGLA: TypeError = operación válida, pero con el tipo de dato equivocado.

# print(my_list["0"])  # TypeError: list indices must be integers or slices, not str
print(my_list[0])      # "Python" → índice entero, correcto
print(my_list[False])  # "Python" → False == 0 en Python (bool hereda de int)


# =============================================================================
# 8. ImportError
# =============================================================================
# QUÉ ES: El módulo SÍ existe, pero el nombre específico que intentas
#         importar desde él NO existe dentro de ese módulo.
#         (ModuleNotFoundError es cuando el módulo entero no existe;
#          ImportError es cuando el módulo existe pero el nombre importado, no)
#
# POR QUÉ OCURRE AQUÍ:
#   from math import PI  <-- "PI" en mayúsculas no existe en math.
#                            El nombre correcto es "pi" (minúsculas).
#
# CÓMO CORREGIR:
#   from math import pi   <-- nombre exacto como está en el módulo
#
# REGLA: ImportError = el módulo existe, pero ese nombre no está dentro de él.

# from math import PI  # ImportError: cannot import name 'PI' from 'math'
from math import pi  # Correcto
print(pi)            # 3.141592653589793


# =============================================================================
# 9. ValueError
# =============================================================================
# QUÉ ES: El tipo de dato ES correcto, pero el VALOR no es válido
#         para esa operación. A diferencia de TypeError (tipo incorrecto),
#         aquí el tipo está bien pero el contenido no tiene sentido.
#
# POR QUÉ OCURRE AQUÍ:
#   int("10 Años")  <-- str es el tipo correcto para int(), pero
#                       "10 Años" no se puede convertir a entero porque
#                       contiene texto extra. int() solo acepta dígitos puros.
#
# CÓMO CORREGIR:
#   Pasar solo el número como string: int("10")
#   O limpiar el string antes: int("10 Años".split()[0])
#
# REGLA: ValueError = tipo correcto, contenido inválido para esa operación.

# my_int = int("10 Años")  # ValueError: invalid literal for int() with base 10
my_int = int("10")
print(type(my_int))  # <class 'int'>


# =============================================================================
# 10. ZeroDivisionError
# =============================================================================
# QUÉ ES: Intentas dividir un número entre cero, lo cual es matemáticamente
#         indefinido. Python lo detecta y lanza este error explícitamente.
#
# POR QUÉ OCURRE AQUÍ:
#   4 / 0  <-- dividir por cero no tiene resultado definido.
#
# CÓMO CORREGIR:
#   Verificar que el divisor no sea cero antes de dividir:
#
#   divisor = 0
#   if divisor != 0:
#       print(4 / divisor)
#   else:
#       print("No se puede dividir entre cero")
#
# REGLA: ZeroDivisionError = siempre valida que tu divisor no sea 0,
#        especialmente cuando viene de input del usuario o de cálculos previos.

# print(4 / 0)  # ZeroDivisionError: division by zero
print(4 / 2)    # 2.0 → correcto


# =============================================================================
# RESUMEN RÁPIDO
# =============================================================================
#
# | Error                | Causa principal                                    |
# |----------------------|----------------------------------------------------|
# | SyntaxError          | Código mal escrito, Python no lo puede leer        |
# | NameError            | Variable/nombre no definido                        |
# | IndexError           | Índice fuera del rango de la secuencia             |
# | ModuleNotFoundError  | Módulo no existe o no está instalado               |
# | AttributeError       | Atributo/método no existe en ese objeto            |
# | KeyError             | Clave no existe en el diccionario                  |
# | TypeError            | Tipo de dato incorrecto para la operación          |
# | ImportError          | Nombre no existe dentro del módulo                 |
# | ValueError           | Tipo correcto, pero valor inválido para la op.     |
# | ZeroDivisionError    | División entre cero                                |
#
# Todos heredan de Exception → puedes capturarlos con try/except (siguiente tema)
# Docs oficiales: https://docs.python.org/3/library/exceptions.html