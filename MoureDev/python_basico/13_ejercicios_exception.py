# 1. Crea una funcion que intente dividir dos numeros proporcionados por el usuario. Usa try-except para capturar cualquier error de numero (por ejemplo, numero por cero).
def dividir():
 try:
     numero_1= int(input("Ingrese primer numero: ")) 
     numero_2= int(input("Ingrese segundo numero: "))
     print(numero_1/numero_2)
     print("no hay error en la division")
 except ValueError:
   print("uno de los parametros no es un numero")

dividir()

# 2. Crea una funcion que tome una cadena e intente convertirla en un numero entero. Usa try-except para capturar cualquier error en la conversion.
def convertir_numero():
 try:
     numero = int(input("Ingrese numero: ")) # esta variable si va dentro del try porque el error estaria en lo que escriba el usuario
     print(f"{numero} convertido a entero correctamente") 
 except ValueError:
     print("el valor no es un numero") # en este caso es mejor poner nos except por si ponen un str en uno de los numeros
 except TypeError:                                 # de esta forma no da el error de no se puede convertir a entero sin saber si fue por letras
     print("Tipos de datos incompatibles")
 
     
# 3. Crea una funcion que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def archivo(archivo):
 documento= None # se debe crear esta variable si el archivo no existe, ya que python intenta leer algo que no existe
 try:            #  y el programa va a fallar en lugar de avisar que no encontro el archivo
   documento= open(archivo,"r")
   contenido= documento.read()  
   return(contenido)
 except FileNotFoundError:
   print("archivo no encontrado")
 finally:
   if documento is not None:
     documento.close()
   
archivo("notas.txt")
archivo("strings.py")
archivo("datos.csv")

# 4. Crea una funcion que realice multiples operaciones (suma, resta, numero, multiplicacion) con dos numeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

def operaciones(numero_1, numero_2):
 #numero_1= int(input("Ingrese primer numero: "))
 #numero_2= int(input("Ingrese segundo numero: "))
 try:
   print(numero_1 + numero_2)
   print(numero_1 - numero_2)
   print(numero_1 / numero_2)
   print(numero_1 * numero_2)
   #print("no hay errores en las operaciones") este se quita debido a que con el "else" ya se indica que esta operacion
   # no fallo y que todo salio bien 
 except ZeroDivisionError:
   print("hay error en la division")
 except ValueError:
   print("error no es un numero")
 except TypeError:
   print("los tipos de datos no son compatibles")
 else:
   print("las operaciones se realizaron correctamente")
 finally:
   print("la ejecucion continua")

operaciones(5,0)

# 5. Crea una funcion que le pida al usuario su edad y lance un ValueError si la entrada no es un numero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

def usuario():
   try:
    edad= int(input("digite su edad: "))                             
    if edad < 0: 
      raise ValueError ("la edad no debe dar negativo")
   except ValueError: #este valueError sirve tanto para numeros negativos como para str por eso esta dos veces
    print("ERROR: el valor debe ser un numero")
    
usuario()

# 6. Crea una funcion que intente acceder a un elemento de una lista por índice.
# Usa try-except para manejar el caso donde el indice esta fuera de rango.

lista = [1, 2, 3, 4]
def indice():
    numero = int(input("numero de indice: "))
    try:
        elemento = lista[numero]  # accede al índice indicado
                                  # los índices empiezan en 0, entonces:
                                  # lista[0]=1, lista[1]=2, lista[2]=3, lista[3]=4
                                  # lista[4] ya no existe → lanza IndexError automáticamente
        print(f"el elemento es {elemento}")
    except IndexError:
        print("ERROR: este indice no existe en la lista")  # captura el IndexError de lista[numero]

indice()

# 7. Crea una funcion que use try-except para manejar multiples excepciones: ZeroDivisionError, ValueError y TypeError.

def multiples_excepciones():
    try:
       numero_1= int(input("inserte primer valor: "))
       numero_2= int(input("inserte segundo valor: "))
       print(numero_1 / numero_2)
       print("operacion correcta")  
    except ZeroDivisionError:
        print("error, division por cero")
    except ValueError:
        print("uno de los elementos no es convertible a numero")
    except TypeError:
        print("uno de los elementos no es un numero")

multiples_excepciones()

# 8. Crea una funcion que simule una transaccion. Lanza una excepcion personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

# 9. Crea una funcion que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

# 10. Crea una funcion que calcule la rai­z cuadrada de un numero. Lanza un ValueError si el numero es negativo.