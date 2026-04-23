# 7. Escribe un modulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

def escribir(texto):
 with open("escritura.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto)

def leer():
  with open ("escritura.txt","r", encoding= "utf-8") as archivo:
    contenido= archivo.read()
    print(contenido)
