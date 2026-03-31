"""Ejercicio 4 — Conversor de moneda Pide al usuario una cantidad en pesos colombianos y muestra su equivalente en dólares. 
Usa una tasa de cambio fija de $4200 pesos por dólar."""
tasa_fija= 4200
peso_colombiano= float(input("valor en pesos a convertir?"))
dollar= round(peso_colombiano / tasa_fija, 2)
print (f"{peso_colombiano} pesos colombianos equivalen a ${dollar} dolares")

"""al hacer conversiones forzar decimales con float() de esa manera coge toda
la cifra de la conversion"""
"""se pueden redondear los decimales para que no sea muy largo.
existen 2 formas:
- en la operacion: dollar = round(peso_colombiano / tasa_fija, 2)
- en el print: print(f"{peso_colombiano} pesos equivalen a ${round(dollar, 2)} dólares") """