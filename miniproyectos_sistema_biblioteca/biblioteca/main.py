from libro import Libro
from almacen import guardar_libro, leer_libro

libro_1=Libro ("Cien años de soledad", "Gabriel García Márquez", 1967)
libro_2=Libro ("El principito", "Antoine de Saint-Exupéry", 1943)
libro_3=Libro ("1984", "George Orwell", 1949)



guardar_libro(libro_1)
guardar_libro(libro_2)
guardar_libro(libro_3)

lectura_1= leer_libro()
for x in lectura_1:
    print(x)
