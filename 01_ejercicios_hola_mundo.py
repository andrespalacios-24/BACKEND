# 1- Imprime "¡Hola Mundo!" por consola.
print ("hola mundo")
# 2- Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# este codigo hace visible el texto en el terminal
# 3- Imprime tu nombre y edad en la misma línea utilizando la función print.
print ("nombre: Andres, Edad: 27 años")
# 4- Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print (type("texto"))
print (type(45))
print (type(3.6))
# tipos de datos
# 5- Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""que son los tipos de datos en py?
Son las categorías que le dicen a Python 
qué tipo de valor estás manejando.
Tipos de datos en Python:
str   -> texto, ejemplo: "hola"
int   -> entero, ejemplo: 10
float -> decimal, ejemplo: 3.14
bool  -> verdadero o falso, True / False
list  -> colección, ejemplo: [1, 2, 3]
dict  -> clave y valor, ejemplo: {"nombre": "Andrés"}
"""
# 6- Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
"""se usa para unir 2 o mas cadenas de texto
en una sola"""
print("hola" + "mundo")
"""si se quiere que imprima separado
se debe poner"""
print ("hola" + " " + "mundo")
# dejando el espacio entre las comillas
# 7- Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
NOMBRE= "Andres" 
EDAD= 27
print (NOMBRE + " " + str(EDAD))
""" debido a que la variable edad 
esta en numeros al concatenar dara error por eso se debe poner str()
asi no hay conflicto y al imprimir se vera en numeros"""
# 8- Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo
NOMBRE= input ("CUAL ES TU NOMBRE ?")
print ("HOLA!!!" + NOMBRE ) 
""" input() solicita datos al usuario desde la consola. (terminal)
El texto dentro de los paréntesis es el mensaje que ve el usuario.
Lo que el usuario escriba queda guardado en una variable.
despues se usa print () y se concatena el texto que el usuario vera
al escribir su nombre en la terminal
"""
# 9- Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
X= 34
Y= 56
print (type(X + Y))
print (X + Y)
# 10- Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
# para el ejercicio 9 se crearon 2 variables con valores enteros
# despues se usa print mas el type() para ver el tipo de variables de esta linea en el terminal
# se pedia una suma, en python solo basta con el comando print y la suma de las variables
# en el terminal se mostrara el tipo de variable y despues la suma de las variables