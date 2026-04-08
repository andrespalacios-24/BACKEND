# 1. Escribe un programa que verifique si un numero es positivo, negativo o cero.
numero= -2
if numero >=1: 
    print("el numero es positivo")
elif numero < 0: 
    print("numero negativo")
else:
    print("numero igual a cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o mas) o menor de edad.
edad= int(input("Ingresar Edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto esta vacia y muestre un mensaje en consecuencia.
cadena_de_texto= input("cadena de texto:")

if not cadena_de_texto:
    print("cadena de texto vacia") 
else:
    print("Contiene texto")

# 4. Crea un programa que solicite dos numeros al usuario y compare cual es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
numero_1= int(input("Digite el primer numero:"))
numero_2= int(input("Digite el segundo numero:"))
if numero_1 > numero_2:
    print("primer numero es mayor")
elif numero_1 == numero_2:
    print("los dos numeros son iguales")
else:
    print("segundo numero es mayor")


# 5. Escribe un programa que verifique si un numero es divisible por 3 y por 5 al mismo tiempo.
numero= int(input("ingrese un numero:"))
if numero % 5 == 0 and numero % 3 == 0:
    print("el numero es divisible entre 3 y 5")
else:
    print("el numero no es divisible entre 3 y 5 ")

# 6. Solicita al usuario que ingrese un numero y verifica si es par o impar.
numero= int(input("ingrese un numero:"))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

# 7. Escribe un programa que determine si una persona puede votar en funcion de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
edad= int(input("Ingrese su edad:"))
if edad >= 18:
    print("Puede acceder al punto de votacion")
elif edad == 16 or edad == 17:
    print("Puede acceder al punto de votacion con permiso especial")
else:
    print("no puede acceder al punto de votacion")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
contraseña_predefinida= "contraseña123"
contraseña_usuario= input("Ingrese contraseña:")
if contraseña_usuario == contraseña_predefinida:
    print("Ingreso valido")
else:
    print("Ingreso invalido: contraseña incorrecta")
# 9. Escribe un programa que determine si un numero esta entre 10 y 20 (ambos incluidos).
numero= int(input("Ingrese un numero:"))
if numero >= 10 and numero <= 20:
    print("El numero esta entre 10 y 20")
else:
    print("El numero no esta entre 10 y 20")
# 10. Escribe un programa que simule un semaforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color =input("color del semaforo:")
match color:
    case "rojo":
        print("detente mamaguevo")
    case "amarillo":
        print("rapidito hijo del diablo")
    case "verde":
        print("no estamos en pare") 