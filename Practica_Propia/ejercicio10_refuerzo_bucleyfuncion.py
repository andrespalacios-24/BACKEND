# ============================================================
# REFUERZO: BUCLES + FUNCIONES - CONTEXTO BACKEND
# ============================================================
# Nivel: Python básico / intermedio temprano
# Temas: while, for, range(), break, continue, def, return
# Contexto: situaciones reales de backend
# Máximo 5 ejercicios, progresivos
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 - Validador de contraseña (bucle + función)
# ------------------------------------------------------------
# Un endpoint de registro necesita validar que la contraseña
# tenga mínimo 8 caracteres. Si no cumple, sigue pidiendo
# hasta que el usuario ingrese una válida.
#
# Requisitos:
# - Crea una función que reciba una contraseña y retorne
#   True si tiene 8+ caracteres, False si no.
# - Usa un bucle while que siga pidiendo hasta que sea válida.
# - Cuando sea válida, imprime "Contraseña aceptada."

def validar_contrasena(contrasena):
    pass  # reemplaza con tu lógica


# ------------------------------------------------------------
# EJERCICIO 2 - Registro de usuarios (for + función)
# ------------------------------------------------------------
# Tienes una lista de usuarios nuevos para registrar.
# Algunos ya existen en el sistema (otra lista).
# 
# Requisitos:
# - Crea una función que reciba la lista de nuevos usuarios
#   y la lista de usuarios existentes.
# - Recorre los nuevos con un for.
# - Si ya existe, imprime "{usuario} ya está registrado."
# - Si no existe, imprime "{usuario} registrado exitosamente."

usuarios_existentes = ["ana", "carlos", "luis"]
nuevos_usuarios = ["ana", "pedro", "luis", "maria"]

def registrar_usuarios(nuevos, existentes):
    pass  # reemplaza con tu lógica


# ------------------------------------------------------------
# EJERCICIO 3 - Filtro de logs (for + continue + función)
# ------------------------------------------------------------
# Un servidor genera logs con diferentes niveles:
# "INFO", "WARNING", "ERROR".
# Solo te interesan los ERROR para reportar.
#
# Requisitos:
# - Crea una función que reciba una lista de logs (strings)
#   y retorne una lista solo con los que contienen "ERROR".
# - Usa for y continue para saltar los que no son ERROR.

logs = [
    "INFO: servidor iniciado",
    "ERROR: conexión rechazada",
    "INFO: usuario autenticado",
    "ERROR: timeout en base de datos",
    "WARNING: uso de CPU alto",
    "ERROR: ruta no encontrada"
]

def filtrar_errores(logs):
    pass  # reemplaza con tu lógica


# ------------------------------------------------------------
# EJERCICIO 4 - Intentos de login (while + break + función)
# ------------------------------------------------------------
# Un sistema permite máximo 3 intentos de login.
# Si el usuario adivina la contraseña antes, accede.
# Si agota los intentos, se bloquea.
#
# Requisitos:
# - Crea una función que reciba la contraseña correcta.
# - Usa while con máximo 3 intentos.
# - Si acierta, imprime "Acceso concedido." y usa break.
# - Si agota intentos, imprime "Usuario bloqueado."

def intentos_login(contrasena_correcta):
    pass  # reemplaza con tu lógica


# ------------------------------------------------------------
# EJERCICIO 5 - Resumen de ventas (for + range() + función)
# ------------------------------------------------------------
# Tienes una lista de ventas diarias (números).
# Necesitas calcular el total, el promedio y la venta máxima.
# Esto simula un endpoint de reportes.
#
# Requisitos:
# - Crea una función que reciba la lista de ventas.
# - Recórrela con for (puedes usar range() o directo).
# - Retorna un diccionario con: total, promedio, maximo.
# - Imprime el resultado formateado con f-string.

ventas = [120, 340, 89, 456, 230, 178, 95]

def resumen_ventas(ventas):
    pass  # reemplaza con tu lógica


# ------------------------------------------------------------
# PRUEBAS - descomenta cuando tengas cada ejercicio listo
# ------------------------------------------------------------

# validar_contrasena(input("Ingresa tu contraseña: "))
# registrar_usuarios(nuevos_usuarios, usuarios_existentes)
# print(filtrar_errores(logs))
# intentos_login("backend123")
# print(resumen_ventas(ventas))