"""
MÓDULO os — Referencia completa con contexto backend
=====================================================
El módulo `os` es la interfaz de Python con el sistema operativo.
Te permite trabajar con archivos, carpetas, rutas, variables de entorno
y procesos de forma portable: el mismo código corre en Linux, macOS y Windows.

En backend se usa constantemente:
    - Leer configuración desde variables de entorno (API keys, passwords)
    - Crear carpetas de uploads, logs, exports en tiempo de ejecución
    - Listar y procesar archivos de un directorio (logs, CSVs, imágenes)
    - Construir rutas de forma portátil sin hardcodear "/" o "\\"
    - Verificar que un archivo existe antes de abrirlo o moverlo

import os   # siempre disponible, no necesitas instalar nada
"""

import os


# ══════════════════════════════════════════════════════════════════════════════
# 1. RUTAS — os.path
# ══════════════════════════════════════════════════════════════════════════════
# os.path es un submódulo dedicado 100% a manipular rutas como strings.
# La regla de oro: NUNCA construyas rutas concatenando strings con "/" o "\\".
# Usa os.path para que tu código funcione en cualquier sistema operativo.

# ── os.path.join() ────────────────────────────────────────────────────────────
# Une partes de una ruta con el separador correcto del SO actual.
# En Linux/macOS usa "/", en Windows usa "\\". Tú nunca te preocupas por eso.

ruta = os.path.join("proyectos", "backend", "datos.csv")
print(ruta)  # proyectos/backend/datos.csv  (en Linux)

# Caso real: construir la ruta de un archivo de configuración
BASE_DIR = os.path.dirname(__file__)          # carpeta donde está este script
CONFIG   = os.path.join(BASE_DIR, "config", "settings.json")
UPLOADS  = os.path.join(BASE_DIR, "uploads")

# También puedes encadenar con una ruta absoluta como punto de partida
LOG_FILE = os.path.join("/var", "log", "mi_app", "errores.log")

# ── os.path.split() y os.path.splitext() ──────────────────────────────────────
# split()     → separa la ruta en (carpeta_padre, nombre_archivo)
# splitext()  → separa el nombre en (nombre_sin_extension, extension)
# Ambas retornan una tupla de dos elementos.

carpeta, archivo = os.path.split("/home/andres/documentos/reporte.pdf")
print(carpeta)   # /home/andres/documentos
print(archivo)   # reporte.pdf

nombre, ext = os.path.splitext("reporte.pdf")
print(nombre)    # reporte
print(ext)       # .pdf   ← incluye el punto

# Caso real: validar que un upload tiene extensión permitida
def extension_permitida(nombre_archivo, permitidas=("jpg", "jpeg", "png", "pdf")):
    _, ext = os.path.splitext(nombre_archivo)
    return ext.lstrip(".").lower() in permitidas

print(extension_permitida("foto.JPG"))    # True
print(extension_permitida("virus.exe"))  # False

# ── os.path.basename() y os.path.dirname() ───────────────────────────────────
# basename() → solo el nombre final (archivo o carpeta más interna)
# dirname()  → todo el camino excepto el nombre final

ruta_completa = "/home/andres/proyectos/app.py"
print(os.path.basename(ruta_completa))   # app.py
print(os.path.dirname(ruta_completa))    # /home/andres/proyectos

# Caso real: saber en qué carpeta está el script que se está ejecutando
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# ── os.path.abspath() ────────────────────────────────────────────────────────
# Convierte una ruta relativa en ruta absoluta, usando el directorio actual.

print(os.path.abspath("datos"))          # /home/andres/BACKEND/datos  (ejemplo)
print(os.path.abspath("."))             # directorio de trabajo actual

# ── os.path.exists() / isfile() / isdir() ────────────────────────────────────
# Antes de operar sobre algo, siempre verifica que existe y qué tipo es.

ruta_prueba = "/tmp/prueba.txt"

os.path.exists(ruta_prueba)   # True si existe (archivo O carpeta)
os.path.isfile(ruta_prueba)   # True solo si es un archivo
os.path.isdir("/tmp")         # True solo si es una carpeta

# Caso real: no procesar algo que no existe
def procesar_csv(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        print(f"ERROR: '{ruta_archivo}' no es un archivo válido.")
        return
    # ... procesar


# ── os.path.getsize() ────────────────────────────────────────────────────────
# Retorna el tamaño del archivo en bytes.

# tamanio = os.path.getsize("foto.jpg")  # ej: 204800  (200 KB)
# print(f"{tamanio / 1024:.1f} KB")

# Caso real: rechazar uploads que superen un límite
def upload_valido(ruta_archivo, max_mb=5):
    tamanio_bytes = os.path.getsize(ruta_archivo)
    return tamanio_bytes <= max_mb * 1024 * 1024


# ══════════════════════════════════════════════════════════════════════════════
# 2. LISTAR CONTENIDO DE UN DIRECTORIO
# ══════════════════════════════════════════════════════════════════════════════

# ── os.listdir(ruta) ─────────────────────────────────────────────────────────
# Retorna una lista con los NOMBRES (no rutas completas) de todo lo que hay
# en la carpeta: archivos, subcarpetas, enlaces simbólicos. Todo mezclado.
# El orden no está garantizado.

contenido = os.listdir("/tmp")            # ["archivo.txt", "subcarpeta", ...]
# contenido = os.listdir(".")             # lista el directorio actual

# Caso real: filtrar solo archivos (sin subcarpetas)
carpeta = "/tmp"
solo_archivos = [
    nombre for nombre in os.listdir(carpeta)
    if os.path.isfile(os.path.join(carpeta, nombre))
    # ↑ IMPORTANTE: isfile necesita la ruta completa, no solo el nombre
]

# Filtrar por extensión
csvs = [
    nombre for nombre in os.listdir(carpeta)
    if nombre.endswith(".csv")
]

# ── os.walk(ruta) ─────────────────────────────────────────────────────────────
# Recorre un árbol de directorios de forma recursiva.
# En cada iteración retorna una tupla: (carpeta_actual, subcarpetas, archivos)
# Úsalo cuando necesitas procesar una carpeta y TODAS sus subcarpetas.

for carpeta_actual, subcarpetas, archivos in os.walk("/tmp"):
    for nombre_archivo in archivos:
        ruta_completa = os.path.join(carpeta_actual, nombre_archivo)
        print(ruta_completa)

# Caso real: buscar todos los .log en un árbol de directorios
def encontrar_logs(directorio_raiz):
    logs_encontrados = []
    for carpeta_actual, _, archivos in os.walk(directorio_raiz):
        for nombre in archivos:
            if nombre.endswith(".log"):
                logs_encontrados.append(os.path.join(carpeta_actual, nombre))
    return logs_encontrados

# os.listdir → un solo nivel, rápido
# os.walk    → recursivo, para árboles completos


# ══════════════════════════════════════════════════════════════════════════════
# 3. CREAR Y ELIMINAR CARPETAS
# ══════════════════════════════════════════════════════════════════════════════

# ── os.mkdir(ruta) ───────────────────────────────────────────────────────────
# Crea UNA sola carpeta. Falla si ya existe o si el padre no existe.

# os.mkdir("logs")                   # crea carpeta "logs" en el directorio actual
# os.mkdir("/tmp/nueva_carpeta")

# ── os.makedirs(ruta, exist_ok=False) ────────────────────────────────────────
# Crea la carpeta Y todos los padres intermedios que falten.
# exist_ok=True → no lanza error si la carpeta ya existe.
# En backend casi siempre usarás makedirs con exist_ok=True.

os.makedirs("uploads/imagenes/2024", exist_ok=True)
# Si uploads/ o uploads/imagenes/ no existen, los crea automáticamente.
# Si ya existen, no hace nada. No lanza FileExistsError.

# Caso real: preparar estructura de carpetas al iniciar la app
def inicializar_estructura():
    carpetas = ["uploads", "logs", "exports", "tmp"]
    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)
    print("Estructura de carpetas lista.")

# ── os.rmdir(ruta) ───────────────────────────────────────────────────────────
# Elimina una carpeta vacía. Si tiene contenido, lanza OSError.
# Para eliminar carpetas con contenido usa shutil.rmtree() (ver archivo shutil).

# os.rmdir("carpeta_vacia")

# ── os.remove(ruta) ──────────────────────────────────────────────────────────
# Elimina un ARCHIVO. No funciona con carpetas.

# os.remove("archivo_temporal.txt")

# Caso real: eliminar un archivo temporal después de procesarlo
def limpiar_temporal(ruta_archivo):
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)


# ══════════════════════════════════════════════════════════════════════════════
# 4. RENOMBRAR Y MOVER (básico)
# ══════════════════════════════════════════════════════════════════════════════

# ── os.rename(origen, destino) ───────────────────────────────────────────────
# Renombra un archivo o carpeta. También sirve para mover dentro del mismo
# sistema de archivos. Para mover entre discos distintos, usa shutil.move().

# os.rename("reporte_v1.pdf", "reporte_final.pdf")
# os.rename("datos/archivo.csv", "backups/archivo.csv")   # mover

# Diferencia clave:
# os.rename  → rápido, mismo filesystem, falla si el destino existe
# shutil.move → más robusto, funciona entre discos distintos


# ══════════════════════════════════════════════════════════════════════════════
# 5. VARIABLES DE ENTORNO — os.environ
# ══════════════════════════════════════════════════════════════════════════════
# Las variables de entorno son la forma estándar de pasar configuración
# a una aplicación backend sin escribirla en el código.
# Ejemplos: DATABASE_URL, SECRET_KEY, API_KEY, DEBUG, PORT.

# ── os.environ ───────────────────────────────────────────────────────────────
# Es un diccionario con todas las variables de entorno del proceso actual.

# Leer una variable (lanza KeyError si no existe)
# home = os.environ["HOME"]

# ── os.environ.get(clave, valor_por_defecto) ─────────────────────────────────
# La forma SEGURA de leer: retorna None (o el default) si no existe.
# Nunca uses os.environ[] directamente en producción.

PORT    = os.environ.get("PORT", "8000")          # default "8000"
DEBUG   = os.environ.get("DEBUG", "false")
DB_URL  = os.environ.get("DATABASE_URL", "")

# Caso real: configuración típica de un backend
class Config:
    SECRET_KEY   = os.environ.get("SECRET_KEY", "dev-key-insegura")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///local.db")
    DEBUG        = os.environ.get("DEBUG", "false").lower() == "true"
    PORT         = int(os.environ.get("PORT", 8000))

# ── os.getenv() ──────────────────────────────────────────────────────────────
# Alias exacto de os.environ.get(). Elige uno y úsalo consistentemente.

api_key = os.getenv("API_KEY", "")          # equivalente a environ.get

# ── Establecer variables de entorno (en el proceso actual) ───────────────────
os.environ["MI_VARIABLE"] = "mi_valor"
# Solo afecta al proceso Python actual, no al shell ni a otros procesos.


# ══════════════════════════════════════════════════════════════════════════════
# 6. DIRECTORIO DE TRABAJO — getcwd / chdir
# ══════════════════════════════════════════════════════════════════════════════

# ── os.getcwd() ──────────────────────────────────────────────────────────────
# Retorna el directorio de trabajo actual (Current Working Directory).
# Es el punto de referencia para todas las rutas relativas.

directorio_actual = os.getcwd()
print(directorio_actual)   # /home/andres/BACKEND  (ejemplo)

# ── os.chdir(ruta) ───────────────────────────────────────────────────────────
# Cambia el directorio de trabajo. Úsalo con precaución en scripts,
# puede afectar al resto del programa si usa rutas relativas.

# os.chdir("/home/andres/BACKEND")


# ══════════════════════════════════════════════════════════════════════════════
# 7. INFORMACIÓN DEL SISTEMA
# ══════════════════════════════════════════════════════════════════════════════

# ── os.name ──────────────────────────────────────────────────────────────────
# "posix" en Linux/macOS, "nt" en Windows.
print(os.name)   # "posix" en tu WSL/Ubuntu

# ── os.sep ───────────────────────────────────────────────────────────────────
# Separador de rutas del SO actual: "/" en Linux, "\\" en Windows.
# Rara vez lo necesitas si usas os.path.join().
print(os.sep)    # /

# ── os.getpid() ──────────────────────────────────────────────────────────────
# ID del proceso actual. Útil en logs para identificar workers.
print(os.getpid())   # ej: 12345

# Caso real: identificar al worker en un servidor con múltiples procesos
# logger.info(f"Worker PID={os.getpid()} procesando request")


# ══════════════════════════════════════════════════════════════════════════════
# 8. RESUMEN — CUÁNDO USAR CADA FUNCIÓN
# ══════════════════════════════════════════════════════════════════════════════
"""
RUTAS
    os.path.join()          → construir rutas portátiles (usa siempre esto)
    os.path.split()         → separar carpeta y nombre de archivo
    os.path.splitext()      → separar nombre y extensión
    os.path.basename()      → obtener solo el nombre final
    os.path.dirname()       → obtener solo la carpeta padre
    os.path.abspath()       → convertir ruta relativa a absoluta
    os.path.exists()        → verificar si algo existe (archivo o carpeta)
    os.path.isfile()        → verificar que es específicamente un archivo
    os.path.isdir()         → verificar que es específicamente una carpeta
    os.path.getsize()       → tamaño de un archivo en bytes

LISTAR
    os.listdir(ruta)        → contenido de una carpeta (un solo nivel)
    os.walk(ruta)           → contenido recursivo de un árbol de carpetas

CARPETAS
    os.mkdir(ruta)          → crear UNA carpeta (el padre ya debe existir)
    os.makedirs(ruta, exist_ok=True)  → crear carpeta + todos los padres
    os.rmdir(ruta)          → eliminar carpeta vacía

ARCHIVOS
    os.remove(ruta)         → eliminar un archivo
    os.rename(origen, dest) → renombrar o mover (mismo filesystem)

VARIABLES DE ENTORNO
    os.environ.get(k, default)  → leer variable de entorno con seguridad
    os.environ[k] = v           → definir variable de entorno

DIRECTORIO DE TRABAJO
    os.getcwd()             → directorio actual
    os.chdir(ruta)          → cambiar directorio actual
"""