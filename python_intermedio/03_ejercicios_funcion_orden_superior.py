# 1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.

def multiply(numero_m):
    return numero_m * 333

def recibelo (numero, funcion):
    return funcion(numero)

print (recibelo(45,multiply))
    
# 2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.
def restica(numero):
    return numero - 2

def sumita(numero_1,numero_2,funcion):
    return funcion(numero_1 + numero_2)

print (sumita(5,5,restica))

# 3. Crea una función que devuelva otra función que sume un número fijo.

def sum_ten(numero_fijo):
    def add(value):
        return value + numero_fijo  
    return add

suma_cinco = sum_ten(5)
print(suma_cinco(3))  

# 4. Usa map() con lambda para multiplicar cada número de una lista por 10.

#pseudocodigo
#crear lista de donde el map() tomara los numeros
#crear lambda donde tome cada elemento del iterable de la lista y lo multiplique por el 10
#para imprimir debe ser en una lista porque map devuelve un objeto que debe ser convertido en lista

listica= [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda numero:numero * 10, listica)))

# 5. Usa filter() con lambda para quedarte solo con los números pares.

#pseudocodigo
#se crea lista de donde filter tomara los valores segun los parametros establecidos con el lambda
#se escribe el lambda donde todo numero %2 ==0 que al pasarlo por esta operacion sea igual a cero es par
# filter() usa el parametro y solo deja los numeros pares
numeritos= [14, 37, 82, 5, 19, 64, 91, 23, 48, 77]
print(list(filter(lambda numero : numero %2 == 0,numeritos))) 

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce
#pseudocodigo
#crear lista de donde reduce ire acumulando los numeros sumandolos hasta que quede 1 solo
#crear el lambda donde se sumen los numeros.
listilla= [14, 37, 82, 5, 19, 64, 91, 23, 48, 77]

print(reduce(lambda a,b: a + b, listilla))

# 7. Escribe una función que devuelva una función que reciba un nombre y devuelva “Hola, ”.

def nombrecito (nombre):
    def add():
        return "hola," + nombre
    return add

nombre= nombrecito("robertillo")
print(nombre())

# 8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.

# pseudocodigo
# La condición la decide quien llama a selector, no selector mismo
# Pseudocódigo:
# crear funcion selector que reciba (funcion, lista)
#   crear contador = 0
#   por cada elemento en lista:
#       si funcion(elemento) es True:
#           contador += 1
#   retornar contador

def selector(funcion, lista):
    contador = 0
    for x in lista:
        if funcion(x):  # aquí usamos la función que llegó como parámetro
            contador += 1
    return contador

def es_impar(numero):
    return numero % 2 != 0

numeracos = [14, 37, 82, 5, 19, 64, 91, 23, 48, 77]
print(selector(es_impar, numeracos))  # cuenta los impares


# 9. Crea una función que reciba dos funciones y un número, y las aplique en orden.

# 10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).bucle (sin map).