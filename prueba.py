listilla=[48, 57, 32, 24, 31, 27, 15, 47, 49, 36, 13, 58, 46, 33, 19, 8, 59, 12, 48, 9]

def transformar_y_filtrar(funcion_1,funcion_2, lista):
    trasformacion=[]
    filtro= []
    for x in lista:
        trasformacion.append(funcion_1(x))
    for y in trasformacion:
        if funcion_2(y):
            filtro.append(y)
    return filtro 

def por_tres(numero):
    return numero * 3

def filtrado(numero):
    if numero > 50:
        return numero

print(transformar_y_filtrar(por_tres, filtrado, listilla))