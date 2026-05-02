 # 1. Crea una lambda que sume dos numeros.

suma= lambda numero_1, numero_2: numero_1 + numero_2
print(suma(5,5))

# 2. Crea una lambda que calcule el cuadrado de un numero.

cuadrado=lambda numero: numero**2
print(cuadrado(3))

# 3. Crea una lambda que devuelva el mayor de dos numeros.

mayor= lambda numero_1, numero_2: max(numero_1,numero_2)
print(mayor(4434,523543))

# 4. Crea una lambda que sume 10 a un numero dado.

suma_diez= lambda numero: numero +10
print(suma_diez(5)) 

# 5. Crea una lambda que devuelva el ultimo caracter de una cadena.

ultimo_caracter= lambda str: str[-1]
print(ultimo_caracter("gatito"))

# 6. Crea una lambda que indique si una palabra tiene mas de 6 letras.

mas_De_seis= lambda palabra: "Mas de 6 letras" if len(palabra) > 6 else "Menos de 6 letras"
print(mas_De_seis("asdfg"))

# 7. Crea una lambda que convierta una cadena a minusculas.

minuscula= lambda palabra: palabra.lower()
print(minuscula("ENTONCES MI PAPA"))

# 8. Crea una lambda que devuelva True si un numero es positivo.

positivo= lambda numero: True if numero >0 else False
print(positivo(0)) 

# 9. Crea una lambda que devuelva "Cadena vaci­a" si el string esta vaci­o.

vacio= lambda cadena: "cadena vacia" if len(cadena.strip()) == 0 else cadena
print(vacio(" "))

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.

precio_iva= lambda precio: precio + (precio*0.21)
print(precio_iva(100))