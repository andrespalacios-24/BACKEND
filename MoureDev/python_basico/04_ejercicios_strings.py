# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text= "aprendiendo python"
print(len(text))
# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola li­nea.
print("hola " + "Python" )
# 3. Crea una cadena que incluya un salto de linea, y luego impri­mela para ver el resultado.
salto= "hola como estan\nme imagino que muy bien"
print (salto)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre="ANDRES"
apellido= "PALACIOS"
edad= 28
print(F"{nombre} {apellido} {edad}" ) #Si se ponen espacios entre los corchetes al imprimir sale con los espacios
# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego impre­melos uno por uno.
palabra= "python"
a, b, c, d, e, f= palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# 6. Extrae un "slice" de la palabra "Programacion" para obtener los caracteres desde la posicion 3 hasta la 7.
palabra="programacion"
palabra_slice= palabra[3:7]
print(palabra_slice)
# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
revertir= palabra[::-1]
print(revertir)
# 8. Convierte la cadena "aprendiendo python" en mayusculas usando el metodo adecuado e imprimela.
print(palabra.upper()) #despues del .upper se debe poner () queda: .upper()
# 9. Cuenta cuantas veces aparece la letra "n" en la cadena "Programacion en Python".
numero_de_veces="programacion en python" 
print(numero_de_veces.count("n")) #la letra debe ir con "" si no, no las cuenta
# 10. Verifica si la cadena "12345" es numerica usando el metodo adecuado e imprime el resultado.
cadena= "12345"
print(cadena.isnumeric())