# 10. Lee un archivo línea por línea y muestra solo las que contienen la palabra "Python".
with open("/home/andres/BACKEND/segundo.txt", "r") as archivo:
    for linea in archivo:
        if "python" in linea.lower(): #ya que python es sensible a mayusculas se pone .lower()
            print(linea)
        