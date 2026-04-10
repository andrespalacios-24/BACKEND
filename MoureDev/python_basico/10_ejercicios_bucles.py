# 1. Usa un bucle while para imprimir los numeros del 1 al 10.
condicion= 0
while condicion <= 10:
    print(condicion)
    condicion +=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada numero.
lista= [10, 20, 30, 40, 50]   #se usa for para recorrer listas.
for recorrer in lista:  #la palabra recorrer puede ser cualquier palabra, la condicion es que este igual en el print
    print(recorrer)

# 3. Escribe un programa que use un bucle while para sumar los numeros del 1 al 100 e imprime el resultado.
condicion= 0
total_suma= 0
while condicion <=100:
    total_suma += condicion  # total_suma += condicion va primero: así sumamos el valor actual antes de incrementarlo.
    condicion +=1            # Si incrementamos primero, sumamos el número siguiente, no el actual.
  #la suma correcta es 5050, si invertimos el orden de la condicion dara 5151   

print(total_suma)
 
# 4. Escribe un bucle for que imprima cada caracter de la cadena "Python".
cadena= "Python"
for recorrer in cadena:
    print(recorrer)
# 5. Usa un bucle while para encontrar el primer numero divisible por 7 entre 1 y 50.
numero = 1
while numero <= 50:
    if numero % 7 == 0:
        print(numero)  # imprime el primero divisible por 7
        break          # detiene el bucle inmediatamente despues de encontrarlo
    numero += 1        # solo incrementa si NO es divisible, avanza al siguiente

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
# "elemento" toma el valor de cada clave en cada vuelta
diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}
for elemento in diccionario:
    print(elemento)  # imprime las claves: name, age, country

# Para imprimir valores: diccionario[elemento] usa la clave variable para acceder al valor
for elemento in diccionario:
    print(diccionario[elemento])  # imprime: Brais, 37, Galicia

# 7. Escribe un programa que use un bucle while para imprimir los numeros pares entre 1 y 20.
numero= 1
while numero <=20:
    if numero %2 == 0:
        print(numero)
    numero +=1
    
# 8. Usa un bucle for con la funcion range() para imprimir los numeros del 1 al 10 en orden inverso.
for x in range(10, 0, -1):
    print(x)
# 9. Escribe un programa que use un bucle for para contar cuantas veces aparece el numero 30 en la lista[30, 10, 30, 20, 30, 40].
lista= [30, 10, 30, 20, 30, 40]
numero_de_repetidos= 0
for n in lista:
    if n ==30:
       
        numero_de_repetidos +=1
        
        
print(numero_de_repetidos)


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = [
    "Alex", "Beatriz", "Carla", "Daniel", "Elena", 
    "Fernando", "Gabriela", "Héctor", "Isabel", "Jorge", 
    "Kevin", "Laura", "Brais", "Marta", "Nico"]

for nombre in nombres:
    if nombre == "Brais": #verificar las mayusculas ya que para python son variables distintas ej: brais y Brais
        break

    print(nombre)
