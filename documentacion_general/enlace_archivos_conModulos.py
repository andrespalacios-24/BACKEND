# =============================================================
# REFERENCIA: Cómo se enlazan archivos en Python (módulos)
# Andrés Palacios — Python Básico
# =============================================================

# -------------------------------------------------------------
# EL PROBLEMA QUE RESUELVE
# -------------------------------------------------------------
# Cuando tienes un proyecto grande, no puedes poner todo en un
# solo archivo. Lo divides en módulos (archivos .py separados).
# Pero entonces necesitas que se "hablen" entre sí.
# Para eso existe el import.

# -------------------------------------------------------------
# PASO 1: CREAR LA CLASE EN SU PROPIO ARCHIVO (cuenta.py)
# -------------------------------------------------------------
#
# # cuenta.py
# class BankAccount:
#     def __init__(self, usuario):
#         self.usuario = usuario
#         self.__saldo = 0
#
#     def depositar(self, monto):
#         if monto <= 0:
#             raise ValueError("El monto debe ser mayor a cero")
#         self.__saldo += monto
#
# → cuenta.py define QUÉ ES y QUÉ PUEDE HACER una cuenta.
#   No sabe nada del resto del proyecto.

# -------------------------------------------------------------
# PASO 2: IMPORTAR EN OTRO ARCHIVO (operaciones.py)
# -------------------------------------------------------------
#
# # operaciones.py
# from cuenta import BankAccount          ← trae la clase
# from cuenta import SaldoInsuficienteError ← trae la excepción
#
# → Con from cuenta import BankAccount le dices a Python:
#   "Ve al archivo cuenta.py y tráeme la clase BankAccount"
#   A partir de ese momento, operaciones.py puede usarla.

# -------------------------------------------------------------
# PASO 3: RECIBIR EL OBJETO COMO PARÁMETRO
# -------------------------------------------------------------
#
# # operaciones.py
# def hacer_deposito(cuenta, monto):   ← recibe el objeto
#     try:
#         cuenta.depositar(monto)      ← usa el método del objeto
#         print("Depósito exitoso")
#     except ValueError as e:
#         print(f"Error: {e}")
#
# → La función NO crea la cuenta, la RECIBE.
#   El objeto trae consigo todos sus métodos de cuenta.py.
#   Cuando llamas cuenta.depositar(monto), Python va al objeto,
#   busca el método depositar y lo ejecuta.

# -------------------------------------------------------------
# PASO 4: EL FLUJO COMPLETO (main.py orquesta todo)
# -------------------------------------------------------------
#
# # main.py
# from cuenta import BankAccount
# from operaciones import hacer_deposito
#
# cuenta1 = BankAccount("Andrés")    ← crea el objeto
# hacer_deposito(cuenta1, 500)       ← pasa el objeto a operaciones
#
# → main.py crea los objetos y los pasa a las funciones.
#   Las funciones hacen el trabajo con esos objetos.

# -------------------------------------------------------------
# CÓMO VIAJA EL ERROR ENTRE ARCHIVOS
# -------------------------------------------------------------
#
# cuenta.py                operaciones.py            main.py
# ───────────────          ──────────────────        ──────────────
# depositar(monto)  →  →   try:                      hacer_deposito(
#   if monto <= 0:            cuenta.depositar()      cuenta1, -100)
#     raise ValueError  →  except ValueError as e:
#                              print(f"Error: {e}")
#
# → El raise nace en cuenta.py
# → Viaja automáticamente a quien llamó el método
# → El except en operaciones.py lo atrapa
# → main.py nunca ve el error, operaciones lo manejó

# -------------------------------------------------------------
# RESUMEN VISUAL
# -------------------------------------------------------------
#
#   cuenta.py          operaciones.py         main.py
#   ──────────         ──────────────         ──────────
#   class              from cuenta import     from operaciones import
#   BankAccount   ←──  BankAccount       ←──  hacer_deposito
#
#   define la          usa la clase           orquesta todo
#   clase              con try/except         crea objetos
#                                             llama funciones

# -------------------------------------------------------------
# REGLA PARA RECORDAR
# -------------------------------------------------------------
# El objeto es el puente entre archivos.
# Lo creas en main.py, lo pasas a operaciones.py,
# y operaciones.py llama los métodos que viven en cuenta.py.