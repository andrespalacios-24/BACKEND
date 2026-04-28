#registro
#crear funcion registro que contenga (usuario,operacion, monto)
#abrir el archivo historial.txt en modo append (a) asi no se sobre escribe encima de otro archivo
#debe incluir: usuario, operacion, monto
# 
import os
# os es un modulo de Python que permite interactuar con el sistema operativo
# en este caso lo usamos para manejar rutas de archivos

RUTA = os.path.join(os.path.dirname(__file__), "historial.txt")
# __file__      → es la ruta del archivo actual (historial.py)
# os.path.dirname → obtiene la carpeta donde vive ese archivo
# os.path.join  → une la carpeta con el nombre del archivo
# resultado: siempre crea historial.txt en la misma carpeta que historial.py
# sin importar desde donde ejecutes el programa

def registro (usuario, operacion, monto):
    with open(RUTA,"a") as h:
        h.write(f"{usuario},{operacion},{monto}\n")

#ver historial
#crear una funcion para leer los registros
#usar el try/except para manejar el error si no hay archivo creado que leer
#abrir el archivo historia.txt en modo (r)
#usar bucle for para que lea linea por linea

def lectura_registro():
    try:
        with open(RUTA,"r") as r:
            for historial in r:
                print(historial)
    except FileNotFoundError:
       print(("no hay registro del historial")) 
            
 




