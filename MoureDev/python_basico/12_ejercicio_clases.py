# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un metodo "make_sound" que imprima un sonido generico.

class Animal():
    def __init__(self, species):
        self.species=species

    def make_sound(self):
        print(f"El {self.species} hace un sonido propio del animal")
        
domestico = Animal("gato")
print(domestico.species)
domestico.make_soud()
# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacenala en una propiedad publica. Añade el metodo "make_sound" que imprima un sonido dependiendo de la especie.

class Animal():
    def __init__(self, species):
        self.species=species

    def make_sound(self):
        if self.species.lower() == "perro": #se puso el .lower() por si un usuario escribe la primera en
            print("guau guau")              # mayuscula entonces en make_sound aparece sonido no reconocido
        elif self.species.lower() == "gato": #debido a que el sistema busca la misma palabra, de esa forma
            print("miau miau")               # no importan las mayusculas lo empareja
        else:
            print("sonido aun no reconocido")

domestico= Animal("Gato")
print(domestico.species)
domestico.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades publicas "brand" y "model". Ademas, debe tener una propiedad privada "_speed" que inicialmente sera 0.

class Car(): #los nombres de las clases su primer letra siempre en mayuscula ej: CarDealer
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        self._speed= 0
        

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

carro= Car("Toyota", "supra")
print(f"su carro marca: {carro.brand} y modelo: {carro.model}")
carro.accelerate()
carro.accelerate()
carro.brake()
print(carro._speed)

# 5. Crea una clase "Book" que tenga propiedades como "title" (publico) y "author" (privado). Añade un metodo para obtener el autor y otro para cambiar el ti­tulo del libro.

class Book ():
    def __init__(self, title, author):
        self.title= title
        self.__author= author
    #getter
    def obtener_author(self): # esto se hace cuando necesitas saber que va en una variable encapsulada
        return self.__author
    def cambiar_titulo(self, titulo_nuevo):
        self.title= titulo_nuevo

titulo= Book("ay mi gatito miau, miau", "el gatito")
print(f"el libro: {titulo.title} del autor: {titulo.obtener_author()}")

#para poder imprimir el autor que esta encapsulado se pone la variable que se uso para hacer el    
# getter, de esa forma podemos imprimir esa variable encapsulada.
#setter = se usa para cambiar la variable encapsulada, tambien sirve con variable publica
titulo.cambiar_titulo("mi perrito guau guau")
print(titulo.title)

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un metodo para calcular y devolver la nota media del estudiante.

class Estudiante():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.lista_notas= []
        
    def agregar_nota(self, nota):
        self.lista_notas.append(nota)

    def total_nota(self):
        return sum(self.lista_notas)
    
    def promedio(self):
        if len(self.lista_notas)== 0:
            return 0
        return sum(self.lista_notas) / len(self.lista_notas)

primer_estudiante= Estudiante("robert", "kiyo")
print(f"primer nombre:{primer_estudiante.nombre} Primer apellido: {primer_estudiante.apellido}")
primer_estudiante.agregar_nota(3.0)
primer_estudiante.agregar_nota(3.0)
primer_estudiante.agregar_nota(3.0)
primer_estudiante.agregar_nota(3.0)
print(f"total notas:{primer_estudiante.total_nota()}, total promedio:{primer_estudiante.promedio()}")
# se tiene que poner los () al final ya que eso llama el metodo y dan las operaciones si no no sabe
# donde coger los valores y dara <bound method Estudiante.total_nota of <__main__.Estudiante object at 0x7e33db94ddc0>>

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade metodos para depositar y retirar dinero, asegurandote de que no se pueda retirar mas de lo que hay en la cuenta.

class BankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance                 # saldo actual como número

    def depositar(self, monto):
        if monto <= 0:                         # validación: no depositar negativos
            print("El monto a depositar debe ser mayor a 0.")
            return
        self.balance += monto                  # actualiza el saldo directamente
        print(f"Depósito exitoso. Saldo actual: {self.balance}")

    def retirar(self, monto):
        if monto <= 0:                         # validación: no retirar negativos
            print("El monto a retirar debe ser mayor a 0.")
            return
        if monto > self.balance:               # validación: saldo suficiente
            print(f"Saldo insuficiente. Saldo actual: {self.balance}")
            return
        self.balance -= monto                  # descuenta directamente del saldo
        print(f"Retiro exitoso. Saldo actual: {self.balance}")

    def ver_saldo(self):
        print(f"Titular: {self.owner} | Saldo: {self.balance}")

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

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un metodo que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee():
    def __init__(self, name, hourly_wage):
        self.name=name
        self.hourly_wage=hourly_wage
        self.hours_worked= 0

    def horas (self,numero ):
        self.hours_worked +=numero

    def pago (self):
      sueldo=  self.hours_worked * self.hourly_wage
      return sueldo
       

trabajador= Employee("robert",34)

trabajador.horas(22)
trabajador.horas(22)

print(trabajador.hours_worked)
print(trabajador.pago())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un metodo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.