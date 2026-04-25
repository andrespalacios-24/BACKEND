from estudiantes import Estudiante
from estadistica import media, mediana

# IMPORTS: estudiante.py y estadisticas.py

# crear variable estudiante_1 con su nombre (instancia de Estudiante)
# crear variable estudiante_2 con su nombre
# crear variable estudiante_3 con su nombre

# agregar notas a cada estudiante con try/except:
#   try: estudiante_1.agregar_notas(nota)
#   except ValueError: mostrar mensaje de error

# obtener promedio individual de cada estudiante con .promedio_notas()
# guardar cada promedio en una variable

# crear lista con los tres promedios juntos
# usar media() y mediana() de estadisticas.py con esa lista

# mostrar resultados

estudiante_1=Estudiante("maikel manue")
estudiante_2=Estudiante("jorge the corious")
estudiante_3=Estudiante("kiyo zaki")

try:
    estudiante_1.agregar_notas(1)
    estudiante_1.agregar_notas(8)
    estudiante_1.agregar_notas(6) 
    
except ValueError as error:
    print(error) 

try:
    estudiante_2.agregar_notas(7)
    estudiante_2.agregar_notas(5)
    estudiante_2.agregar_notas(2)
except ValueError as error:
    print(error) 

try:
    estudiante_3.agregar_notas(9)
    estudiante_3.agregar_notas(18)
    estudiante_3.agregar_notas(6)
except ValueError as error:
    print(error) 

promedio_estudiante_1=estudiante_1.promedio_notas()

promedio_estudiante_2=estudiante_2.promedio_notas()

promedio_estudiante_3=estudiante_3.promedio_notas()

lista_promedios_totales=[promedio_estudiante_1, promedio_estudiante_2, promedio_estudiante_3]


print(media(lista_promedios_totales))
print(mediana(lista_promedios_totales))