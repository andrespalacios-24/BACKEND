# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un numero entero que represente tu edad.
# height: un numero flotante que represente tu altura.
# Imprime cada variable en una linea separada.
name = "ANDRES"
age = 27
height = 1.76
print(name, age, height, sep="\n")
""" al imprimir hay 2 formas de que el texto quede en lineas individuales en el terminal
1. dandole print() en lineas separadas para cada terminal
2. usando sep="\n" al final de las variables en el print (como se hizo en el ejercicio)"""
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
age = 27
print ("cuantos años tienes" + " " + str(age) + "años")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_student= True
print ("es estudiante" + " " + str (is_student))
""" tambien se podia separar solo con una coma(,) ya que esta no mezcla variables
y asi no poner (+) que los concatena
pero no se tiene control sobre el formato del texto al usar (,)"""
# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
name= "ANDRES FELIPE PALACIOS VIVEROS"
print (len(name))
# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad= "andres", "palacios", "buga" # los valores en texto siempre entre comillas
print (nombre +" " + apellido + " " + ciudad) 
# usando f_string
print(f"Hola, soy {nombre} {apellido} y vivo en {ciudad}")
"""La f antes de las comillas le dice a Python que dentro del texto puede haber variables 
entre {}. Python las reemplaza automáticamente por sus valores.
El f-string produjo exactamente el mismo resultado que con +, 
pero el código queda mucho más limpio y fácil de leer."""
# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color= input ("color favorito")
print ("su color favorito es:", color) 
# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit= "banano"
print (fruit) 
fruit= "pera"
print (fruit) 
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price= 25.596
print (int(price)) 
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len= "carrera quince numero venticiete a catorce"
print (len(address_len))
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone= int(12345678)
print (type(phone))
phone= int(87654321)
print (type(phone))