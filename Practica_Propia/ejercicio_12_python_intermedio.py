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

def cargar_empleados():
    # pseudocode aquí
    pass


# --- FUNCIÓN 2 ---
# Guarda la lista de empleados en el archivo JSON.
# Usa indent=4 para que sea legible.

def guardar_empleados(empleados):
    # pseudocode aquí
    pass


# --- FUNCIÓN 3 ---
# Agrega un nuevo empleado a la lista.
# Pide por consola: nombre, cargo, salario (validar que sea número positivo),
# fecha de ingreso (formato YYYY-MM-DD, validar con try/except y strptime).
# Guarda después de agregar.

def agregar_empleado(empleados):
    # pseudocode aquí
    pass


# --- FUNCIÓN 4 ---
# Lista todos los empleados con formato legible.
# Si no hay empleados, muestra un mensaje indicándolo.
# La fecha de ingreso debe mostrarse como "10 de mayo de 2024" (strftime).

def listar_empleados(empleados):
    # pseudocode aquí
    pass


# --- FUNCIÓN 5 ---
# Busca empleados cuyo nombre coincida con el texto ingresado.
# USA re.search() con re.IGNORECASE.
# Muestra todos los que coincidan.
# Si no hay coincidencias, indicarlo.

def buscar_empleado(empleados):
    # pseudocode aquí
    pass


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