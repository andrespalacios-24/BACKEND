"""Ejercicio 2 — Calculadora de año de nacimiento
Pide al usuario su nombre y su edad. Calcula el año aproximado en que nació y muestra:
Andrés, probablemente naciste en el año 1999."""
nombre= input("cual es su nombre?")
edad= int(input("cuantos años tiene?"))
año_nacimiento= 2026 - edad
print (f"{nombre}, probablemente naciste en el año {año_nacimiento}")
""" Siempre se debe forzar el formato int() a la hora de usar numeros.
ya que al usar matematicas si no se fuerza a int() y esta en str() no 
podra hacer las funciones matematicas."""