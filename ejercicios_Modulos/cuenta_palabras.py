# 9. Crea un modulo que contenga una funcion para contar cuantes veces aparece una palabra en un texto. Escribe un programa que importe el modulo y lo use para contar palabras en una cadena.
def conteo(texto,palabra):
 frecuencia= texto.count(palabra)
 return frecuencia 