# 1. Genera un SyntaxError al imprimir una cadena sin parentesis.
print "da error o no ?"

# 2. Genera un NameError intentando usar una variable no definida.
#numerito= 23
print(numerito)

# 3. Genera un IndexError accediendo a un i­ndice inexistente de una lista.
lista=[1,2,3,4,5,6,7,8,9,]
print(lista[9])

# 4. Genera un ModuleNotFoundError al importar un modulo inexistente.
import modulo 

# 5. Genera un AttributeError accediendo a un atributo que no existe.
from datetime import date
date.dai    

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.
diccionario= {"moto":"xtz", "año":"2018"}
print(diccionario["motor"])

# 7. Genera un TypeError usando tipos incorrectos (indice string en lista).
print(lista["2"])

# 8. Genera un ImportError al importar una funcion que no existe desde un modulo.
from datetime import datetaim

# 9. Genera un ValueError intentando convertir un string no numerico a entero.
numeral= int("10 numerales")

# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.
try:
    print(diccionario["anio"])
except KeyError:
    print("error")
