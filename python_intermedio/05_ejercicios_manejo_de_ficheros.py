# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".

archivo_texto = open("nuevo.txt", "w+")
archivo_texto.write("Hola desde Python")
archivo_texto.close()

with open("texto.txt","w+") as archivo_con_withOpen:
    archivo_con_withOpen.write("hola, desde python")
#forma con with open, la mejor forma porque cierra automatica

# 2. Abre un archivo y lee todo su contenido.

with open("python_intermedio/nuevo.txt", "r") as archivo:
    print(archivo.read()) 
# se debe especificar la ruta relativa desde donde corre Python (cwd)

# 3. Añade una nueva línea al final del archivo con el texto "Línea añadida".

with open("python_intermedio/nuevo.txt", "a") as archivo:
    archivo.write("\nLínea añadida")

# 4. Lee solo los primeros 10 caracteres del archivo.

with open("python_intermedio/nuevo.txt", "r") as archivo:
    print(archivo.read(10)) 

# 5. Usa seek para volver al inicio del archivo y leer desde ahí.

with open("python_intermedio/nuevo.txt", "r") as archivo:
    archivo.seek(0)
    print(archivo.read()) 

# 6. Lee e imprime el contenido línea por línea usando readline.

with open("python_intermedio/nuevo.txt", "r") as archivo:
    print(archivo.readline().strip()) 
    print(archivo.readline().strip()) 
# el .strip() es para que en la consola no aparezca un espacio entre lineas

# 7. Lee todas las líneas del archivo en una lista y recórrelas con un bucle.

with open("python_intermedio/nuevo.txt", "r") as archivo:
    for  linea in archivo.readlines():
        print(linea.strip())

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias líneas.

with open("python_intermedio/nuevo_1.txt", "w") as archivo:
    archivo.write("sera que funciona?\n")
    archivo.write("o sera que sobre escribe todo")

# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.

def abrir_cerrar_archivo(archivo):
    with open(archivo,"w") as archivo_con_withOpen:
        archivo_con_withOpen.write("hola, desde python")


print(abrir_cerrar_archivo("segundo.txt"))

# 10. Lee un archivo línea por línea y muestra solo las que contienen la palabra "Python".
with open("/home/andres/BACKEND/segundo.txt", "r") as archivo:
    for linea in archivo:
        if "python" in linea.lower(): #ya que python es sensible a mayusculas se pone .lower()
            print(linea)