#crear una  funcion media donde de la lista se tome:
# la suma de toda la lista sum() y el total de elementos de la lista len() y se divida la suma entre el numero
#
#crear una funcion mediana 
#donde primero se ordenen los datos con sorted
#y se cree una variable ya con los datos ordenados 
# se cuentan el numero de elementos dentro de la lista con len 
# se crea variable donde se tomen los datos y se dividan entre 2 llamada mitad
#con un if se crea una condicional donde se tomen el numero de datos y se le saque el residuo de 2 
#si el valor es igual a 0 es par entonces toca hacer la operacion para numeros pares(ya descrita en otro ejercicio)
#si no con else se retorna la mitad 

def media(notas):
  resultado=  sum(notas)/ len(notas)
  return resultado
 

def mediana(notas):
  datos_ordenados = sorted(notas)
  n= len(datos_ordenados)
  mitad= n // 2
  if n %2 == 0:
    return (datos_ordenados[mitad -1] + datos_ordenados[mitad]) /2
  else:
    return datos_ordenados[mitad] 