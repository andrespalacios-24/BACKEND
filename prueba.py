# 4. Añade a la clase "Car" un metodo llamado "accelerate" que aumente la velocidad en 10 unidades. Añade tambien un metodo "brake" que reduzca la velocidad en 10 unidades. Asegurate de que la velocidad no sea negativa.

class Car(): #los nombres de las clases su primer letra siempre en mayuscula ej: CarDealer
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        self._speed= 0

    def accelerate(self):
        self._speed += 10

    def brake(self):
        if self._speed > 0:
            self._speed -= 10
        else:
            print("no es posible el carro esta detenido")