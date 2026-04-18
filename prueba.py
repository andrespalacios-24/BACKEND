# ------------------------------------------------------------
# EJERCICIO 5 - Resumen de ventas (for + range() + función)
# ------------------------------------------------------------
# Tienes una lista de ventas diarias (números).
# Necesitas calcular el total, el promedio y la venta máxima.
# Esto simula un endpoint de reportes.
#
# Requisitos:
# - Crea una función que reciba la lista de ventas.
# - Recórrela con for (puedes usar range() o directo).
# - Retorna un diccionario con: total, promedio, maximo.
# - Imprime el resultado formateado con f-string.

ventas = [120, 340, 89, 456, 230, 178, 95]

def resumen_ventas(ventas):
   total= 0                 #las listas en 0 deben queda dentro de la funcion pero
   promedio= 0              # fuera del bucle en este caso for
   maximo= 0
   for venta in ventas:
    total += venta
   maximo= max(ventas) 
   promedio= round (total / len(ventas),2) #le puse round para que lo redondeara a 2 decimales
   return{
    "total":total,
    "promedio": promedio, 
    "maximo": maximo
   }
resultado= resumen_ventas(ventas) #esto se hace para que se procese la lista y devuelva el 
                                  # diccionario que tenemos dentro de la funcion (lo hace internamente)
print(f"total de ventas:{resultado["total"]} | promedio de ventas:{resultado["promedio"]} | venta maxima:{resultado["maximo"]}")

   
    
 




