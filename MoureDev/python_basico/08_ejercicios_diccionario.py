# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
datos= {"name": "ANDRES", "age": 28, "country": "COLOMBIA",} #al poner {} python entiende que es un diccionario
print(datos)
# 2. Accede al valor de la clave name en el diccionario.
print(datos["name"])
# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
datos["job"] = "Programador"
print(datos)
# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
datos["age"]= 38
print(datos)
# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del datos["country"]
print(datos)
# 6. Crea un diccionario donde las claves sean numeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
numericos= {1:1,  2: 4,  3: 9, 4: 16, 5: 25}
print(numericos)
# 7. Verifica si la clave age esta presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
datos=  {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in datos) 
# 8. Imprime solo las claves del diccionario.
print(datos.keys()) # al final de key poner el () para que funcione
# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
lista= list(datos)
print(lista)
# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
lista= ["name", "age", "job"]
dic_lista= dict.fromkeys(lista, "desconocido")
print(dic_lista)