# ============================================================
# MINIPROYECTO — SISTEMA DE GESTIÓN DE EMPLEADOS
# Temas integrados: JSON, RegEx, Excepciones, datetime
# ============================================================

# INSTRUCCIONES:
# Antes de escribir cualquier función, escribe el pseudocode en comentarios.
# Piensa en el flujo lógico antes de la sintaxis.
# El sistema debe funcionar desde consola con un menú principal.

# ============================================================
# REQUERIMIENTOS
# ============================================================

# El sistema debe permitir:
# 1. Agregar un empleado (nombre, cargo, salario, fecha de ingreso)
# 2. Listar todos los empleados
# 3. Buscar empleado por nombre (usando RegEx)
# 4. Mostrar estadísticas (salario promedio, empleado mejor pagado)
# 5. Eliminar un empleado por nombre
# 6. Guardar los datos en un archivo JSON
# 7. Cargar los datos desde el archivo JSON al iniciar

# ============================================================
# ESTRUCTURA DE DATOS SUGERIDA
# ============================================================

# Cada empleado es un diccionario:
# {
#     "nombre": "Andrés Palacio",
#     "cargo": "Backend Developer",
#     "salario": 3500000,
#     "fecha_ingreso": "2024-05-10"
# }
#
# Todos los empleados van en una lista de diccionarios.
# Esa lista se guarda y carga desde "empleados.json".

# ============================================================
# RESTRICCIONES (para guiarte, no son opcionales)
# ============================================================

# - Usar try/except donde el programa pueda fallar
#   (archivo no existe, entrada inválida, lista vacía)
# - La búsqueda por nombre DEBE usar re.search() con re.IGNORECASE
# - La fecha de ingreso debe guardarse como string "YYYY-MM-DD"
#   y mostrarse formateada con datetime.strptime()
# - El salario debe validarse: no puede ser negativo ni texto
# - Si no hay empleados al pedir estadísticas, manejar el caso

# ============================================================
# ESQUELETO — completa cada función
# ============================================================

import json
import re
from datetime import datetime

ARCHIVO = "empleados.json"


# --- FUNCIÓN 1 ---
# Carga los empleados desde el archivo JSON.
# Si el archivo no existe, retorna una lista vacía.
# Si el archivo existe pero está mal formado, maneja el error.
#pseudocode
#crear una funcion para cargar los empleados con archivo json (read)
#se ua el try /except para manejar el error de que no se ha creado la lista
#usamos el with open para que el archivo cierre automaticamente 
#se pone la ubicacion del archivo donde se abre el json y se lee
#se una el json.load para cargar el archivo
#en el except despues del manejo del file no found se retorna una lista vacia 
#en el except despues del json.JSONDecodeError se retorna un print con:
#Error de sintaxis en el JSON: {e} y retornamos nuevamente una lista vacia 
def cargar_empleados():
    try:
        with open("python_intermedio/empleados.json","r", encoding="utf-8")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []



# --- FUNCIÓN 2 ---
# Guarda la lista de empleados en el archivo JSON.
# Usa indent=4 para que sea legible.
#pseudocode
#se crea la funcion donde se guardara el archivo .json
#se usa el with open para el cerrado automatico 
#se pone al ubicacion donde el archivo se sobre escribe 
#para sobreescribir o crear si no existe se usa "w"
#se usa el .dump para guardar el archivo como json
#dentro del .dump se pone el ident=4
#ira tambien empleados y el archivo donde se sobreescribira 
#usar el ensure_ascii=False para poder que los nombres seal legibles por humanos
def guardar_empleados(empleados):
   with open("python_intermedio/empleados.json","w",encoding="utf-8")as archivo:
        json.dump(empleados, archivo, indent=4, ensure_ascii=False)

# --- FUNCIÓN 3 ---
# Agrega un nuevo empleado a la lista.
# Pide por consola: nombre, cargo, salario (validar que sea número positivo),
# fecha de ingreso (formato YYYY-MM-DD, validar con try/except y strptime).
# Guarda después de agregar.
#pseudocode
#se crea funcion para agregar los empleados
#se debe pedir nombre, cargo con input
#se pide salario con input con un while, dentro un try except para manejar los errres de numero negativo y str
#debera lanzar un value error
#se pide con input la fecha de ingreso y con try except se valida que el formato sea el corecto
#se crea variable que contenga el dict con la clave valor entra cada uno de nombre, cargo y salario
#se llama a guardar empleados al final para guardar al archivo json

def agregar_empleado(empleados):
    nombre= input("escribir nombre de nuevo contacto: ")
    cargo= input("cargo a tener: ")
    while True:
        try:
            salario= float(input("salario mensual a ganar: "))
            if salario <0: 
                print("ERROR: el salario no puede ser negativo")
                continue
            print(f"Salario validado con éxito: {salario}")
            break
        except ValueError:
            print("Error: Debes introducir un número válido (no texto).")
    
    while True:
        try:
            fecha_ingreso= input("Introduce la fecha (YYYY-MM-DD): ")
            fecha_objeto = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
            print(f"Fecha válida: {fecha_objeto.strftime('%Y-%m-%d')}")
            break
        except ValueError:
            print("Error: Formato incorrecto. Debe ser AAAA-MM-DD (ejemplo: 2026-05-14).")

    trabajadores= {
        "nombre": nombre,
        "cargo": cargo,
        "salario": salario,
        "fecha_ingreso":fecha_ingreso
    }
    empleados.append(trabajadores)
    guardar_empleados(empleados)
   


# --- FUNCIÓN 4 ---
# Lista todos los empleados con formato legible.
# Si no hay empleados, muestra un mensaje indicándolo.
# La fecha de ingreso debe mostrarse como "10 de mayo de 2024" (strftime).
#pseudocode
#crear funcion  para ver los empleados
#usar bucle for para moverse en el diccionario key:valor 
#usar if/else para indicar que no existe el empleado y que imprima un mensaje
#usar el formato strftime para hacer la fecha legible 
def listar_empleados(empleados):
    if not empleados:
        print("No hay empleados en el registro")
    else:
        for empleado in empleados:
            print(empleado["nombre"])
            print(empleado["cargo"])
            print(empleado["salario"])
            # Paso 1: string → objeto datetime
            fecha_obj = datetime.strptime(empleado["fecha_ingreso"], "%Y-%m-%d")
            # Paso 2: objeto datetime → string bonito
            fecha_bonita = fecha_obj.strftime("%d de %B de %Y")
            print(fecha_bonita)
            print("-" * 30)


# --- FUNCIÓN 5 ---
# Busca empleados cuyo nombre coincida con el texto ingresado.
# USA re.search() con re.IGNORECASE.
# Muestra todos los que coincidan.
# Si no hay coincidencias, indicarlo.
#pseudocode
#crear un funcion de buscar empleados 
# crear variable con una lista vacia donde se guarden los resultados de la busqueda
#crear variable que contenga un output donde se ingresa el nombre a buscar
#usar el bucle for empleado in empleados 
#usar el if:
#usar re.search() con empelados, nombre y el ignorecase
#si cumple se usa .append para enviarla a la lista vacia
# se retorna la lista
#con else se lanza print con usuario no existe 
def buscar_empleado(empleados):
    personal= []
    nombre= input("buscar empleado por nombre: ")
    for empleado  in empleados:
        if re.search(nombre, empleado["nombre"], re.I):
            personal.append(empleado)
    if personal:
        for resultado in personal:
            print(resultado["nombre"])
            print(resultado["cargo"])
            print(resultado["salario"])
            print("-" * 30)
    else:
        print("No se encontró ningún empleado con ese nombre.")
    
    



# --- FUNCIÓN 6 ---
# Muestra estadísticas:
# - Total de empleados
# - Salario promedio
# - Empleado con mayor salario
# - Empleado con menor salario
# Si no hay empleados, manejar el caso.

def mostrar_estadisticas(empleados):
    # pseudocode aquí
    pass


# --- FUNCIÓN 7 ---
# Elimina un empleado por nombre exacto (puedes usar RegEx o comparación directa).
# Si no existe, indicarlo.
# Guarda después de eliminar.

def eliminar_empleado(empleados):
    # pseudocode aquí
    pass


# --- MENÚ PRINCIPAL ---
# No modificar este bloque — es el punto de entrada del programa.
# Cuando completes todas las funciones, el menú funcionará solo.

def menu():
    empleados = cargar_empleados()
    print("\n=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

    while True:
        print("\n1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Estadísticas")
        print("5. Eliminar empleado")
        print("6. Salir")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            agregar_empleado(empleados)
        elif opcion == "2":
            listar_empleados(empleados)
        elif opcion == "3":
            buscar_empleado(empleados)
        elif opcion == "4":
            mostrar_estadisticas(empleados)
        elif opcion == "5":
            eliminar_empleado(empleados)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()