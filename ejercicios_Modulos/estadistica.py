# 8. Crea un modulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de numeros. Usa este modulo para calcular estos valores en una lista dada.
def media(lista):
  resultado=  sum(lista)/ len(lista)
  return resultado
 

def mediana(lista):
  datos_ordenados = sorted(lista)
  n= len(datos_ordenados)
  mitad= n // 2
  if n %2 == 0:
    return (datos_ordenados[mitad -1] + datos_ordenados[mitad]) /2
  else:
    return datos_ordenados[mitad] 


