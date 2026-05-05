# ============================================================
# REFUERZO - FUNCIONES DE ORDEN SUPERIOR
# Enfoque: pasar funciones como parámetro + acumular resultados
# ============================================================

# ------------------------------------------------------------
# EJERCICIO 1
# Crea una función llamada `aplicar_a_todos` que reciba una lista
# y una función, y devuelva una nueva lista con la función aplicada
# a cada elemento. Usa un bucle for (sin map).
#
# Pruébala con una función que eleve cada número al cuadrado.
#
# Pseudocódigo:
# crear funcion que va a recibir la lista y otra funcion
# crear una lista vacia donde retornen los elementos a  los que se le aplique la segunda funcion
# usar bucle for x in lista... para recorrer cada elemento de la variable
# el bucle for aplica la segunda fucion a cada variable
# ------------------------------------------------------------
aleatorio =[724, 18, 541, 92, 305, 617, 44, 883, 219, 560]
def aplicar_a_todos(funcion,lista):
    aplicados= []
    for x in lista:
        aplicados.append(funcion(x))
    return aplicados

def iva(valores):
    operacion=valores ** 2
    return operacion

print(aplicar_a_todos(iva, aleatorio))

# ------------------------------------------------------------
# EJERCICIO 2
# Crea una función llamada `contar_si` que reciba una lista
# y una función, y cuente cuántos elementos devuelven True
# al aplicarles la función.
#
# Pruébala dos veces:
#   - contando cuántos números son mayores que 100
#   - contando cuántos números son pares
#
# Pseudocódigo:
# crear una variable donde se almacene cada true
# crear funcion que tenga como parametro (funcion, lista)
# usar el bucle for para recorrer cada elemento de la lista
# aplicar la funcion a cada elemento
# si la condicion es true aumentar +1 al contador 
# retornar el contador 
# ------------------------------------------------------------
numero=[12, 45, 128, 7, 230, 89, 512, 33, 104, 61, 744, 19, 315, 94, 201]
def contar_si (funcion, lista):
    contador= 0
    for x in lista:
        if funcion(x):
            contador += 1
    return contador

def mayor_cien(numero):
    return numero > 100

def pares(numero):
    return numero %2 == 0

print(contar_si(mayor_cien,numero))
print(contar_si(pares,numero))
# ------------------------------------------------------------
# EJERCICIO 3
# Crea una función llamada `transformar_y_filtrar` que reciba
# una lista, una función de transformación y una función de filtro.
# Primero aplica la transformación a cada elemento,
# luego filtra los resultados que cumplan la condición.
# Devuelve la lista final.
#
# Pruébala: multiplica cada número por 3, luego quédate
# solo con los mayores que 50.

# Pseudocódigo:
# crear funcion que reciba (funcion_transformar, funcion_filtrar, lista)
# crear lista vacia "transformacion" para guardar los elementos modificados
# crear lista vacia "filtro" para guardar solo los elementos que cumplan la condicion
# bucle for sobre la lista original:
#     aplicar funcion_transformar a cada elemento y agregarlo a "transformacion"
# bucle for sobre "transformacion":
#     si funcion_filtrar(elemento) devuelve True:  ← aqui decide si entra o no con un if  
#         agregar elemento a "filtro"
# retornar "filtro"
# ------------------------------------------------------------
listilla=[48, 57, 32, 24, 31, 27, 15, 47, 49, 36, 13, 58, 46, 33, 19, 8, 59, 12, 48, 9]

def transformar_y_filtrar(funcion_transformar,funcion_filtrar, lista):
    trasformacion=[]
    filtro= []
    for x in lista:
        trasformacion.append(funcion_transformar(x))
    for y in trasformacion:
        if funcion_filtrar(y):
            filtro.append(y)
    return filtro 

def por_tres(numero):
    return numero * 3

def filtrado(numero):
    if numero > 50:
        return numero

print(transformar_y_filtrar(por_tres, filtrado, listilla))