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

def validar_contrasena():
    # el input dentro del bucle es el que permite pedir los datos en cada vuelta si no se cumple la
    while True: # este while true se utiliza cuando el bucle debe repetirse hasta que algo ocurra
        contraseña=input("Ingrese contraseña: ") # si no se cumple con los 8 caracteres
        if len(str(contraseña)) >= 8:            # el bucle sube y esta vez coge al input y asi hasta que de true y para con el break
            print("Contraseña aceptada")
            break
        else:
            print("contraseña incorrecta")
validar_contrasena()

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
   for usuarios in nuevos:
      if usuarios in existentes:
         print(f"{usuarios} el usuario ya esta registrado")
      else:
         print(f"{usuarios} registrado exitosamente")

registrar_usuarios( nuevos_usuarios,usuarios_existentes)

# PARÁMETROS = APODOS TEMPORALES
# def registrar_usuarios(nuevos, existentes) le dice a la función:
# "lo primero que te pasen llámalo 'nuevos', lo segundo 'existentes'"
# Cuando llamas registrar_usuarios(nuevos_usuarios, usuarios_existentes)
# Python hace internamente: nuevos = nuevos_usuarios / existentes = usuarios_existentes
# Por eso la función puede recibir CUALQUIER lista, no depende de nombres fijos.
# Esto es lo que hace reutilizable una función en backend.

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

errores= [] # cree esta lista para que se acumularan los errores

def filtrar_errores(logs):
    for busqueda in logs:
        if "ERROR" in busqueda:          
            errores.append(busqueda) #con el .append va añadiendo a la lista 
    return errores #para que se retorne a la lista de errores

print(filtrar_errores(logs))

# LECCIÓN EJERCICIO 3 - Filtro de logs
# 1. return va FUERA del for, al mismo nivel — si está dentro, la función
#    para en la primera iteración y no recorre toda la lista.
# 2. Primero acumula (append), luego retorna — el return siempre al final.
# 3. continue no siempre es necesario — si el if no se cumple, el for
#    ya pasa solo al siguiente elemento. Úsalo solo cuando necesites
#    saltar lógica adicional que venga después dentro del bucle.


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
    intentos= 0 # el contador debe ir dentro de la funcion pero fuera del bucle para que se haga la suma
    while True:
        
        intento= input("Ingrese contraseña: ")
        if intento == contrasena_correcta:
            print ("Acceso concedido")
            break
        else:
         intentos +=1
         if intentos >=3: # un if pued ir dentro de un else
                print("usuario bloqueado")
                break #para que se detenta en los 3 intentos
        
intentos_login("backend123")


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