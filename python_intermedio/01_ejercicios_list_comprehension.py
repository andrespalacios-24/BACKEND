# 1. Genera una lista utilizando comprension con los numeros del 0 al 10.
#pseudocodigo
#crear la variable donde ira la lista
#escribir la lista con el rango de numeros que van a ir dentro de esta con range()
lista= [i for i in range(11)] 
print(lista)

# 2. Crea una lista utilizando comprension con los cuadrados de los numeros del 1 al 10.
#pseudocodigo
# crear variable donde ira la lista
#escribir el por cuanto se multiplicara cada numero de la lista
#definir el rango de numeros 
lista=[i  ** 2 for i in range(1,11)]
print(lista)

# 3. Genera una lista utilizando comprension con los numeros pares del 0 al 20.
#pseudocodigo
# crear variable de la lista
#especificar el rago 
#dentro de la lista hacer una condiciones if donde i deba ser  %2 ==0 
pares= [i for i in range(21) if i %2==0]
print(pares)
#segunda solucion mas eficiente
pares= [i for i in range(0,21,2) ]
print(pares)
# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprension.
# pseudocodigo
#se crea la variable para la lista, donde se ponen las temperaturas en celcius
#se crea una variable de donde se toman las temperturas y se hace la operacion para convertir
#con la siguiente operacion grados c= c *1.8 +32
lista_grados_C= [24.2, 6.1, 13.8, 29.5, 5.4, 18.9, 2.7, 34.1, 11.0, 27.6 ]
convertir_f=[t * 1.8 + 32 for t in lista_grados_C]

# 5. Crea una lista utilizando comprension con los caracteres de una cadena.

caracteres= "maykel"
contador_caracteres= [s for s in caracteres]
print(contador_caracteres)

# 6. Filtra una lista de palabras y deja solo las que tienen mas de 4 letras utilizando comprension.

#crear la variable para la lista de palabras
#crear la lista con la condicion que la palabra tenga mas de 4 letras con if y len 

palabras = ["sol", "luz", "montaña", "mar", "elefante", "té", "bicicleta", "pez", "horizonte", "relámpago", "pan", "arquitectura", "sal", "espectáculo"]
filtro= [s for s in palabras if len(s) > 4]
print(filtro)
 
# 7. Aumenta en 5 cada numero de una lista con comprension usando una funcion externa.

#crear una lista con numeros
#crear un funcion que aumente en 5 cada numero de una lista.
#crear la lista de comprension donde se integra con la funcion de aumento +5

def aumento_en_cinco(numero):
    return numero +5

numeros=[1,2,3,4,5,6,7,8,9,10]
numeros_mas_cinco= [aumento_en_cinco(n) for n in numeros]
print(numeros_mas_cinco)

# 8. Crea una lista de booleanos que indique si cada numero es mayor que 10 utilizando comprension.

# crear lista de numeros
#crear lista de comprension donde se compare si cada numero es menor o mayor a 10 

lista_numeros= [11, 15, 20, 50, 100, 9, 5, 2, 0, -5]
booleanos= [n >10 for n in lista_numeros  ]
print(booleanos)

# 9. Multiplica solo los numeros impares por 3 en una lista utilizando comprension.

# pseudocodigo
#crear lista con numeros pares e impares.
#con la lista de comprension verificar si cada numero es residuo de 0 si no es impar y se multiplica por 3
numeros= [7, 12, 3, 22, 15, 8, 1, 30, 19, 4]
imparesx3= [n * 3 for n in numeros if n %2 !=0 ]
print(imparesx3)

# 10. Usa comprension de listas anidada para generar una matriz 3x3 con numeros del 1 al 9.

# pseudocodigo
# definir cuantas filas tendra la matriz (3)
# calcular el numero de inicio de cada fila con la formula: fila * 3 + 1
#   fila 0 → 0 * 3 + 1 = 1  → [1, 2, 3]
#   fila 1 → 1 * 3 + 1 = 4  → [4, 5, 6]
#   fila 2 → 2 * 3 + 1 = 7  → [7, 8, 9]
# el for externo recorre las filas (0, 1, 2)
# el for interno genera los 3 numeros de cada fila desde el inicio
# la variable 'fila' nace en el for externo y se usa dentro del for interno
 
matriz = [
    [i for i in range(fila * 3 + 1, fila * 3 + 4)]
    for fila in range(3)
]
print(matriz)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# i    → se guarda en la lista
# fila → solo se usa para calcular el rango