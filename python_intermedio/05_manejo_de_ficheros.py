### FILE HANDLING EN PYTHON ###
# Documentación oficial: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Módulos: os, json, csv (built-in — no requieren instalación)

# =============================================================================
# ¿QUÉ ES EL MANEJO DE FICHEROS Y POR QUÉ IMPORTA EN BACKEND?
# =============================================================================
# Trabajar con ficheros es una de las habilidades más fundamentales en backend.
# Prácticamente cualquier aplicación real necesita persistir datos: guardar
# configuraciones, registrar logs, importar/exportar información, comunicarse
# con otros sistemas, etc.
#
# Python ofrece herramientas nativas (built-in) para los formatos más comunes,
# sin necesidad de instalar nada extra.
#
# TIPOS DE ARCHIVOS QUE VEREMOS:
# ┌─────────┬─────────────────────────────────────────────────────────────────┐
# │ .txt    │ Texto plano. El más básico. Logs, notas, configuraciones simples │
# │ .json   │ Intercambio de datos entre sistemas. El estándar de las APIs     │
# │ .csv    │ Tablas de datos. Exportar/importar desde bases de datos, Excel   │
# │ .xml    │ Configs y APIs antiguas (SOAP). Más verboso que JSON             │
# │ .xlsx   │ Hojas de cálculo de Excel. Requiere módulo externo (openpyxl)   │
# └─────────┴─────────────────────────────────────────────────────────────────┘


# =============================================================================
# ARCHIVO .TXT — ¿QUÉ ES Y PARA QUÉ SIRVE?
# =============================================================================
# Un archivo .txt es texto plano sin ningún formato especial.
# No tiene estructura interna — es simplemente una secuencia de caracteres.
#
# ¿PARA QUÉ SE USA EN BACKEND?
#   → Archivos de log: registrar eventos, errores, actividad del sistema
#   → Archivos de configuración simples (antes de que JSON/YAML se popularizaran)
#   → Guardar resultados de procesos en texto legible
#   → Almacenar datos temporales o de prueba
#   → Exportar reportes en texto simple
#
# ¿CUÁNDO ELEGIR .TXT?
#   → Cuando los datos no tienen estructura (no son tabla ni jerarquía)
#   → Cuando necesitas que cualquier persona pueda abrirlo y leerlo sin software especial
#   → Para logs o registros cronológicos simples
#
# EJEMPLO REAL EN BACKEND:
#   Un script que procesa pedidos escribe en un .txt cada vez que un pedido
#   falla, con timestamp y detalle del error → archivo de log manual.


# =============================================================================
# ARCHIVO .JSON — ¿QUÉ ES Y PARA QUÉ SIRVE?
# =============================================================================
# JSON (JavaScript Object Notation) es un formato de texto con estructura
# clave-valor, similar a un diccionario de Python.
#
# Ejemplo de un JSON:
# {
#   "nombre": "Andrés",
#   "edad": 25,
#   "lenguajes": ["Python", "SQL"]
# }
#
# ¿PARA QUÉ SE USA EN BACKEND?
#   → Es EL formato estándar para comunicación entre APIs (REST APIs)
#   → Archivos de configuración de proyectos (package.json, settings.json, etc.)
#   → Guardar y transportar datos estructurados entre servicios
#   → Respuestas y peticiones HTTP (cuando FastAPI devuelve datos, los devuelve en JSON)
#   → Bases de datos NoSQL como MongoDB almacenan documentos en formato JSON
#
# ¿CUÁNDO ELEGIR .JSON sobre .TXT?
#   → Cuando los datos tienen estructura jerárquica (objetos anidados, listas)
#   → Cuando necesitas que otra aplicación o API consuma esos datos
#   → Cuando necesitas tipos de datos: numbers, booleans, null, arrays, objects
#
# EJEMPLO REAL EN BACKEND:
#   Un endpoint de FastAPI recibe una petición con datos de un usuario en JSON,
#   los procesa, y devuelve una respuesta también en JSON.
#   Tu app guarda la configuración del servidor en un config.json.


# =============================================================================
# ARCHIVO .CSV — ¿QUÉ ES Y PARA QUÉ SIRVE?
# =============================================================================
# CSV (Comma-Separated Values) es un formato de texto para representar
# datos tabulares — como una hoja de cálculo en texto plano.
#
# Ejemplo de un CSV:
#   name,surname,age
#   Andrés,Palacios,25
#   Brais,Moure,35
#
# ¿PARA QUÉ SE USA EN BACKEND?
#   → Importar y exportar datos de bases de datos (MySQL, PostgreSQL)
#   → Compartir datos entre sistemas que no hablan el mismo lenguaje
#   → Reportes que el cliente va a abrir en Excel
#   → Migraciones de datos entre sistemas
#   → Análisis de datos con pandas (data science/ML pipelines)
#   → Logs estructurados cuando necesitas columnas fijas
#
# ¿CUÁNDO ELEGIR .CSV sobre .JSON?
#   → Cuando los datos son planos (tabla sin jerarquía ni anidamiento)
#   → Cuando el destino final es Excel u otra hoja de cálculo
#   → Cuando necesitas compatibilidad máxima con herramientas de datos
#   → Para datasets grandes (CSV es más compacto que JSON para tablas)
#
# EJEMPLO REAL EN BACKEND:
#   Un sistema de gestión exporta todos los pacientes a un CSV para que
#   el área administrativa los importe en su hoja de cálculo.
#   Un script importa un CSV con inventario y lo carga en la base de datos.


# =============================================================================
# ARCHIVO .XML — ¿QUÉ ES Y PARA QUÉ SIRVE?
# =============================================================================
# XML (eXtensible Markup Language) es un formato de texto con etiquetas,
# similar a HTML pero para datos. Es más verboso que JSON.
#
# Ejemplo de un XML:
#   <usuario>
#     <nombre>Andrés</nombre>
#     <edad>25</edad>
#   </usuario>
#
# ¿PARA QUÉ SE USA EN BACKEND?
#   → APIs antiguas (protocolo SOAP, que precede a REST)
#   → Configuración de frameworks Java (Spring, Maven) y .NET
#   → Archivos de configuración de sistemas empresariales
#   → Intercambio de datos con sistemas legacy (bancarios, hospitalarios)
#   → Sitemap.xml para SEO, RSS feeds para blogs/noticias
#
# ¿CUÁNDO ELEGIR .XML?
#   → Generalmente cuando el sistema con el que interactúas ya lo usa
#   → Para nuevos proyectos, JSON es casi siempre mejor opción
#
# EJEMPLO REAL EN BACKEND:
#   Un hospital usa un sistema legacy que solo acepta datos de pacientes
#   en formato XML (estándar HL7). Tu backend convierte los datos a XML
#   antes de enviarlos.


# =============================================================================
# ARCHIVO .XLSX — ¿QUÉ ES Y PARA QUÉ SIRVE?
# =============================================================================
# XLSX es el formato de Microsoft Excel. A diferencia de CSV, puede tener
# múltiples hojas, fórmulas, estilos, colores, gráficos, etc.
#
# ¿PARA QUÉ SE USA EN BACKEND?
#   → Generar reportes formateados para clientes o directivos
#   → Importar datos desde archivos Excel que envían usuarios o proveedores
#   → Exportar resultados de análisis con formato profesional
#   → Automatizar la generación de informes periódicos
#
# ¿CUÁNDO ELEGIR .XLSX sobre .CSV?
#   → Cuando necesitas múltiples hojas o formato visual (colores, anchos)
#   → Cuando el cliente espera específicamente un archivo Excel
#   → Cuando los datos tienen fórmulas que deben conservarse
#
# MÓDULO: openpyxl (pip install openpyxl)
# EJEMPLO REAL EN BACKEND:
#   Tu app genera automáticamente el reporte mensual de ventas en Excel
#   con una hoja por región y totales resaltados en verde/rojo.


import json
import csv
import os


# =============================================================================
# 1. ARCHIVOS .TXT — MODOS DE APERTURA
# =============================================================================
# open(archivo, modo) es la función nativa de Python para abrir ficheros.
# Siempre hay que cerrar el fichero después de usarlo (con .close() o with).
#
# Modos principales:
#   "r"  → read:  solo lectura. Error si el archivo no existe. (DEFAULT)
#   "w"  → write: escritura. SOBRESCRIBE si ya existe, lo crea si no existe.
#   "a"  → append: agrega al final. No borra el contenido existente.
#   "x"  → exclusive create: crea archivo nuevo. Error si ya existe.
#   "r+" → lectura Y escritura. El archivo debe existir.
#   "w+" → lectura Y escritura. Crea o SOBRESCRIBE.
#   "a+" → lectura Y escritura al final. Crea si no existe.
#
# Agregar "b" al modo → modo binario: "rb", "wb" (para imágenes, PDFs, etc.)


# =============================================================================
# 2. ESCRIBIR EN UN ARCHIVO .TXT
# =============================================================================
# "w+" crea el archivo si no existe, o lo sobrescribe si ya existe.
# El cursor queda al FINAL después de escribir.

txt_file = open("my_file.txt", "w+")

txt_file.write("Mi nombre es Andrés\nMi apellido es Palacios\n25 años\nY mi lenguaje preferido es Python")
# \n es el salto de línea dentro del string


# =============================================================================
# 3. seek() — MOVER EL CURSOR DENTRO DEL ARCHIVO
# =============================================================================
# Después de escribir, el cursor está al final del archivo.
# seek(n) mueve el cursor a la posición n (en bytes desde el inicio).
# seek(0) → va al inicio del archivo.
# Sin seek(0), read() devuelería string vacío porque el cursor ya está al final.

txt_file.seek(0)
print(txt_file.read())          # Lee TODO el contenido desde el inicio


# =============================================================================
# 4. LEER ARCHIVOS — read(), readline(), readlines()
# =============================================================================

# --- read(n) → lee n caracteres desde la posición actual del cursor ---
txt_file.seek(0)
print(txt_file.read(10))        # Lee los primeros 10 caracteres
# El cursor ahora está en la posición 10.

# --- readline() → lee una línea completa (hasta \n) desde la posición actual ---
print(txt_file.readline())      # Lee el RESTO de la línea actual (desde pos 10)
print(txt_file.readline())      # Lee la siguiente línea completa

# --- readlines() → devuelve una lista con todas las líneas restantes ---
for line in txt_file.readlines():
    print(line)
# Nota: cada elemento incluye el \n al final. Puedes usar .strip() para quitarlo.

# --- Iterar directamente sobre el fichero (más eficiente en memoria) ---
# txt_file.seek(0)
# for line in txt_file:
#     print(line.strip())


# =============================================================================
# 5. AGREGAR CONTENIDO SIN SOBRESCRIBIR — modo "a"
# =============================================================================
# write() también puede llamarse después de mover el cursor con seek().
# Si el archivo fue abierto con "w+", puedes escribir en cualquier posición.

txt_file.write("\nAunque también me gusta Kotlin")

txt_file.seek(0)
print(txt_file.read())

txt_file.close()                # Siempre cerrar el fichero cuando ya no se usa


# =============================================================================
# 6. CONTEXTO with — LA FORMA RECOMENDADA (cierre automático)
# =============================================================================
# with open(...) as f: cierra el archivo automáticamente al salir del bloque,
# incluso si ocurre una excepción. Es la práctica estándar en Python.

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")
# El archivo se cierra solo al salir del bloque with.

# Leer con with:
with open("my_file.txt", "r") as f:
    content = f.read()
    print(content)


# =============================================================================
# 7. MÓDULO os — OPERACIONES CON ARCHIVOS Y DIRECTORIOS
# =============================================================================
# os permite interactuar con el sistema operativo: rutas, carpetas, archivos.
# Documentación: https://docs.python.org/3/library/os.html

# Verificar si un archivo existe antes de operar sobre él
if os.path.exists("my_file.txt"):
    print("El archivo existe")

# os.remove() → elimina un archivo
# os.remove("my_file.txt")      # Descomenta para eliminar

# os.rename() → renombra un archivo
# os.rename("my_file.txt", "nuevo_nombre.txt")

# os.getcwd() → devuelve el directorio de trabajo actual (current working directory)
print(os.getcwd())

# os.listdir() → lista los archivos y carpetas de un directorio
print(os.listdir("."))          # "." = directorio actual

# os.makedirs() → crea carpetas (incluyendo intermedias si no existen)
# os.makedirs("carpeta/subcarpeta", exist_ok=True)


# =============================================================================
# 8. ARCHIVOS .JSON
# =============================================================================
# JSON (JavaScript Object Notation) es el formato estándar para intercambio de
# datos entre sistemas (APIs, bases de datos, configuración).
# En Python, un JSON es equivalente a un diccionario (o lista de diccionarios).
# Módulo: json (built-in)
# Documentación: https://docs.python.org/3/library/json.html
#
# json.dump()  → escribe un dict de Python a un archivo JSON
# json.load()  → lee un archivo JSON y lo convierte a dict de Python
# json.dumps() → convierte un dict a STRING JSON (sin archivo)
# json.loads() → convierte un STRING JSON a dict de Python

json_data = {
    "name": "Andrés",
    "surname": "Palacios",
    "age": 25,
    "languages": ["Python", "SQL"],
    "website": "https://github.com/andrespalacios-24"
}

# Escribir JSON en archivo
with open("my_file.json", "w+") as json_file:
    json.dump(json_data, json_file, indent=2)
    # indent=2 → indentación para que el JSON sea legible por humanos
    # ensure_ascii=False → permite caracteres especiales como ñ, á, etc.

# Leer JSON como texto línea por línea
with open("my_file.json") as json_file:
    for line in json_file.readlines():
        print(line, end="") # el end cancela el \n automático de print para no duplicar los saltos de línea que ya vienen en el archivo.

# Leer JSON y convertirlo a dict de Python (lo más común en backend)
with open("my_file.json") as json_file:
    json_dict = json.load(json_file)

print(json_dict)                # {'name': 'Andrés', 'surname': 'Palacios', ...}
print(type(json_dict))          # <class 'dict'>
print(json_dict["name"])        # Andrés
print(json_dict["languages"])   # ['Python', 'SQL']

# json.dumps() — útil para logging o enviar datos por red
json_string = json.dumps(json_data, indent=2, ensure_ascii=False)
print(json_string)              # Imprime el JSON como string formateado


# =============================================================================
# 9. ARCHIVOS .CSV
# =============================================================================
# CSV (Comma Separated Values) es el formato más común para tablas y datos.
# Cada línea es una fila; los valores se separan por coma (u otro delimitador).
# Módulo: csv (built-in)
# Documentación: https://docs.python.org/3/library/csv.html
#
# csv.writer()  → para escribir filas en el archivo
# csv.reader()  → para leer el archivo fila por fila como listas
# csv.DictWriter() → escribe usando diccionarios (más legible en código)
# csv.DictReader() → lee el CSV y convierte cada fila en un diccionario

# Escribir CSV
with open("my_file.csv", "w+", newline="") as csv_file:
    # newline="" es necesario en Windows para evitar filas vacías extra
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["name", "surname", "age", "language", "website"])  # cabecera
    csv_writer.writerow(["Andrés", "Palacios", 25, "Python", "https://github.com/andrespalacios-24"])
    csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])

# Leer CSV línea por línea como texto
with open("my_file.csv") as csv_file:
    for line in csv_file.readlines():
        print(line, end="")

print()

# Leer CSV con csv.reader → cada fila es una lista
with open("my_file.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader: #row solo es una variable que significa fila en ingles
        print(row)              # ['name', 'surname', 'age', ...]

# Leer CSV con DictReader → cada fila es un diccionario (más práctico en backend)
with open("my_file.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(dict(row))        # {'name': 'Andrés', 'surname': 'Palacios', ...}
        print(row["name"])      # Acceso directo por nombre de columna


# =============================================================================
# 10. BUENAS PRÁCTICAS — RESUMEN
# =============================================================================
# ✅ Siempre usar `with open(...)` para abrir archivos (cierre automático)
# ✅ Especificar encoding explícitamente para evitar errores con caracteres especiales:
#    with open("file.txt", "r", encoding="utf-8") as f:
# ✅ Verificar si el archivo existe antes de leerlo (os.path.exists)
# ✅ Usar json.dump con ensure_ascii=False para manejar ñ, acentos, etc.
# ✅ Usar newline="" en csv.writer para evitar líneas vacías en Windows
# ✅ Cerrar archivos con close() si no usas with (aunque with es siempre mejor)
#
# ❌ No abrir en modo "w" si necesitas conservar el contenido existente → usa "a"
# ❌ No olvidar seek(0) antes de leer si acabas de escribir con el mismo file handle
# ❌ No encadenar read() sin seek() entre medio — el cursor no se resetea solo


# =============================================================================
# 11. MANEJO DE EXCEPCIONES CON FICHEROS (integración con lo ya visto)
# =============================================================================
# Los errores más comunes al trabajar con archivos:
#   FileNotFoundError → el archivo no existe (modo "r" o "r+")
#   PermissionError   → sin permisos para leer/escribir
#   IsADirectoryError → intentaste abrir una carpeta como archivo

try:
    with open("archivo_que_no_existe.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: el archivo no existe.")
except PermissionError:
    print("Error: no tienes permisos para acceder a este archivo.")
except Exception as e:
    print(f"Error inesperado: {e}")


# =============================================================================
# FORMATOS ADICIONALES MENCIONADOS POR MOUREDEV
# =============================================================================
# .xml  → módulo xml.etree.ElementTree (built-in)
#         más verboso que json, usado en configs y APIs antiguas
#         doc: https://docs.python.org/3/library/xml.etree.elementtree.html
#
# .xlsx → requiere instalar openpyxl o xlrd:
#         pip install openpyxl
#         doc: https://openpyxl.readthedocs.io/
#
# Ejemplo básico con openpyxl (descomenta si tienes el módulo):
# import openpyxl
# wb = openpyxl.Workbook()
# ws = wb.active
# ws["A1"] = "Nombre"
# ws["B1"] = "Edad"
# wb.save("my_file.xlsx") 