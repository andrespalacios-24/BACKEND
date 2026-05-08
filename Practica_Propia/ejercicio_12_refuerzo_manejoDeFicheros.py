### MINIPROYECTO — AGENDA DE CONTACTOS ###
# Tema: Manejo de ficheros (JSON)
# Dificultad: Intermedio
# Tiempo estimado: 1 sesión
#
# REGLA OBLIGATORIA:
# Antes de escribir cualquier función, escribe el pseudocode en comentarios.
# Primero la lógica, luego el código.


# =============================================================================
# CONTEXTO
# =============================================================================
# Vas a construir una agenda de contactos que persiste datos en un archivo
# JSON. Cada vez que cierres y abras el programa, los contactos siguen ahí.
# Nada de listas en memoria que se borran al terminar — datos reales en disco.


# =============================================================================
# REQUISITOS DEL PROGRAMA
# =============================================================================
# El programa debe poder:
#
#   1. AGREGAR un contacto nuevo (nombre, teléfono, email)
#   2. VER todos los contactos guardados
#   3. BUSCAR un contacto por nombre
#   4. ELIMINAR un contacto por nombre
#   5. GUARDAR los cambios en el archivo JSON automáticamente
#
# Cada contacto tiene esta estructura en el JSON:
# {
#   "nombre": "Andrés",
#   "telefono": "123456789",
#   "email": "andres@email.com"
# }
#
# El archivo JSON guarda una LISTA de contactos:
# [
#   { "nombre": "Andrés", "telefono": "...", "email": "..." },
#   { "nombre": "Brais",  "telefono": "...", "email": "..." }
# ]


# =============================================================================
# PISTAS DE DISEÑO (no son el código — son orientación)
# =============================================================================
# → Necesitas una función para CARGAR el JSON al inicio del programa.
#   Pregunta: ¿qué pasa si el archivo no existe todavía? ¿Qué excepción manejas?
#
# → Necesitas una función para GUARDAR el JSON cada vez que haya un cambio.
#   Pregunta: ¿qué modo de apertura usas para sobrescribir con los datos nuevos?
#
# → Las funciones de agregar, buscar y eliminar trabajan sobre una lista
#   de diccionarios en memoria, y al final llaman a la función de guardar.
#
# → Para buscar y eliminar, necesitas recorrer la lista y comparar nombres.
#   Pregunta: ¿cómo haces la comparación insensible a mayúsculas?
#
# → El menú principal puede ser un bucle while con input() que llame a
#   cada función según lo que elija el usuario.

import json
# =============================================================================
# ESTRUCTURA SUGERIDA (solo los nombres — tú implementas el contenido)
# =============================================================================

# ARCHIVO_JSON = "python_intermedio/agenda.json"


# def cargar_contactos():
#crear una funcion para cargar el archivo json (read)
# usar try except para manejar el error que no exista el archivo
# usar with open para que cierre automaticamente 
# poner la ubicacion del archivo donde abrira el json y se sobreescribira 
# usar el json.load para cargar el archivo. 
# despues del manejo del filenofound retornar una lista vacia     
# 
def cargar_contactos():
    try:
        with open("python_intermedio/agenda.json","r", encoding="utf-8")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []



# def guardar_contactos(contactos):
# crear funcion donde guardar el archivo json    
# usar el with open para cerrado automatico 
#usar la ubicacion donde el archivo se sobreescribira 
# para esto se usa "w" 
# usar el .dump donde adentro ira ident=4 para que sea legible por humanos
# dentro del dump ira el contacto y el archivo donde se sobreescribira 
# usar el ensure_ascii=False para poder que los nombres seal legibles por humanos

def guardar_contactos(contactos):
    with open("python_intermedio/agenda.json","w",encoding="utf-8")as archivo:
        json.dump(contactos, archivo, indent=4, ensure_ascii=False)

# def agregar_contacto(contactos):
# pedir nombre con input()
# pedir telefono con input()
# pedir email con input()
# crear diccionario con esos tres valores
# agregar el diccionario a la lista con append
# llamar a guardar_contactos(contactos)

def agregar_contacto(contactos):
    nombre= input("escribir nombre de nuevo contacto: ")
    telefono= input("escribir telefono de nuevo contacto: ")
    email= input("escribir email de nuevo contacto")
    nuevos = {
        "nombre":nombre,
        "telefono": telefono,
        "email": email
    }
    contactos.append(nuevos)
    guardar_contactos(contactos)


# def ver_contactos(contactos):
#crear fucion ver contactos
#usar bucle for para moverse en el diccionaro key valor

def ver_contactos(contactos):
    for contacto in contactos:
     print(contacto["nombre"])
     print(contacto["telefono"])
     print(contacto["email"])
     print("-" * 30) #solo visual para separar un contacto de otro con (------)
     

# def buscar_contacto(contactos):
#     # pseudocode aquí primero
#     pass


# def eliminar_contacto(contactos):
#     # pseudocode aquí primero
#     pass


# def menu():
#     # pseudocode aquí primero
#     pass


# =============================================================================
# CONCEPTOS QUE VAS A INTEGRAR EN ESTE PROYECTO
# =============================================================================
# ✅ json.load()          → cargar contactos desde el archivo al iniciar
# ✅ json.dump()          → guardar contactos en el archivo al modificar
# ✅ FileNotFoundError    → manejar el caso de que el archivo no exista aún
# ✅ with open()          → abrir archivos correctamente
# ✅ Listas de dicts      → estructura de datos de los contactos en memoria
# ✅ Funciones            → cada operación en su propia función reutilizable
# ✅ Bucle while          → menú que se repite hasta que el usuario salga
# ✅ .lower()             → búsqueda insensible a mayúsculas
# ✅ input()              → interacción con el usuario


# =============================================================================
# DESAFÍO EXTRA (opcional, si terminas antes)
# =============================================================================
# → Validar que el email tenga formato correcto (contiene "@" y ".")
# → No permitir agregar dos contactos con el mismo nombre
# → Mostrar los contactos ordenados alfabéticamente por nombre