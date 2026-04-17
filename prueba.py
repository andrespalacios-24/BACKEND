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