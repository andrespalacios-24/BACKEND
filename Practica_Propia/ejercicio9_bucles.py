# ============================================================
# PRÁCTICA: BUCLES EN PYTHON
# Progresión de dificultad — intenta cada uno antes de ver la solución
# ============================================================


# ============================================================
# NIVEL 1 — Bucles básicos
# ============================================================

# Ejercicio 1
# Usa un bucle for con range() para imprimir los números del 1 al 20
# solo los que sean múltiplos de 3.
# Resultado esperado: 3, 6, 9, 12, 15, 18
for x in range (3, 20, 3): #se podria hacer con una condicional if si se pone
    print(x)               # range desde 0, 20, 3 con un if x >=3

# Ejercicio 2
# Usa un bucle while para contar cuántos números entre 1 y 50
# son divisibles por 5. Imprime el resultado al final.
# Resultado esperado: 10
contador= 0
numero = 1 
while numero <=50:
    if numero %5== 0:
        contador +=1
    numero +=1
print(contador)


# Ejercicio 3
# Dada esta lista de temperaturas:
# temperaturas = [22, 35, 18, 40, 29, 15, 38]
# Usa un bucle for para encontrar e imprimir la primera temperatura
# que supere los 30 grados. Detén el bucle al encontrarla.
# Resultado esperado: 35

temperaturas = [22, 35, 18, 40, 29, 15, 38]
for temp in temperaturas: # se pone un nombre a la variable diferente a la de la lista
    if temp >30:          # este es el nombre de la variable donde estara el bucle
        print(temp) #se imprime temp que es donde se almacena la variable
        break


# ============================================================
# NIVEL 2 — Acumuladores y contadores
# ============================================================

# Ejercicio 4
# Dada esta lista de ventas diarias:
# ventas = [120, 85, 200, 95, 310, 60, 175]
# Usa un bucle for para calcular:
# - El total de ventas
# - Cuántos días superaron los 100
# Imprime ambos resultados al final.

ventas = [120, 85, 200, 95, 310, 60, 175]
total_ventas=0
venta_superior=0
for venta in ventas:
    total_ventas +=venta
    if venta >100:
        venta_superior +=1
print(f"ventas totales: {total_ventas} || total ventas que superaron 100: {venta_superior}")

# Ejercicio 5
# Dada esta cadena: "backend developer python 2024"
# Usa un bucle for para contar cuántas vocales tiene.
# Pista: puedes comparar cada carácter con "aeiou"
# Resultado esperado: 7
cadena= "backend developer python 2024"
vocales=0
for vocal in cadena:
 if vocal in "aeiou":
  vocales +=1

print(vocales)


# Ejercicio 6
# Usa un bucle while para encontrar el primer número entre 1 y 200
# que sea divisible tanto por 6 como por 8.
# Pista: usa el operador % con ambas condiciones y el operador and
# Resultado esperado: 24
primer_numero = 1  # empieza en 1, no en 0, porque 0 cumple la condición y detendría el bucle antes de buscar

while primer_numero <= 200:
    if primer_numero % 6 == 0 and primer_numero % 8 == 0:  # ambas condiciones deben cumplirse con 'and'
        print(primer_numero)
        break  # detiene el bucle al encontrar el primer número
    
    primer_numero += 1  # va fuera del if para subir en cada vuelta, no solo cuando cumple la condición

# ============================================================
# NIVEL 3 — Listas y diccionarios con bucles
# ============================================================

# Ejercicio 7
# Tienes esta lista de usuarios registrados en una API:
# usuarios = ["ana", "luis", "maria", "ana", "pedro", "luis", "ana"]
# Usa un bucle for para contar cuántas veces aparece cada nombre.
# Guarda los resultados en un diccionario y muéstralo al final.
# Resultado esperado: {"ana": 3, "luis": 2, "maria": 1, "pedro": 1}

usuarios = ["ana", "luis", "maria", "ana", "pedro", "luis", "ana"]
resultado= {}
for usuario in usuarios:
    if usuario in resultado:
        resultado[usuario] +=1
        
    else:
     resultado[usuario]=1

print(resultado)

# Ejercicio 8
# Tienes este diccionario con productos y sus precios:
# productos = {"laptop": 1200, "mouse": 25, "teclado": 80, "monitor": 350, "auriculares": 60}
# Usa un bucle for para:
# - Imprimir solo los productos que cuesten más de 100
# - Calcular el precio total de esos productos
# Imprime el total al final.
productos = {"laptop": 1200, "mouse": 25, "teclado": 80, "monitor": 350, "auriculares": 60}

precio_total=0
for items in productos:
    if (productos[items]) >100:
     print(items)
     precio_total+=(productos[items])

print(precio_total)

# ============================================================
# NIVEL 4 — Lógica backend real
# ============================================================

# Ejercicio 9
# Tienes esta lista de logs de un servidor:
# logs = ["OK", "ERROR", "OK", "OK", "ERROR", "ERROR", "OK", "ERROR"]
# Usa un bucle for para:
# - Contar cuántos "OK" y cuántos "ERROR" hay
# - Si hay más de 3 errores, imprime "ALERTA: demasiados errores"
# - Si no, imprime "Sistema estable"

logs = ["OK", "ERROR", "OK", "OK", "ERROR", "ERROR", "OK", "ERROR"]
estable=0
alerta=0
for intentos in logs:
    if "OK" in intentos:
        estable+=1
    else:
        alerta+=1   

if alerta>3:
    print("ALERTA: demasiados errores")  #se pueden hacer if/else fuera de bucles para 
else:                                    #continuar con otra condicion
    print("Sistema estable")


# Ejercicio 10
# Tienes esta lista de intentos de login con su resultado:
# intentos = [
#     {"usuario": "ana", "exitoso": True},
#     {"usuario": "luis", "exitoso": False},
#     {"usuario": "ana", "exitoso": False},
#     {"usuario": "pedro", "exitoso": True},
#     {"usuario": "luis", "exitoso": False},
#     {"usuario": "luis", "exitoso": False},
# ]
# Usa un bucle for para:
# - Contar los intentos fallidos por usuario
# - Imprimir los usuarios que tengan 2 o más intentos fallidos (posible ataque)
# Resultado esperado: luis tiene 3 intentos fallidos — ALERTA