def dividir():
 try:
     numero_1= int(input("Ingrese primer numero: ")) 
     numero_2= int(input("Ingrese segundo numero: "))
     print(numero_1/numero_2)
     print("no hay error en la division")
 except ValueError:
   print("uno de los parametros no es un numero")

dividir()

#git commit -m "se inicia tema nuevo:excepciones y se hacen los ejercicios de mouredev del 1 al 7, se agrega el tema visto con sus explicaciones"