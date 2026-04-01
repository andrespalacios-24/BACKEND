"""Ejercicio 5 — Calculadora de promedio Pide al usuario 4 notas de un estudiante. 
Calcula el promedio y muestra si el estudiante aprobó o reprobó (el mínimo para aprobar es 3.0)."""
""" Nota 1: 4.5
Nota 2: 3.2
Nota 3: 2.8
Nota 4: 3.9
-----------------
Promedio: 3.6
Resultado: Aprobado ✓"""
# Conceptos: input(), float(), división, f-strings.
nota_1= float(input("nota 1:"))
nota_2= float(input("nota 2:"))
nota_3= float(input("nota 3:"))
nota_4= float(input("nota 4:"))
numero_de_notas= 4
promedio_estudiante= (nota_1 + nota_2 + nota_3 + nota_4) / numero_de_notas
print(f"nota 1: {nota_1}")
print(f"nota 2: {nota_2}")
print(f"nota 3: {nota_3}")
print(f"nota 4: {nota_4}")
print ("-----------------------")
print (f"promedio: {promedio_estudiante}")
