from cuenta import BankAcount
from cuenta import SaldoInsuficienteError
from operaciones import depositar_monto, retirar_monto
from historial import lectura_registro, registro

#pseudocodigo
# crear 2 cuentas usando Cuenta y ponemos los parametros
# hacer deposito y retiro, tanto correctamente como con numeros invalidos
# se registra las operaciones en historial.txt
# darle print al historial para ver los movimientos

cliente_1= BankAcount("roberto")
cliente_2= BankAcount("maicol")

try:
    cliente_1.depositar(700)
    registro("roberto","depositar",700)
except ValueError as e:
    print(f"ERROR:{e}")

try:
   
 cliente_2.depositar(233)
 registro("maicol", "depositar",233)
except ValueError as e:
    print(f"ERROR:{e}")

try:
    
    cliente_1.depositar(-44)
    registro("roberto","depositar",-44)
except ValueError as e:
    print(f"ERROR:{e}")


try:
    cliente_1.retirar(345)
    registro("roberto","retiro",345)
except SaldoInsuficienteError as e:
    print(f"ERROR: {e}")

try:
    
    cliente_2.retirar(634)
    registro("maicol","retiro",634)
except SaldoInsuficienteError as e:
    print(f"ERROR: {e}")

lectura_registro()