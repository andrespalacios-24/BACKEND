# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un metodo que calcule la distancia entre dos puntos.
import math
class Coordenada():
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distacia_a(self, otra):
    
        dx= self.x - otra.x
        dy= self.y - otra.y

        distancia= math.sqrt(dx**2 + dy**2)
    
        return distancia
    
punto_a= Coordenada(1,2)
punto_b= Coordenada(3,4)
resultado= punto_a.distacia_a(punto_b)
print(f"La distancia es: {resultado}")