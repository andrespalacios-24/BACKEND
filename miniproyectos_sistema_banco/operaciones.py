from cuenta import BankAcount
from cuenta import SaldoInsuficienteError
#pseudocodigo
#crear variable (depositar dinero)
#se llama cuenta.depositar(monto) para usar el metodo del objeto
#donde se sume el monto del deposito al saldo
#con try except para capturar el error
#en el except se pone el value error donde se le asigna un nombre 
#para impirmirlo y que salga la advertencia que pusimos en el archivo cuenta

def depositar_monto(cuenta,monto):
    try:
        cuenta.depositar(monto)
        print(f"deposito exitoso, su saldo actual es: {cuenta.ver_saldo()}")
    except ValueError as error:
        print(f"ERROR: {error}") 


#crea variable retirar_monto (cuenta,monto)
#se llama cuenta.retirar(monto) para usar el metodo del objeto
#donde se resta el monto del saldo que tiene
#con try except se atrapa el error personalizado 
#retiro menor a cero y saldo menor al monto a retirar 
#donde se le asigna el texto del error puesto en el archivo cuenta

def retirar_monto(cuenta,monto):
    try: 
        cuenta.retirar(monto)
        print(f"retiro exitoso, su saldo actual es: {cuenta.ver_saldo()}")
    except ValueError as error:
        print(f"ERROR:{error}")
    except SaldoInsuficienteError as e:
        print(f"ERROR:{e}")

