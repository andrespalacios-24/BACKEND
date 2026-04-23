# 8. Crea un modulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de numeros. Usa este modulo para calcular estos valores en una lista dada.
def media(lista):
  resultado=  sum(lista)/ len(lista)
  return resultado


def mediana(lista):
  lista.sort()
  if len(lista) % 2 ==0:



