# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprimela.
tupla= (10, 20, 30, 40, 50)
print(tupla)
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muestralo.
tupla=(100, 200, 300, 400, 500)
print(tupla[1])
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tupla=(1, 2, 3)
# tupla[0]= 10
#print(tupla) dara: (TypeError: 'tuple' object does not support item assignment) que significa que es algo que no se modifica
# 4. Cuenta cuantas veces aparece el numero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
tupla=(1, 2, 3, 3, 4, 5, 3)
print(tupla.count(3))
# 5. Encuentra el i­ndice de la primera aparicion de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
tupla= ("Java", "Python", "JavaScript", "Python")
print(tupla.index("Python"))
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla_1= (1, 2, 3)
tupla_2=(4, 5, 6)
tupla_x2= tupla_1 + tupla_2
print(tupla_x2)
# 7. Crea una subtupla con los elementos desde la posicion 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
tupla=(10, 20, 30, 40, 50)
sub_tupla= tupla[2:4]
print(sub_tupla)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tupla= ("rojo", "verde", "azul")
lista= list(tupla)
lista[1]= "amarillo"
tupla= tuple(lista)
print(tupla)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple= (1, 2, 3, 4)
#del my_tuple #no lleva parentesis porque es una variable creada no un elemento o palabra
#print(my_tuple)
# 10. Crea una tupla con un solo elemento (el numero 100) e imprimela. Asegurate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tupla=(100,) #si es un solo elemento se debe poner coma para que lo interprete como una tupla no como un entero int()
print(tupla)