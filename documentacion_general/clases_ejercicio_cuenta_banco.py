# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade metodos para depositar y retirar dinero, asegurandote de que no se pueda retirar mas de lo que hay en la cuenta.

class BankAccount():
    def __init__(self,owner):
        self.owner=owner
        self.balance=[]
    
    def entradas(self,deposito):
        self.balance.append(deposito)

    def total_entradas(self):
        return sum(self.balance)
    
    def salidas(self,retiro):
        saldo_actual= self.total_entradas()
        if saldo_actual < retiro:
            print("noo mi papa su saldo actual es:")
            return saldo_actual
        else:
           nuevo_saldo= saldo_actual - retiro
        self.balance.append(-retiro)
        return nuevo_saldo


cliente= BankAccount("robert el kiyo")
cliente.entradas(30)
cliente.entradas(34)
cliente.entradas(54)
cliente.entradas(675)
cliente.entradas(34534)
print(cliente.total_entradas())
cliente.salidas(5327)
print(cliente.total_entradas())




# ============================================================
# CLASE BANKACCOUNT - ANÁLISIS Y VERSIÓN MEJORADA
# ============================================================

# ------------------------------------------------------------
# VERSIÓN ORIGINAL (funciona, pero tiene un diseño confuso)
# ------------------------------------------------------------

# El problema principal: balance es una LISTA que acumula todos
# los movimientos (depósitos como positivos, retiros como negativos).
# total_entradas() suma todo eso con sum(), lo que da el saldo neto.
# Funciona matemáticamente, pero:
#   - El nombre "total_entradas" es engañoso (incluye retiros)
#   - Es más difícil de leer y mantener
#   - Si la lista crece mucho, recalcular sum() cada vez es ineficiente

class BankAccountOriginal():
    def __init__(self, owner):
        self.owner = owner
        self.balance = []                      # lista de movimientos

    def entradas(self, deposito):
        self.balance.append(deposito)          # agrega número positivo

    def total_entradas(self):
        return sum(self.balance)               # suma TODO, incluidos negativos

    def salidas(self, retiro):
        saldo_actual = self.total_entradas()   # calcula saldo antes de retirar
        if saldo_actual < retiro:
            print("Saldo insuficiente. Saldo actual:", saldo_actual)
            return saldo_actual
        else:
            nuevo_saldo = saldo_actual - retiro
        self.balance.append(-retiro)           # agrega número negativo
        return nuevo_saldo


# ------------------------------------------------------------
# VERSIÓN MEJORADA (más clara, más directa)
# ------------------------------------------------------------

# Cambios clave:
#   - balance es un número (float), no una lista
#   - Se actualiza directamente con += y -=
#   - Los métodos se llaman depositar() y retirar() (más descriptivos)
#   - No hay que recalcular sum() en cada operación

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


# ------------------------------------------------------------
# PRUEBAS
# ------------------------------------------------------------

print("=" * 40)
print("VERSIÓN ORIGINAL")
print("=" * 40)
cliente1 = BankAccountOriginal("Robert el Kiyo")
cliente1.entradas(30)
cliente1.entradas(34)
cliente1.entradas(54)
cliente1.entradas(675)
cliente1.entradas(34534)
print("Saldo tras retiro de 534:", cliente1.salidas(534))   # espera 34793
print("Saldo tras retiro de 99999:", cliente1.salidas(99999))  # saldo insuficiente

print()
print("=" * 40)
print("VERSIÓN MEJORADA")
print("=" * 40)
cliente2 = BankAccount("Robert el Kiyo")
cliente2.depositar(30)
cliente2.depositar(34)
cliente2.depositar(54)
cliente2.depositar(675)
cliente2.depositar(34534)
cliente2.retirar(534)                          # espera saldo 34793
cliente2.retirar(99999)                        # saldo insuficiente
cliente2.ver_saldo()