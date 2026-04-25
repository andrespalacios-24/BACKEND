# CLASE Estudiante:
#   ATRIBUTOS:
# nombre del estudiante y notas[]
#   METODO __init__:
#    self.estudiante y self.nota[]
# METODO agregar_nota(nota):
#  se agrega primero la excepcion personalizada:
# con el if raise donde la nota no puede ser menor que 0 ni mayor que 10
# si esta dentro del rago que retorne la nota a la lista
#si no esta en el rago que lance el error personalizado que la nota no esta en los rangos
# METODO promedio():
#   se lanza primero un if para verificar si hay algo que promediar o lanza un error
#con el raise lanzo el error personalizado no hay notas para promediar 

class Estudiante:
    def __init__(self,alumno):
        self.alumno=alumno
        self.nota=[]
        
    def agregar_notas(self,nota):
        if nota < 0 or nota > 10:
            raise ValueError("la nota no esta en los rangos aceptados")
        self.nota.append(nota)
    
    def promedio_notas(self):
        if len(self.nota) == 0:
            raise ValueError("no hay notas para promediar")
        return sum(self.nota) / len(self.nota)
