"""
PROYECTO 1 — Organizador de archivos por extensión
====================================================
Mueve archivos de una carpeta origen a subcarpetas organizadas por extensión.
Ejemplo: foto.jpg  ->  origen/imagenes/foto.jpg
         datos.csv ->  origen/csv/datos.csv

Módulos que vas a necesitar:
    - os        : listar archivos, crear carpetas, mover archivos
    - pathlib   : (opcional pero recomendado) manejo de rutas más limpio que os.path
    - shutil    : mover archivos de un lugar a otro

Flujo general del programa:
    1. Definir la carpeta a organizar
    2. Listar todos los archivos que hay en ella
    3. Por cada archivo, obtener su extensión
    4. Crear la subcarpeta de esa extensión si no existe
    5. Mover el archivo a la subcarpeta correspondiente
    6. Mostrar un resumen al final
"""

import os
import shutil
from pathlib import Path 

# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────────

# Carpeta que se va a organizar.
# Pista: usa os.path.join o una ruta absoluta para que funcione desde cualquier lugar.
CARPETA_ORIGEN = "/home/andres/prueba_organizador"  # TODO: define la ruta aquí


# ── FUNCIONES ──────────────────────────────────────────────────────────────────

def obtener_extension(nombre_archivo):
    """
    Recibe el nombre de un archivo y retorna su extensión en minúsculas,
    sin el punto. Ejemplo: "foto.JPG" -> "jpg"

    Pista: os.path.splitext() separa nombre y extensión.
    Si el archivo no tiene extensión, retorna "sin_extension".
    """
    # TODO: 
    extension= Path(nombre_archivo).suffix[1:].lower()
    if extension == "":
        return "sin_extension"
    else:
        return extension
    


def crear_carpeta_si_no_existe(ruta_carpeta):
    """
    Recibe una ruta y crea la carpeta si no existe todavía.
    Si ya existe, no hace nada (no lanza error).

    Pista: os.makedirs() tiene un parámetro útil para esto.
    """
    # TODO: 
    nueva_carpeta= Path(ruta_carpeta)
    nueva_carpeta.mkdir(parents=True, exist_ok= True)
   


def organizar_carpeta(carpeta_origen):
    """
    Función principal. Recorre todos los archivos de carpeta_origen
    y los mueve a subcarpetas según su extensión.

    Pasos sugeridos:
        1. Verificar que carpeta_origen existe (si no, mostrar error y salir)
        2. Listar el contenido con os.listdir()
        3. Filtrar solo los archivos (no carpetas) con os.path.isfile()
        4. Para cada archivo:
            a. Obtener su extensión
            b. Construir la ruta de la subcarpeta destino
            c. Crear la subcarpeta si no existe
            d. Mover el archivo con shutil.move()
            e. Imprimir qué archivo se movió y a dónde
        5. Al final, imprimir cuántos archivos se procesaron
    """
    # TODO: 
    ruta= Path(carpeta_origen)
    archivos_procesados= 0
    if ruta.exists():
        print("La carpeta (o archivo) existe en el sistema.")
        for elemento in ruta.iterdir():
            if elemento.is_file():
             extension= obtener_extension(elemento)
             ruta_subcarpeta = Path(ruta) / extension
             crear_carpeta_si_no_existe(ruta_subcarpeta)
             shutil.move(elemento,ruta_subcarpeta)
             archivos_procesados +=1
             print(f"Movido con éxito: {elemento} -> {ruta_subcarpeta}")
        print(f"total de archivos procesados:{archivos_procesados}")
    else:
        print("La carpeta (o archivo) NO existe en el sistema.")
        return


# ── PUNTO DE ENTRADA ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    organizar_carpeta(CARPETA_ORIGEN)



#------------------------------------------------------------------------------------------
#CAMBIOS QUE HIZO CLAUDE CON RESPECTO AL QUE HICE YO (COMENTADO)
#------------------------------------------------------------------------------------------
"""
Organizador de archivos por extensión — versión comentada
==========================================================
Esta es la versión de estudio. La versión limpia para portafolio
está en proyecto_portafolio/etapa1/organizador_archivos.py
"""

import os
import shutil
from pathlib import Path


CARPETA_ORIGEN = "/home/andres/prueba_organizador"


def obtener_extension(nombre_archivo):
    """Retorna la extensión del archivo en minúsculas y sin punto.
    Si no tiene extensión retorna 'sin_extension'."""

    extension = Path(nombre_archivo).suffix[1:].lower()

    # CAMBIO: el if/else original funcionaba bien pero se puede simplificar
    # con un operador ternario en una sola línea.
    #
    # Tu versión original:
    #   if extension == "":
    #       return "sin_extension"
    #   else:
    #       return extension
    #
    # Versión limpia equivalente:
    return extension if extension else "sin_extension"
    # Lectura: "retorna extension si extension no está vacía, si no retorna 'sin_extension'"
    # Una string vacía "" es falsy en Python, por eso no necesitas comparar con "".


def crear_carpeta_si_no_existe(ruta_carpeta):
    """Crea la carpeta si no existe. Si ya existe, no hace nada."""

    # CAMBIO: tu versión creaba una variable intermedia innecesaria.
    #
    # Tu versión original:
    #   nueva_carpeta = Path(ruta_carpeta)
    #   nueva_carpeta.mkdir(parents=True, exist_ok=True)
    #
    # Versión limpia — se puede hacer en una sola línea:
    Path(ruta_carpeta).mkdir(parents=True, exist_ok=True)


def organizar_carpeta(carpeta_origen):
    """Recorre la carpeta origen y mueve cada archivo a una subcarpeta
    según su extensión."""

    ruta = Path(carpeta_origen)

    # CAMBIO: tu versión usaba if ruta.exists() y metía todo el trabajo adentro.
    # El patrón estándar en backend es validar primero con "if not" y salir
    # temprano (early return). Esto evita un nivel de indentación innecesario
    # y deja el flujo principal del código al mismo nivel.
    #
    # Tu versión original:
    #   if ruta.exists():
    #       print("La carpeta existe...")
    #       for elemento in ruta.iterdir():
    #           ...
    #   else:
    #       print("No existe")
    #       return
    #
    # Versión limpia con early return:
    if not ruta.exists():
        print(f"Error: la carpeta '{carpeta_origen}' no existe.")
        return
    # Si llega aquí, la carpeta existe. Todo el trabajo va al mismo nivel,
    # sin estar anidado dentro de un if.

    archivos_procesados = 0

    for elemento in ruta.iterdir():
        if elemento.is_file():
            extension = obtener_extension(elemento)
            ruta_subcarpeta = ruta / extension
            crear_carpeta_si_no_existe(ruta_subcarpeta)
            shutil.move(elemento, ruta_subcarpeta)
            archivos_procesados += 1

            # CAMBIO: en tu versión imprimías la ruta completa del archivo.
            # elemento.name retorna solo el nombre del archivo, más legible.
            #
            # Tu versión: print(f"Movido con éxito: {elemento} -> {ruta_subcarpeta}")
            # Versión limpia: 
            print(f"Movido: {elemento.name} -> {ruta_subcarpeta}/")

    print(f"\nTotal de archivos procesados: {archivos_procesados}")
    # CAMBIO menor: se agregó \n antes del total para separarlo visualmente
    # de la lista de archivos movidos.


if __name__ == "__main__":
    organizar_carpeta(CARPETA_ORIGEN)
