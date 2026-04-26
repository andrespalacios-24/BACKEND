# PSEUDOCÓDIGO cuenta.py
#
# Excepción personalizada:
#   SaldoInsuficienteError
#
# Clase BankAccount:
#   Atributos:
#     - titular (público)
#     - __saldo (privado/encapsulado)
#
#   Métodos:
#     - getter saldo
#
#     - depositar(monto):
#         verificar que monto > 0
#         si no, lanzar ValueError
#
#     - retirar(monto):
#         verificar que monto > 0
#         si no, lanzar ValueError
#         verificar que monto <= saldo
#         si no, lanzar SaldoInsuficienteError

class SaldoInsuficienteError(Exception):
    pass

class BankAcount():
    def __init__(self,usuario):
        self.usuario=usuario
        self.__saldo= 0 

     #getter
    def ver_saldo(self):
     return self.__saldo
    
    
    def depositar(self, monto):
     if monto <= 0:
      raise ValueError ("el monto debe ser mayor a cero")
     self.__saldo += monto
   
    def retirar(self, monto):
     if monto <=0:
      raise ValueError ("el monto a retirar debe ser mayor a cero")
     if monto > self.__saldo:
       raise SaldoInsuficienteError(f"saldo insuficiente su saldo actual es: {self.ver_saldo()}")
     self.__saldo -= monto
     print(f"Retiro exitoso. saldo actual: {self.ver_saldo()}")
         
    

      