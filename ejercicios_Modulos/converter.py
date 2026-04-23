# 2. Crea un modulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este modulo y realice conversiones.
#crear funcion para cada uno
# hacer la operacion para cada funcion


def celsius(F):
   
    grados_celcius= (F- 32) / 1.8
    return grados_celcius


def fahrenheit (C):
    grados_fahrenheit= (C * 1.8) + 32
    return grados_fahrenheit


