### EXCEPCIONES EN PYTHON - Referencia Completa ###
# Fuente base: MoureDev | Ampliado con docs.python.org
#
# ¿Qué es una excepción?
# Un error que ocurre DURANTE la ejecución del programa (no al escribirlo).
# Sin manejo de excepciones, el programa se ROMPE y para completamente.
# Con manejo, puedes controlar el error y decidir qué hacer.
#
# En backend esto es CRÍTICO: un servidor no puede romperse cada vez
# que un usuario manda datos incorrectos o una DB no responde.
#-----------------------------------------------------------------------
# REGLA
#-----------------------------------------------------------------------
# try → el código que puede fallar
# except → qué hacer si falla
# else → qué hacer si no falla
# finally → qué hacer siempre, pase lo que pase

# -----------------------------------------------------------------------

numberOne = 5
numberTwo = "1"  # Esto provoca TypeError al intentar sumar con un int

# -----------------------------------------------------------------------
### 1. ESTRUCTURA BASE: try / except ###
# -----------------------------------------------------------------------
# try   → código que PUEDE fallar
# except → qué hacer SI falla
#
# Uso en backend: envolver llamadas a DB, APIs externas, parseo de datos.
# Un except vacío (sin tipo) atrapa CUALQUIER excepción — útil como último
# recurso, pero en producción siempre es mejor especificar el tipo.

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce CUALQUIER excepción
    print("Se ha producido un error")

# -----------------------------------------------------------------------
### 2. FLUJO COMPLETO: try / except / else / finally ###
# -----------------------------------------------------------------------
# else    → se ejecuta SOLO si NO hubo excepción (el try fue exitoso)
# finally → se ejecuta SIEMPRE, haya o no error
#
# Uso en backend:
#   else    → procesar la respuesta si la llamada a la DB fue exitosa
#   finally → cerrar la conexión a la DB siempre, pase lo que pase
#             (evita conexiones abiertas que consumen recursos del servidor)

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Solo llega aquí si el try NO lanzó excepción
    print("La ejecución continúa correctamente")
finally:
    # Siempre se ejecuta — ideal para cerrar archivos, conexiones, etc.
    print("La ejecución continúa (finally siempre corre)")

# -----------------------------------------------------------------------
### 3. EXCEPCIONES POR TIPO ###
# -----------------------------------------------------------------------
# Puedes capturar excepciones específicas en orden de más específico
# a más general. Python recorre los except de arriba hacia abajo y
# ejecuta el PRIMERO que coincida.
#
# Jerarquía oficial (docs.python.org):
#   BaseException
#   └── Exception
#       ├── TypeError       → tipos incompatibles (int + str)
#       ├── ValueError      → tipo correcto, valor inválido (int("abc"))
#       ├── KeyError        → clave inexistente en diccionario
#       ├── IndexError      → índice fuera de rango en lista
#       ├── AttributeError  → atributo inexistente en objeto
#       ├── FileNotFoundError → archivo no encontrado
#       ├── ZeroDivisionError → división por cero
#       ├── ImportError     → módulo no encontrado
#       └── OSError         → errores del sistema operativo
#
# Regla importante: except más específico SIEMPRE antes que el general.
# Si pones except Exception primero, nunca llega a TypeError o ValueError.

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    # Tipo correcto pero valor inválido → ej: int("hola"), float("abc")
    # Backend: datos de formulario que tienen formato incorrecto
    print("Se ha producido un ValueError")
except TypeError:
    # Operación con tipos incompatibles → ej: 5 + "1", len(42)
    # Backend: usuario manda un string donde se esperaba un número
    print("Se ha producido un TypeError")

# -----------------------------------------------------------------------
### 4. CAPTURA DE INFORMACIÓN DE LA EXCEPCIÓN ###
# -----------------------------------------------------------------------
# "as nombre" → guarda el objeto excepción en una variable
# Puedes leer el mensaje de error con print(nombre)
#
# Exception es la clase base de casi todas las excepciones normales.
# Capturarla como último except es el patrón estándar en backend
# para errores inesperados (logs, alertas, respuestas genéricas al cliente).

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    # error contiene el mensaje y detalles del ValueError
    print(error)
except Exception as my_random_error_name:
    # Atrapa cualquier excepción no capturada arriba
    # En backend: aquí loggearías el error y devolverías HTTP 500
    print(my_random_error_name)

# -----------------------------------------------------------------------
### 5. RAISE: LANZAR EXCEPCIONES MANUALMENTE ###
# -----------------------------------------------------------------------
# "raise" lanza una excepción intencionalmente desde tu código.
# Útil para validar datos de entrada antes de procesarlos.
#
# Uso en backend: si el usuario manda un campo vacío o un valor fuera
# de rango, lanzas la excepción tú mismo en lugar de dejar que falle
# más adelante en un lugar difícil de depurar.

def crear_usuario(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    return f"Usuario creado con edad {edad}"

try:
    crear_usuario(-5)
except ValueError as e:
    print(f"Error de validación: {e}")

# -----------------------------------------------------------------------
### 6. EXCEPCIONES PERSONALIZADAS ###
# -----------------------------------------------------------------------
# Puedes crear tus propias excepciones heredando de Exception.
# Docs oficiales recomiendan heredar de Exception (no de BaseException).
#
# Uso en backend: errores específicos de tu dominio de negocio.
# En FastAPI, por ejemplo, defines excepciones propias para cada
# tipo de error de la API y las conviertes en respuestas HTTP.

class SaldoInsuficienteError(Exception):
    # Excepción personalizada para lógica de negocio bancaria
    pass

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(f"Saldo insuficiente: tienes {saldo}, intentas retirar {monto}")
    return saldo - monto

try:
    retirar(100, 500)
except SaldoInsuficienteError as e:
    print(f"Error de negocio: {e}")

# -----------------------------------------------------------------------
### RESUMEN: CUÁNDO USAR CADA COSA ###
# -----------------------------------------------------------------------
# try/except básico      → envolver cualquier operación que pueda fallar
# else                   → código que depende de que el try fue exitoso
# finally                → limpieza garantizada (cerrar archivos, conexiones)
# except TipoEspecífico  → manejar errores concretos con lógica diferente
# except Exception as e  → capturar error inesperado, loggearlo, responder
# raise                  → validar entradas y lanzar error controlado
# Clase propia de error  → errores de negocio específicos de tu aplicación

# ============================================================
# EXCEPCIONES COMUNES EN PYTHON - Referencia para try-except
# ============================================================
# Uso: except NombreError:
# Puedes capturar varios errores con múltiples except en un mismo try
# ============================================================


# ------------------------------------------------------------
# 1. ZeroDivisionError
# Cuándo ocurre: cuando divides un número entre cero
# ------------------------------------------------------------
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")


# ------------------------------------------------------------
# 2. ValueError
# Cuándo ocurre: cuando el tipo es correcto pero el valor no
# Ejemplo típico: int("hola") -> el input es string pero no es número
# ------------------------------------------------------------
try:
    numero = int("hola")
except ValueError:
    print("El valor no se puede convertir")


# ------------------------------------------------------------
# 3. TypeError
# Cuándo ocurre: cuando operas con tipos incompatibles
# Ejemplo: sumar un string con un entero
# ------------------------------------------------------------
try:
    resultado = "tres" + 3
except TypeError:
    print("Tipos de datos incompatibles")


# ------------------------------------------------------------
# 4. FileNotFoundError
# Cuándo ocurre: cuando intentas abrir un archivo que no existe
# ------------------------------------------------------------
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("El archivo no fue encontrado")


# ------------------------------------------------------------
# 5. IndexError
# Cuándo ocurre: cuando accedes a un índice que no existe en una lista
# ------------------------------------------------------------
lista = [1, 2, 3]
try:
    print(lista[10])
except IndexError:
    print("El índice no existe en la lista")


# ------------------------------------------------------------
# 6. KeyError
# Cuándo ocurre: cuando buscas una clave que no existe en un diccionario
# ------------------------------------------------------------
diccionario = {"nombre": "Andrés"}
try:
    print(diccionario["edad"])
except KeyError:
    print("La clave no existe en el diccionario")


# ------------------------------------------------------------
# 7. AttributeError
# Cuándo ocurre: cuando usas un método o atributo que no existe
# Ejemplo: llamar .upper() sobre un entero
# ------------------------------------------------------------
try:
    numero = 5
    numero.upper()
except AttributeError:
    print("Ese método no existe para este tipo de dato")


# ------------------------------------------------------------
# 8. NameError
# Cuándo ocurre: cuando usas una variable que no ha sido definida
# ------------------------------------------------------------
try:
    print(variable_inexistente)
except NameError:
    print("La variable no está definida")


# ------------------------------------------------------------
# CAPTURAR VARIOS ERRORES EN UN MISMO TRY
# Útil cuando una función puede fallar por distintas razones
# ------------------------------------------------------------
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: división entre cero")
    except TypeError:
        print("Error: los valores deben ser números")


# ------------------------------------------------------------
# FINALLY - se ejecuta SIEMPRE, haya error o no
# Útil para cerrar archivos, conexiones, etc.
# ------------------------------------------------------------
documento = None
try:
    documento = open("archivo.txt", "r")
    contenido = documento.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    if documento is not None:
        documento.close()


# ------------------------------------------------------------
# WITH - alternativa moderna a try/finally para archivos
# Cierra el archivo automáticamente al salir del bloque
# ------------------------------------------------------------
try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado")


# ============================================================
# ¿CUÁNDO VA EL INPUT DENTRO O FUERA DEL TRY?
# ============================================================

#NOTA: La regla real es: todo lo que pueda fallar debe estar dentro de algún try. 
#La decisión es si usas uno o dos bloques separados. 

# ✅ "FUERA" no significa fuera de todo try
# Significa: en un try SEPARADO, antes de la operación

def ejemplo_fuera():
    try:
        numero_1 = int(input("Ingrese primer numero: "))
        numero_2 = int(input("Ingrese segundo numero: "))
    except ValueError:
        print("Debes ingresar un número entero")
        return

    try:
        print(numero_1 / numero_2)
    except ZeroDivisionError:
        print("No se puede dividir por cero")

# ✅ "DENTRO" significa: todo en el mismo try
def ejemplo_dentro():
    try:
        numero_1 = int(input("Ingrese primer numero: "))
        numero_2 = int(input("Ingrese segundo numero: "))
        print(numero_1 / numero_2)
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("Debes ingresar un número entero")

# Ventaja: más simple y conciso