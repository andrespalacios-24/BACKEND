#crear clase Libro
# crear los atributos: titulo, autor, año
# crear metodo constructor init:
#- self.titulo, self.autor, self.año
#crear metodo __str__ con lo que mostrara el imprimir: titulo,autor,año
# escribir las variables del atributo


class Libro:
    def __init__(self, titulo, autor,anio):
        self.titulo=titulo
        self.autor= autor
        self.anio=anio
        
        
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.anio}"
