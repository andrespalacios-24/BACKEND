from libro import Libro

#pseudocodigo
#crear funcion para guardar libros
#abrir el archivo biblioteca.txt en modo append asi no se borra el anterior con uno nuevo
#escribir el archivo con el .(a) donde incluya:
#escribir: libro.titulo, libro.autor, libro.anio separados por comas

def guardar_libro(texto):
    with open("biblioteca.txt","a") as book:
        book.write(f"{texto.titulo},{texto.autor},{texto.anio}\n")

#pseudocodigo
#crear funcion para leer los libros
#abrir el archivo biblioteca.txt en modo lectura
#con el bucle for hacer que se lea linea a linea
# crear lista vacía para guardar los objetos Libro
# por cada línea:
#     separar los valores por comas con el .split()
#     crear objeto Libro con esos valores
#     agregar a la lista
# retornar la lista

def leer_libro():
    try:
     with open ("biblioteca.txt", "r" ) as book:
        lista=[]
        for contenido in book:
          partes= contenido.strip().split(",") 
          objetos= Libro(partes[0],partes[1],partes[2])
          lista.append(objetos)
     return lista
    except FileNotFoundError:
       print ("el libro no existe aun")
       return[]

