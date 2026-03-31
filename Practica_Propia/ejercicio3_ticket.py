"""Ejercicio 3 — Ticket de compra Pide al usuario 3 precios de productos distintos.
 Calcula el total y muestra un resumen así: Producto 1: $5000
Producto 2: $3200
Producto 3: $8100
-----------------
Total: $16300"""
producto_1= int(input("defina el costo del primer producto"))
producto_2= int(input("defina el costo del segundo producto"))
producto_3= int(input("defina el costo del tercer producto"))
costo_total= producto_1 + producto_2 + producto_3
print (f"producto 1:${producto_1}")
print(f"producto 2: ${producto_2}")
print(f"producto 3: ${producto_3}")
print ("---------------------------")
print (f"TOTAL: ${costo_total}") 
"""recordar que para poder sumar toca forzar el formato a
int() """  