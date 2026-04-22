# 10. Crea una funcion que calcule la rai­z cuadrada de un numero. Lanza un ValueError si el numero es negativo.

def raiz_cuadrada(numero):
    try:
     if numero <0:
         raise ValueError
     raiz= (numero ** 0.5)  
     return raiz
    except ValueError:
          print ("el numero es negativo")

print(raiz_cuadrada(-9))

# cuando la función encuentra un ValueError (número negativo),
# entra al except y ejecuta el print() — imprime el mensaje y listo.
# pero la función NO retorna ningún valor — simplemente termina.
# en Python, cuando una función termina sin return, automáticamente retorna None.

# el problema está afuera:
print(raiz_cuadrada(-9))
# esto hace DOS cosas:
# 1. ejecuta raiz_cuadrada(-9) → que ya imprime "el numero es negativo"
# 2. intenta imprimir lo que retornó la función → que es None
# por eso ves las dos líneas:
# el numero es negativo
# None

# solución: para el caso de error, el print ya está DENTRO de la función.
# no necesitas otro print() afuera. solo usas print() afuera para el caso exitoso:
print(raiz_cuadrada(9))   # aquí sí tiene sentido porque retorna un valor
raiz_cuadrada(-9)         # aquí no necesitas print() afuera, ya lo maneja la función
#La regla general para recordar: si la función ya imprime por dentro, no la envuelvas en print() por fuera.