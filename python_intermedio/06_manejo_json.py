### JSON EN PYTHON — REFERENCIA COMPLETA ###
# Documentación oficial: https://docs.python.org/3/library/json.html
# Módulo: json (built-in — no requiere instalación)

# =============================================================================
# ¿QUÉ ES JSON Y POR QUÉ ES EL FORMATO MÁS IMPORTANTE EN BACKEND?
# =============================================================================
# JSON (JavaScript Object Notation) es un formato de texto con estructura
# clave-valor. Aunque el nombre dice "JavaScript", es independiente del
# lenguaje y hoy es el estándar universal para comunicación entre sistemas.
#
# ¿POR QUÉ ES EL MÁS IMPORTANTE?
#   → Es el formato que usan TODAS las APIs REST modernas (incluido FastAPI)
#   → Cuando tu frontend le habla a tu backend, lo hace en JSON
#   → Cuando tu backend le habla a otra API (pagos, envíos, mapas), usa JSON
#   → Las bases de datos NoSQL (MongoDB, Firestore) guardan documentos en JSON
#   → Los archivos de configuración de casi todos los proyectos son JSON
#     (package.json, settings.json, appsettings.json, etc.)
#
# EQUIVALENCIAS ENTRE JSON Y PYTHON:
# ┌─────────────────┬────────────────────────────────────────────────────────┐
# │ JSON            │ Python                                                 │
# ├─────────────────┼────────────────────────────────────────────────────────┤
# │ object {}       │ dict                                                   │
# │ array []        │ list                                                   │
# │ string ""       │ str                                                    │
# │ number (int)    │ int                                                    │
# │ number (float)  │ float                                                  │
# │ true / false    │ True / False                                           │
# │ null            │ None                                                   │
# └─────────────────┴────────────────────────────────────────────────────────┘
# OJO: true/false en JSON → True/False en Python (mayúscula distinta)
#      null en JSON       → None en Python
#
# ESTRUCTURA DE UN JSON:
# {
#   "nombre": "Andrés",               ← string
#   "edad": 25,                       ← número
#   "activo": true,                   ← booleano
#   "saldo": null,                    ← null
#   "lenguajes": ["Python", "SQL"],   ← array (lista)
#   "direccion": {                    ← objeto anidado (dict dentro de dict)
#     "ciudad": "Bogotá",
#     "pais": "Colombia"
#   }
# }


import json
import os


# =============================================================================
# 1. LAS CUATRO FUNCIONES PRINCIPALES DEL MÓDULO json
# =============================================================================
# El módulo json tiene 4 funciones que vas a usar constantemente.
# La clave para no confundirlas es distinguir dos ejes:
#
#   1) ¿Trabajas con un ARCHIVO o con un STRING en memoria?
#   2) ¿Lees (deserializas) o escribes (serializas)?
#
# ┌────────────────┬──────────────────────────┬────────────────────────────────┐
# │                │ CON ARCHIVO              │ CON STRING (en memoria)        │
# ├────────────────┼──────────────────────────┼────────────────────────────────┤
# │ LEER/CARGAR    │ json.load(file)          │ json.loads(string)             │
# │ (JSON→Python)  │ lee el archivo           │ parsea el string               │
# ├────────────────┼──────────────────────────┼────────────────────────────────┤
# │ ESCRIBIR/GUARDAR│ json.dump(data, file)   │ json.dumps(data)               │
# │ (Python→JSON)  │ escribe en el archivo    │ devuelve un string             │
# └────────────────┴──────────────────────────┴────────────────────────────────┘
#
# REGLA MNEMOTÉCNICA:
#   load  / dump  → trabajan con ARCHIVOS (disco)
#   loads / dumps → "s" de "string" → trabajan con texto en memoria


# =============================================================================
# 2. DATOS DE EJEMPLO — DICT EN PYTHON
# =============================================================================
# Este dict simula datos que podrían venir de una base de datos o formulario.

paciente = {
    "id": 1,
    "nombre": "Carlos",
    "apellido": "Ramírez",
    "edad": 42,
    "activo": True,
    "historia_clinica": None,           # → null en JSON
    "especialidades_requeridas": [      # lista → array en JSON
        "Cirugía general",
        "Anestesiología"
    ],
    "datos_contacto": {                 # dict anidado → object en JSON
        "ciudad": "Bogotá",
        "telefono": "3001234567"
    }
}


# =============================================================================
# 3. json.dump() — GUARDAR UN DICT/LISTA COMO ARCHIVO JSON
# =============================================================================
# Sintaxis: json.dump(objeto_python, file_handle, **kwargs)
#
# ¿QUÉ HACE INTERNAMENTE?
#   json.dump() toma un objeto Python (dict, list, str, int, bool, None)
#   y lo CONVIERTE a texto JSON, escribiéndolo directamente en el archivo.
#   Es una operación de SERIALIZACIÓN: Python → texto JSON en disco.
#
#   El proceso interno es:
#   1. Recorre el objeto Python (dict, list, etc.)
#   2. Convierte cada tipo al equivalente JSON (True→true, None→null, etc.)
#   3. Escribe el resultado como texto en el file handle que le pasaste
#
# ¿QUÉ ES EL file_handle?
#   Es el objeto que devuelve open(). Cuando escribes:
#     with open("archivo.json", "w") as f:
#         json.dump(datos, f)
#   El "f" es el file handle — json.dump lo usa para saber DÓNDE escribir.
#   json.dump NO abre el archivo por ti. Tú abres el archivo, y le pasas el handle.
#
# MODO DE APERTURA CON json.dump:
#   Casi siempre usarás "w" (write):
#   → "w" SOBREESCRIBE el archivo si existe, o lo CREA si no existe.
#   → Esto es intencional: cada vez que guardas, quieres el estado completo actualizado.
#   → NO uses "a" (append) con json.dump — el resultado sería un JSON inválido
#     porque tendría dos objetos pegados sin separación.
#
# PARÁMETROS MÁS USADOS:
#
#   indent=n
#     → Agrega indentación de n espacios para que el JSON sea legible por humanos.
#     → Sin indent: todo en una línea → más compacto, difícil de leer.
#     → Con indent=4: formato multilínea → fácil de leer y depurar.
#     → Cuándo usar cada uno:
#        indent=4 (o 2) → cuando el archivo lo va a leer una persona
#        sin indent     → cuando el JSON viaja por red (menos bytes)
#
#   ensure_ascii=False
#     → Por defecto (True), json.dump escapa todos los caracteres no-ASCII.
#     → "Ramírez" se guardaría como "Ram\u00edrez" — técnicamente correcto
#       pero ilegible para humanos.
#     → Con ensure_ascii=False, los caracteres se guardan tal cual: "Ramírez"
#     → Regla práctica: si tus datos tienen español, SIEMPRE pon ensure_ascii=False.
#
#   sort_keys=True
#     → Ordena las claves del dict alfabéticamente en el JSON resultante.
#     → Útil cuando quieres comparar dos JSONs o tener salida reproducible.
#     → Por defecto False: las claves salen en el orden del dict original.
#
# ¿CUÁNDO USARLO?
#   → Cada vez que modifiques datos en memoria y quieras persistirlos en disco.
#   → En el miniproyecto: cada vez que agregues, edites o elimines un contacto.

with open("paciente.json", "w", encoding="utf-8") as archivo:
    json.dump(paciente, archivo, indent=4, ensure_ascii=False)
# Resultado en paciente.json:
# {
#     "id": 1,
#     "nombre": "Carlos",
#     "apellido": "Ramírez",
#     ...
# }

# SIN indent (compacto):
with open("paciente_compacto.json", "w", encoding="utf-8") as archivo:
    json.dump(paciente, archivo, ensure_ascii=False)
# Resultado: {"id": 1, "nombre": "Carlos", "apellido": "Ramírez", ...}

# DIFERENCIA VISUAL entre indent y sin indent:
ejemplo = {"nombre": "Andrés", "lenguajes": ["Python", "SQL"], "activo": True}
print("--- SIN indent ---")
print(json.dumps(ejemplo, ensure_ascii=False))
print("--- CON indent=4 ---")
print(json.dumps(ejemplo, ensure_ascii=False, indent=4))


# =============================================================================
# 4. json.load() — CARGAR UN ARCHIVO JSON COMO OBJETO PYTHON
# =============================================================================
# Sintaxis: json.load(file_handle)
#
# ¿QUÉ HACE INTERNAMENTE?
#   json.load() lee TODO el contenido del archivo de una sola vez, interpreta
#   ese texto como JSON válido, y lo convierte al tipo Python equivalente.
#   Es DESERIALIZACIÓN: texto JSON en disco → objeto Python en memoria.
#
#   El proceso interno es:
#   1. Lee el texto completo del archivo desde la posición actual del cursor
#   2. Parsea la estructura JSON (detecta {}, [], "", números, true/false, null)
#   3. Convierte cada elemento al tipo Python correspondiente
#   4. Devuelve el objeto Python resultante
#
# EL TIPO QUE DEVUELVE depende de cómo empieza el JSON en el archivo:
#   Si el archivo contiene { ... }  → devuelve dict
#   Si el archivo contiene [ ... ]  → devuelve list
#   Esto importa porque determina cómo accedes a los datos después.
#   En el miniproyecto, el archivo guarda una LISTA de contactos → devuelve list.
#
# ¿QUÉ ES EL file_handle? (igual que en json.dump)
#   Es el objeto que devuelve open(). json.load NO abre el archivo por ti.
#   Tú abres el archivo con open(), y le pasas el handle a json.load().
#     with open("agenda.json", "r") as f:
#         contactos = json.load(f)   ← f es el file handle
#
# MODO DE APERTURA CON json.load:
#   Siempre "r" (read) — solo necesitas leer el contenido.
#   NUNCA uses "w" para leer — "w" borra el archivo antes de que puedas leerlo.
#
# CUÁNDO EL ARCHIVO NO EXISTE — el caso más importante:
#   Si intentas abrir un archivo que no existe con "r", Python lanza
#   FileNotFoundError ANTES de que json.load() llegue a ejecutarse.
#   El error lo lanza open(), no json.load().
#   Por eso el try/except va ALREDEDOR del open(), no solo alrededor del load.
#
#   Este es el caso que DEBES manejar en cargar_contactos() del miniproyecto:
#   la primera vez que el programa corre, el archivo todavía no existe.
#   La solución es retornar una lista vacía [] en el except FileNotFoundError.
#
# CUÁNDO EL ARCHIVO EXISTE PERO ESTÁ VACÍO O CORRUPTO:
#   json.load() lanza json.JSONDecodeError si el contenido no es JSON válido.
#   Ejemplo: si el archivo existe pero está vacío, json.load() falla.
#   También falla si el JSON tiene errores de sintaxis (coma extra, comillas mal, etc.)
#
# CONVERSIONES DE TIPOS — se restauran automáticamente:
#   true/false en el archivo → True/False en Python
#   null en el archivo       → None en Python
#   números sin comillas     → int o float en Python
#   No tienes que hacer nada extra — json.load() lo hace solo.
#
# DIFERENCIA ENTRE json.load() Y read():
#   archivo.read()     → devuelve el contenido como STRING crudo (texto plano)
#   json.load(archivo) → devuelve el contenido ya convertido a dict/list de Python
#   Si usas read() en lugar de json.load(), obtienes un string que parece JSON
#   pero NO puedes hacer datos["nombre"] — primero tendrías que parsearlo con json.loads().
#   Por eso para JSON siempre usas json.load() directamente.
#
# ¿CUÁNDO USARLO?
#   → Al INICIO del programa para cargar el estado guardado anteriormente.
#   → En el miniproyecto: dentro de cargar_contactos(), es la función central.
#   → Siempre que necesites leer un JSON de disco para trabajar con él en memoria.

with open("paciente.json", "r", encoding="utf-8") as archivo:
    datos_cargados = json.load(archivo)

print(type(datos_cargados))                           # <class 'dict'>
print(datos_cargados["nombre"])                       # Carlos
print(datos_cargados["datos_contacto"]["ciudad"])     # Bogotá — dict anidado
print(datos_cargados["especialidades_requeridas"][0]) # Cirugía general — por índice

# Las conversiones de tipos se restauran automáticamente:
print(datos_cargados["historia_clinica"])   # None  (era null en el archivo)
print(datos_cargados["activo"])             # True  (era true en el archivo)
print(type(datos_cargados["activo"]))       # <class 'bool'>

# PATRÓN DEFENSIVO — el que usarás en cargar_contactos() del miniproyecto:
def cargar_datos_ejemplo():
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []           # primera vez que corre — archivo aún no existe
    except json.JSONDecodeError:
        return []           # archivo existe pero el contenido no es JSON válido


# =============================================================================
# 5. json.dumps() — CONVERTIR DICT/LISTA A STRING JSON (sin archivo)
# =============================================================================
# Sintaxis: json.dumps(objeto_python, **kwargs)
# Mismos parámetros que json.dump() (indent, ensure_ascii, sort_keys...).
# Devuelve un STRING — no crea ningún archivo.
#
# ¿QUÉ HACE INTERNAMENTE?
#   Hace exactamente lo mismo que json.dump() pero en lugar de escribir
#   en un archivo, construye el texto JSON en memoria y te lo devuelve como str.
#   Útil cuando no quieres escribir a disco todavía, o no quieres hacerlo nunca.
#
# ¿CUÁNDO USARLO?
#   → Para imprimir un dict con formato legible en los logs o en pantalla
#   → Para preparar el body de una petición HTTP antes de enviarlo por red
#   → Cuando necesitas el JSON como texto para pasarlo a otra función
#   → Para ver exactamente cómo quedaría serializado un objeto antes de guardarlo

json_string = json.dumps(paciente, indent=4, ensure_ascii=False)
print(type(json_string))    # <class 'str'> — es texto, NO un dict
print(json_string)          # imprime el JSON formateado

# Comparación importante: str(dict) vs json.dumps() — NO son lo mismo:
print(str(paciente))
# {'id': 1, 'nombre': 'Carlos', 'activo': True, 'historia_clinica': None, ...}
# → comillas simples, True/None con mayúscula → NO es JSON válido

print(json.dumps(paciente, ensure_ascii=False))
# {"id": 1, "nombre": "Carlos", "activo": true, "historia_clinica": null, ...}
# → comillas dobles, true/null en minúscula → JSON válido ✓


# =============================================================================
# 6. json.loads() — PARSEAR UN STRING JSON A OBJETO PYTHON
# =============================================================================
# Sintaxis: json.loads(string_json)
# Convierte un STRING que contiene JSON válido → objeto Python.
# La "s" final = string (trabaja con texto en memoria, no con archivo).
#
# ¿QUÉ HACE INTERNAMENTE?
#   Hace exactamente lo mismo que json.load() pero recibe un STRING
#   en lugar de un file handle. Parsea el texto y devuelve el objeto Python.
#
# ¿CUÁNDO USARLO?
#   → Cuando ya tienes el JSON como string en memoria (no en un archivo)
#   → Al recibir la respuesta de una API HTTP (el body viene como string)
#   → Para procesar datos JSON leídos línea por línea con readlines()
#   → Cuando lees JSON de una base de datos que lo guarda como texto

respuesta_api = '{"status": "ok", "codigo": 200, "datos": {"usuario_id": 99}}'
# Esto simula lo que recibirías del body de una respuesta HTTP. Es un STRING.

datos_parseados = json.loads(respuesta_api)
print(type(datos_parseados))                        # <class 'dict'>
print(datos_parseados["status"])                    # ok
print(datos_parseados["datos"]["usuario_id"])       # 99

# json.loads() con lista JSON:
lista_json = '[{"id": 1, "nombre": "Carlos"}, {"id": 2, "nombre": "Ana"}]'
lista_python = json.loads(lista_json)
print(type(lista_python))               # <class 'list'>
print(lista_python[0]["nombre"])        # Carlos


# =============================================================================
# 7. LEER UN JSON LÍNEA POR LÍNEA CON readlines()
# =============================================================================
# readlines() es un método del file handle (del objeto que devuelve open()).
# Devuelve una lista donde cada elemento es una línea del archivo como string.
#
# ¿CUÁNDO TIENE SENTIDO CON JSON?
#   Solo en un formato llamado NDJSON (Newline Delimited JSON), donde cada
#   línea del archivo es un JSON independiente y completo.
#
#   NDJSON es común en:
#   → Archivos de log estructurados (cada evento del sistema es una línea JSON)
#   → Exportaciones de bases de datos (cada registro es una línea JSON)
#
# DIFERENCIA CLAVE:
#   json.load(f)  → para un JSON normal que ocupa todo el archivo (un objeto o lista)
#   readlines()   → para NDJSON donde cada línea es un JSON independiente
#   NO uses readlines() en un JSON normal — json.load() ya lee todo el archivo.

# Crear un archivo NDJSON de ejemplo:
eventos_log = [
    {"timestamp": "2024-01-15T08:00:00", "evento": "login",    "usuario_id": 1},
    {"timestamp": "2024-01-15T08:05:00", "evento": "consulta", "usuario_id": 1},
    {"timestamp": "2024-01-15T08:10:00", "evento": "logout",   "usuario_id": 1},
]

with open("eventos.ndjson", "w", encoding="utf-8") as archivo:
    for evento in eventos_log:
        archivo.write(json.dumps(evento, ensure_ascii=False) + "\n")
# Resultado en eventos.ndjson (cada línea es un JSON completo independiente):
# {"timestamp": "2024-01-15T08:00:00", "evento": "login", "usuario_id": 1}
# {"timestamp": "2024-01-15T08:05:00", "evento": "consulta", "usuario_id": 1}
# {"timestamp": "2024-01-15T08:10:00", "evento": "logout", "usuario_id": 1}

# Leer NDJSON con readlines() + json.loads() por línea:
with open("eventos.ndjson", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    # lineas = [
    #   '{"timestamp": "...", "evento": "login", ...}\n',
    #   '{"timestamp": "...", "evento": "consulta", ...}\n',
    #   ...
    # ]
    # Cada elemento es un STRING. Hay que parsearlo con json.loads() individualmente.

for linea in lineas:
    evento_dict = json.loads(linea.strip())   # .strip() quita el \n del final
    print(evento_dict["evento"])              # login, consulta, logout

# Iterar directamente (más eficiente para archivos grandes — no carga todo):
with open("eventos.ndjson", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        evento_dict = json.loads(linea.strip())
        print(f"[{evento_dict['timestamp']}] {evento_dict['evento']}")


# =============================================================================
# 8. ACTUALIZAR UN ARCHIVO JSON EXISTENTE
# =============================================================================
# JSON no tiene modo "append" como .txt. No puedes agregar al final.
# El patrón obligatorio es: cargar todo → modificar en Python → guardar todo.
#
# ¿POR QUÉ?
#   Porque un JSON es una estructura completa (un objeto o una lista).
#   Si agregas texto al final del archivo, rompes esa estructura y el JSON
#   deja de ser válido. json.load() fallaría con JSONDecodeError.
#
# PATRÓN: cargar → modificar → guardar

with open("paciente.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Modificar el dict en Python:
datos["edad"] = 43
datos["historia_clinica"] = "HC-2024-001"
datos["especialidades_requeridas"].append("Cardiología")

# Guardar los cambios sobreescribiendo el archivo:
with open("paciente.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Verificación:
with open("paciente.json", "r", encoding="utf-8") as archivo:
    datos_actualizados = json.load(archivo)
print(datos_actualizados["edad"])                       # 43
print(datos_actualizados["historia_clinica"])           # HC-2024-001
print(datos_actualizados["especialidades_requeridas"])  # lista con Cardiología añadida


# =============================================================================
# 9. TRABAJAR CON LISTAS DE OBJETOS JSON
# =============================================================================
# En backend es muy común tener un JSON que es una lista de objetos.
# Es exactamente la estructura del miniproyecto: una lista de contactos.

pacientes = [
    {"id": 1, "nombre": "Carlos", "edad": 42},
    {"id": 2, "nombre": "Ana",    "edad": 31},
    {"id": 3, "nombre": "Luis",   "edad": 55},
]

# Guardar lista como JSON:
with open("pacientes.json", "w", encoding="utf-8") as archivo:
    json.dump(pacientes, archivo, indent=4, ensure_ascii=False)

# Cargar lista desde JSON:
with open("pacientes.json", "r", encoding="utf-8") as archivo:
    lista_cargada = json.load(archivo)

print(type(lista_cargada))          # <class 'list'>
print(lista_cargada[0]["nombre"])   # Carlos — primer elemento, clave "nombre"

# Buscar por campo (patrón que usarás en buscar_contacto()):
def buscar_por_nombre(lista, nombre_buscado):
    for p in lista:
        if p["nombre"].lower() == nombre_buscado.lower():  # insensible a mayúsculas
            return p
    return None

resultado = buscar_por_nombre(lista_cargada, "ana")
print(resultado)        # {'id': 2, 'nombre': 'Ana', 'edad': 31}

# Filtrar con list comprehension:
mayores_40 = [p for p in lista_cargada if p["edad"] > 40]
print(mayores_40)       # Carlos y Luis

# Eliminar un elemento por nombre (patrón para eliminar_contacto()):
lista_cargada = [p for p in lista_cargada if p["nombre"].lower() != "luis"]
print(lista_cargada)    # lista sin Luis


# =============================================================================
# 10. MANEJO DE EXCEPCIONES CON JSON
# =============================================================================
# Errores más comunes al trabajar con JSON:
#
#   FileNotFoundError    → el archivo no existe (json.load con "r")
#   json.JSONDecodeError → el contenido no es JSON válido
#   KeyError             → intentas acceder a una clave que no existe en el dict
#   TypeError            → intentas serializar un tipo que JSON no soporta
#                          (datetime, set, bytes, instancias de clases custom)

# FileNotFoundError + JSONDecodeError — los más frecuentes:
try:
    with open("config.json", "r", encoding="utf-8") as archivo:
        config = json.load(archivo)
except FileNotFoundError:
    print("config.json no existe. Usando configuración por defecto.")
    config = {"debug": False, "puerto": 8000}
except json.JSONDecodeError as e:
    print(f"El archivo JSON tiene un error de sintaxis: {e}")
    # e.msg, e.lineno, e.colno te dicen exactamente dónde está el error

# TypeError — al intentar serializar tipos no soportados:
from datetime import datetime

datos_con_fecha = {
    "nombre": "Andrés",
    "creado_en": datetime.now()     # datetime NO es serializable por json
}

try:
    json.dumps(datos_con_fecha)
except TypeError as e:
    print(f"Error de tipo: {e}")
    # Object of type datetime is not JSON serializable

# SOLUCIÓN: convertir a string ISO antes de serializar
datos_con_fecha["creado_en"] = datetime.now().isoformat()
print(json.dumps(datos_con_fecha, ensure_ascii=False))
# {"nombre": "Andrés", "creado_en": "2024-01-15T08:00:00.123456"}

# TIPOS NO SERIALIZABLES POR DEFECTO:
#   datetime → .isoformat() o str()
#   set      → list()
#   bytes    → .decode("utf-8")
#   objetos de clases propias → to_dict() o __dict__


# =============================================================================
# 11. JSON CON CLASES PROPIAS
# =============================================================================
# Las instancias de clases no son serializables por defecto.
# Patrón más simple: método to_dict() que convierte la instancia a dict.

class Instrumento:
    def __init__(self, nombre, codigo, esteril):
        self.nombre = nombre
        self.codigo = codigo
        self.esteril = esteril

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "esteril": self.esteril
        }

bisturi = Instrumento("Bisturí #22", "BS-022", True)

try:
    json.dumps(bisturi)             # falla — el objeto no es serializable
except TypeError as e:
    print(f"No serializable: {e}")

# Usando to_dict():
json_instrumento = json.dumps(bisturi.to_dict(), ensure_ascii=False, indent=2)
print(json_instrumento)

# Para reconstruir el objeto desde el JSON:
datos_dict = json.loads(json_instrumento)
instrumento_restaurado = Instrumento(**datos_dict)  # ** desempaqueta el dict como kwargs
print(instrumento_restaurado.nombre)    # Bisturí #22


# =============================================================================
# 12. PARÁMETROS — REFERENCIA RÁPIDA
# =============================================================================

# indent — indentación para legibilidad humana
print(json.dumps({"a": 1, "b": [1, 2]}, indent=2))
# {
#   "a": 1,
#   "b": [1, 2]
# }

# sort_keys — claves ordenadas alfabéticamente
print(json.dumps({"z": 3, "a": 1, "m": 2}, sort_keys=True))
# {"a": 1, "m": 2, "z": 3}

# ensure_ascii — controla si se escapan los caracteres especiales
print(json.dumps({"ciudad": "Bogotá"}, ensure_ascii=True))
# {"ciudad": "Bogot\u00e1"}   ← ilegible para humanos
print(json.dumps({"ciudad": "Bogotá"}, ensure_ascii=False))
# {"ciudad": "Bogotá"}        ← legible ✓

# separators — elimina espacios para minimizar tamaño (útil en red)
print(json.dumps({"a": 1, "b": 2}, separators=(",", ":")))
# {"a":1,"b":2}  ← sin espacios = menos bytes


# =============================================================================
# 13. BUENAS PRÁCTICAS — RESUMEN
# =============================================================================
# ✅ Siempre usar with open(...) — cierre automático del archivo
# ✅ Siempre especificar encoding="utf-8" — evita problemas con ñ y acentos
# ✅ Usar ensure_ascii=False al guardar texto en español
# ✅ Usar indent=4 cuando el archivo lo van a leer personas
# ✅ Manejar FileNotFoundError y json.JSONDecodeError al leer archivos
# ✅ Patrón para archivos JSON: cargar → modificar en memoria → guardar completo
#
# ❌ No usar "a" (append) con json.dump → rompe el JSON
# ❌ No olvidar .strip() al parsear líneas leídas con readlines()
# ❌ No intentar json.dump() con datetime, set, bytes o instancias de clases sin convertir
# ❌ No confundir json.dump (archivo) con json.dumps (string)
# ❌ No confundir json.load (archivo) con json.loads (string)


# =============================================================================
# 14. FLUJO COMPLETO — SIMULACIÓN DEL MINIPROYECTO
# =============================================================================
# Mismas funciones que vas a implementar: cargar, guardar, agregar, eliminar.
# Aquí están implementadas para que veas el patrón completo funcionando.
# NO las copies al ejercicio — úsalas solo como referencia de la lógica.

BASE_DATOS = "registro_pacientes.json"

def cargar_pacientes():
    """Carga el archivo JSON. Si no existe, retorna lista vacía."""
    try:
        with open(BASE_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Advertencia: archivo corrupto. Iniciando vacío.")
        return []

def guardar_pacientes(lista):
    """Sobreescribe el archivo JSON con el estado actual de la lista."""
    with open(BASE_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)

def agregar_paciente(nombre, edad):
    """Carga → agrega → guarda."""
    pacientes_actuales = cargar_pacientes()
    nuevo = {"nombre": nombre, "edad": edad}
    pacientes_actuales.append(nuevo)
    guardar_pacientes(pacientes_actuales)
    print(f"Paciente '{nombre}' agregado.")

def eliminar_paciente(nombre):
    """Carga → filtra → guarda."""
    pacientes_actuales = cargar_pacientes()
    filtrados = [p for p in pacientes_actuales if p["nombre"].lower() != nombre.lower()]
    if len(filtrados) == len(pacientes_actuales):
        print(f"No se encontró '{nombre}'.")
    else:
        guardar_pacientes(filtrados)
        print(f"Paciente '{nombre}' eliminado.")

# Uso:
agregar_paciente("María", 38)
agregar_paciente("Jorge", 61)
agregar_paciente("Ana", 29)

todos = cargar_pacientes()
for p in todos:
    print(f"{p['nombre']} — {p['edad']} años")

eliminar_paciente("Jorge")

todos = cargar_pacientes()
for p in todos:
    print(f"{p['nombre']} — {p['edad']} años")

# Limpieza (descomenta para borrar los archivos creados en esta sesión):
# for f in ["paciente.json", "paciente_compacto.json", "pacientes.json",
#           "eventos.ndjson", "registro_pacientes.json"]:
#     if os.path.exists(f):
#         os.remove(f)