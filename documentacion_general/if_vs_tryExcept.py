# =============================================================
# REFERENCIA: if/else  vs  try/except
# Andrés Palacios — Python Básico
# =============================================================

# -------------------------------------------------------------
# LA REGLA SIMPLE
# -------------------------------------------------------------
# if/else   → tú controlas la condición y decides qué hacer en ese momento.
# try/except → otro código puede lanzar un error con raise y tú lo capturas.
#
# CLAVE: raise lanza, except atrapa.
#        Siempre van en pareja, pero pueden estar en archivos distintos.

# -------------------------------------------------------------
# 1. CUÁNDO USAR if/else
# -------------------------------------------------------------
# Cuando TÚ evalúas la condición ahora mismo.
# No hay raise involucrado.

# EJEMPLO:
# edad = 20
#
# if edad >= 18:
#     print("Mayor de edad")
# else:
#     print("Menor de edad")
#
# ¿Por qué if aquí?
# Porque la condición edad >= 18 la evalúas tú, ahí mismo.
# Nadie lanzó ningún error. Tú decides la lógica.

# -------------------------------------------------------------
# 2. CUÁNDO USAR try/except
# -------------------------------------------------------------
# Cuando llamas código que puede lanzar raise
# y quieres capturar ese error para reaccionar.

# EJEMPLO (igual al mini banco):

# --- En cuenta.py (la clase lanza el error) ---
# def depositar(self, monto):
#     if monto <= 0:
#         raise ValueError("El monto debe ser mayor a cero")  ← lanza
#     self.__saldo += monto

# --- En operaciones.py (captura lo que la clase lanzó) ---
# def hacer_deposito(cuenta, monto):
#     try:
#         cuenta.depositar(monto)
#         print("Depósito exitoso")
#     except ValueError as e:
#         print(f"Error: {e}")                                 ← atrapa

# ¿Por qué try aquí?
# Porque depositar() puede lanzar raise ValueError.
# Tú no controlas cuándo ocurre — solo capturas si sucede.

# -------------------------------------------------------------
# 3. TABLA COMPARATIVA
# -------------------------------------------------------------
#
# if / else                              try / except
# ─────────────────────────────────────────────────────────────
# Tú evalúas la condición ahora          Otro código lanza el error
# No hay raise involucrado               Hay raise en algún lugar
# Control total en ese momento           Reacción a algo que puede fallar
# Siempre ejecuta uno u otro bloque      Solo entra al except si hay error
# Ej: validar edad, comparar valores     Ej: capturar ValueError, SaldoInsuficienteError

# -------------------------------------------------------------
# 4. ¿SE PUEDEN COMBINAR?
# -------------------------------------------------------------
# Sí. En este proyecto los usas juntos:
#
#   - Dentro de la clase: usas if para validar y raise para señalar el error.
#   - En operaciones.py: usas try/except para capturar lo que la clase lanzó.
#
# Son dos responsabilidades distintas en dos archivos distintos.
# Eso se llama: separación de responsabilidades.

# -------------------------------------------------------------
# 5. RESUMEN DE UNA LÍNEA
# -------------------------------------------------------------
# Si puedes anticipar el problema con una condición  →  if/else
# Si otro código lanza raise y tú debes reaccionar   →  try/except