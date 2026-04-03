# 1. Crea un set con los numeros del 1 al 5 e imprimelo.
my_set= {1, 2, 3, 4, 5}
print(my_set)
# 2. Añade el numero 6 al set {1, 2, 3, 4, 5} e impri­melo.
my_set= {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
# 3. Intenta añadir el numero 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Que sucede?
my_set= {1, 2, 3, 4, 5}
my_set.add(5)
print(my_set) #no pasa nada porque set no tiene en cuenta los numeros repetidos.
# 4. Verifica si el numero 3 esta en el set {1, 2, 3, 4, 5} e imprime el resultado.
my_set= {1, 2, 3, 4, 5}
print(3 in my_set) # al poner numeros no usar "" porque lo toma como texto y no lo va a encontrar
# 5. Elimina el numero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set= {1, 2, 3, 4, 5}
my_set.remove(4)
print(my_set)
# 6. Usa el metodo clear() para vaciar un set y luego imprime su longitud.
my_set= {1, 2, 3, 4, 5, 6}
my_set.clear()
print(len(my_set))
# 7. Convierte el set {"manzana", "naranja", "platano"} en una lista e imprime el primer elemento de la lista.
my_set= {"manzana", "naranja", "platano"}
set_list= list(my_set)
print(set_list[0])
# 8. Realiza la union de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set_1= {1, 2, 3}
set_2= {4, 5, 6}
print(set_1.union(set_2))
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set_1= {1, 2, 3, 4}
set_2={3, 4, 5, 6}
print(set_1.difference(set_2))
print(set_2.difference(set_1))
"""al hacer la diferencia entre sets, tener en cuenta que el set que se ponga de primero
es al que se le buscara la diferencia respecto al otro set con el que se compara"""
# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
set_eliminado= {1, 2, 3, 4, 5, 6}
del set_eliminado
#print(set_eliminado)