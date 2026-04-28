# =============================================================
# MINIPROYECTO 3: Mini banco
# Temas integrados: OOP, módulos, excepciones, archivos de texto
# =============================================================

# ESTRUCTURA DE ARCHIVOS:
# miniproyectos/
# ├── banco/
# │   ├── cuenta.py        ← módulo con la clase BankAccount mejorada
# │   ├── operaciones.py   ← módulo con funciones de deposito/retiro
# │   ├── historial.py     ← módulo para guardar/leer historial en .txt
# │   └── main.py          ← programa principal

# -------------------------------------------------------------
# ARCHIVO 1: cuenta.py
# -------------------------------------------------------------
# Clase BankAccount con:
#   - atributos: titular, __saldo (encapsulado)
#   - getter saldo
#   - metodo depositar(monto):
#       excepcion si monto <= 0
#   - metodo retirar(monto):
#       excepcion si monto <= 0
#       excepcion si monto > saldo (SaldoInsuficienteError)
# Crear excepcion personalizada SaldoInsuficienteError

# -------------------------------------------------------------
# ARCHIVO 2: operaciones.py
# ------------------------------------------------------------- 
# Importar cuenta
# Funcion hacer_deposito(cuenta, monto):
#   llama cuenta.depositar() con manejo de excepcion
# Funcion hacer_retiro(cuenta, monto):
#   llama cuenta.retirar() con manejo de excepcion

# -------------------------------------------------------------
# ARCHIVO 3: historial.py
# -------------------------------------------------------------
# Funcion registrar(titular, operacion, monto):
#   guarda en "historial.txt": "titular,operacion,monto"
# Funcion ver_historial():
#   lee y muestra todas las operaciones guardadas

# -------------------------------------------------------------
# ARCHIVO 4: main.py
# -------------------------------------------------------------
# Crear 2 cuentas
# Hacer depositos y retiros (incluyendo algunos invalidos)
# Registrar cada operacion en historial.txt
# Mostrar historial al final