# 4. Crea un modulo llamado "geometry" que tenga una funcion para calcular el area de un ci­rculo y un cuadrado. Usa este modulo en otro archivo para calcular areas.


    
def area_circulo_radio(radio):
    return 3.14 * (radio ** 2)



def area_circulo_diametro(diametro):
    radio = diametro / 2
    return 3.14 * (radio ** 2)


def area_cuadrado(lado):
    return lado * lado