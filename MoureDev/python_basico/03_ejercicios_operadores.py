"""EJERCICIOS"""
# 1. Realiza las siguientes operaciones aritmeticas:
# Suma: 15 + 25
print(15 + 25)
# Resta: 50 - 22
print ( 50 - 22)
# Multiplicacion: 8 * 7
print (8 * 7)
# Division: 100 / 20
print (100 / 20)

# 2. Calcula el resto de la division de 37 entre 5 y almacenalo en una variable remainder. Luego impri­melo.
remainder= 37 % 5
print (remainder)
# 3. Convierte el numero 7 en una cadena de texto y concatenalo con la frase  "es mi numero favorito". Imprime el resultado.
 
print (str(7)+ " " + "es mi numero favorito")
# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicacio para cadenas y luego imprimela.
print ("python " *10) #aplicar el espacio entre la palabra y la comilla hace que quede un espacio entre cada palabra en el terminal
# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable  resultado. Imprime el valor de resultado.
a= 12
b= 8
resultado= a > b
print (resultado)
# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y < y explica cual tiene mayor orden alfabetico.
print ( "apple" > "banana")
print ( "apple" < "banana")
"""Lo que significa que "banana" tiene mayor orden alfabético porque su primera letra b 
viene después de a. 
Es exactamente como ordenar palabras en un diccionario."""
# 7. Realiza una comparacion logica usando and para verificar si el numero 10 es mayor que 5 y menor que 20. Imprime el resultado.
print (10 > 5 and 10 < 20)
# 8. Usa el operador or para verificar si el numero 7 es menor que 3 o mayor que 5. Imprime el resultado.
print ( 7 < 3 or 7 > 5)
# 9. Aplica el operador not para invertir el resultado de la comparacion 15 > 20. ¿Cual es el resultado?
print (not(15 > 20))
# 10. Combina operadores aritmeticos y logicos: Verifica si el numero resultante de la expresion (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
resultante= ((5 * 3) + 2 )
print (resultante > 10 and resultante < 20)