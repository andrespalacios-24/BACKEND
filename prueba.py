# 10. Escribe una funcion llamada "display_messages" que reciba un numero indefinido de cadenas y las imprima en mayusculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*cadenas):
    for cadena in cadenas:
        print(cadena.upper())

display_messages("sisas", "mipapacho")