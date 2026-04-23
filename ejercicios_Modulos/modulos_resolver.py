# 1. Crea un modulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos numeros. Importa este modulo en otro archivo y usa sus funciones.

from calculator import sumValue, restValue, divValue, multiplyValue

print (sumValue(3444554,3232323))

print(restValue(13234454,55645))

print(divValue(2343,5))

print(multiplyValue(333,5656))

# 2. Crea un modulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este modulo y realice conversiones.

from converter import celsius, fahrenheit
print(celsius(32))
print(fahrenheit(32))

# 3. Crea un modulo que contenga una lista de nombres de estudiantes y una funcion que imprima todos los nombres. Importa este modulo en otro archivo y usa la funcion para mostrar la lista.

from lista import lista, estudiantes
lista(estudiantes)

# 4. Crea un modulo llamado "geometry" que tenga una funcion para calcular el area de un ci­rculo y un cuadrado. Usa este modulo en otro archivo para calcular areas.

from geometry import area_circulo_radio, area_circulo_diametro, area_cuadrado
print (area_cuadrado(3))
print (area_circulo_diametro(3))
print (area_circulo_radio(3))
# 5. Escribe un modulo que contenga una funcion que acepte cualquier numero de argumentos y devuelva su suma. Importa y usa la funcion en otro archivo.

from sumaArgs import suma_argumentos
print (suma_argumentos(1,1,1,1,1,1,1,1,1,1))

# 6. Crea un modulo que defina una clase llamada "Car" con propiedades como marca, modelo y año Importa este modulo en otro archivo y crea una instancia de la clase "Car".

from car import Car
carro= Car("ford", "fiesta rs", "2018")
print(f"carro marca: {carro.marca}, modelo: {carro.modelo} del año: {carro.año}")

# 7. Escribe un modulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

from lectur_escritura import leer, escribir
escribir("hola mis socios ") #este crea un archivo txt que se vera en las carpetas .py
leer() #similar a un print pero no lo  es   




# 8. Crea un modulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de numeros. Usa este modulo para calcular estos valores en una lista dada.

# 9. Crea un modulo que contenga una funcion para contar cuantes veces aparece una palabra en un texto. Escribe un programa que importe el modulo y lo use para contar palabras en una cadena.

# 10 Crea un modulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este modulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especificas.