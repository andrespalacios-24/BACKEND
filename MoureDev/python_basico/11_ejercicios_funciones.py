# 1. Crea una funcion llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningun nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(nombre="desconocido"):
    print(f"HOLA {nombre}")


personalized_greeting("ANDRES")
personalized_greeting()
 
# 2. Escribe una funcion llamada "multiply" que reciba dos numeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(valor_1, valor_2):
   return valor_1 * valor_2
 
resultado= multiply(5,5)
print(resultado)


# 3. Crea una funcion llamada "is_even" que reciba un numero entero como argumento y retorne True si es par y False si es impar.

def is_even(valor):  #no se puede poner print dentro del return ya que este devuelve un valor
 if valor %2 ==0:    # que se guarda no que se imprime en la pantalla como un print
  return (True)
 else:
  return (False)

#ejemplo tipo backend
usuarios = [2, 5, 8, 11, 14]

for id in usuarios:
    if is_even(id):
        print(f"ID {id} es par - asignar a grupo A")
    else:
        print(f"ID {id} es impar - asignar a grupo B")

# 4. Escribe una funcion llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayusculas.
 
def convert_to_uppercase(frase):
     return frase.upper()

print(convert_to_uppercase("buenas buenas"))


# 5. Crea una funcion llamada "arbitrary_sum" que reciba un numero arbitrario de numeros como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*values):
    return sum(values)
    
    
print(arbitrary_sum(323, 222, 3))

# 6. Escribe una funcion llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(nombre, apellido):
    return (f"HOLA, {nombre} {apellido}")

print(generate_full_greeting(apellido="maikel", nombre="smit"))

# 7. Crea una funcion llamada "power" que reciba dos numeros: base y exponente, y retorne el resultado de elevar la base al exponente.


def power(valor,valor_2):
    return valor ** valor_2

print(power(2, 3)) #8

# 8. Escribe una funcion llamada "calculate_average" que reciba tres numeros y retorne su promedio.

def calculate_average(numero_1, numero_2, numero_3):
    suma= (numero_1 + numero_2 + numero_3) 
    promedio= suma / 3
    return promedio

print(calculate_average(3,3,3))

# 9. Crea una funcion llamada "count_characters" que reciba una cadena de texto y retorne el numero de caracteres que contiene.

def count_characters(texto):
   return len(texto) #queda el len() solo porque es una funcion y no un metodo entonces no lleva .
  

print(count_characters("alo"))

# 10. Escribe una funcion llamada "display_messages" que reciba un numero indefinido de cadenas y las imprima en mayusculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*cadenas):
    for cadena in cadenas:
        print(cadena.upper())

display_messages("sisas", "mipapacho")