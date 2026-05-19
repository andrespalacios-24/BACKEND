"""
MÓDULO pathlib — Referencia completa con contexto backend
==========================================================
Disponible desde Python 3.4. Es el estándar moderno para trabajar con rutas.

PROBLEMA QUE RESUELVE
─────────────────────
Con os.path, una ruta es solo un string y las operaciones son funciones sueltas:

    import os
    ruta = os.path.join("proyectos", "datos.csv")
    ext  = os.path.splitext(ruta)[1]
    os.makedirs(os.path.dirname(ruta), exist_ok=True)   # difícil de leer

Con pathlib, una ruta es un OBJETO que ya sabe lo que es y qué puede hacer:

    from pathlib import Path
    ruta = Path("proyectos") / "datos.csv"
    ext  = ruta.suffix
    ruta.parent.mkdir(parents=True, exist_ok=True)      # más legible

CUÁNDO USAR pathlib VS os
─────────────────────────
    pathlib   → todo lo relacionado con rutas, archivos y carpetas
    os        → variables de entorno (os.environ), info del sistema (os.getpid)
    shutil    → copiar y mover archivos (pathlib no cubre esto)

En proyectos modernos pathlib reemplaza casi todo os.path.

from pathlib import Path
"""

from pathlib import Path


# ══════════════════════════════════════════════════════════════════════════════
# 1. CREAR UN OBJETO PATH
# ══════════════════════════════════════════════════════════════════════════════
# Path() recibe un string con la ruta. A partir de ahí todo es orientado
# a objetos: el objeto Path sabe su nombre, extensión, carpeta padre, etc.

p = Path("documentos/reporte.pdf")   # ruta relativa
q = Path("/home/andres/BACKEND")     # ruta absoluta
r = Path(".")                        # directorio actual

# ── El operador / ─────────────────────────────────────────────────────────────
# pathlib sobrecarga el operador / para unir partes de una ruta.
# Es el reemplazo directo de os.path.join(). Más limpio y legible.

base    = Path("/home/andres/BACKEND")
archivo = base / "uploads" / "foto.jpg"
print(archivo)   # /home/andres/BACKEND/uploads/foto.jpg

# También puedes mezclar Path con strings
config = Path("proyectos") / "backend" / "settings.json"

# Equivalencia:
#   os.path.join("proyectos", "backend", "settings.json")
#   Path("proyectos") / "backend" / "settings.json"    ← preferido hoy


# ══════════════════════════════════════════════════════════════════════════════
# 2. ATRIBUTOS — INFORMACIÓN SOBRE LA RUTA
# ══════════════════════════════════════════════════════════════════════════════
# Los atributos son propiedades del objeto, no funciones. No llevan paréntesis.

ruta = Path("/home/andres/proyectos/reporte_final.pdf")

print(ruta.name)       # reporte_final.pdf       — nombre completo con extensión
print(ruta.stem)       # reporte_final            — nombre sin extensión
print(ruta.suffix)     # .pdf                     — extensión con punto
print(ruta.suffixes)   # ['.pdf']                 — lista (útil para .tar.gz)
print(ruta.parent)     # /home/andres/proyectos   — carpeta padre
print(ruta.parents[0]) # /home/andres/proyectos   — mismo que .parent
print(ruta.parents[1]) # /home/andres             — abuelo
print(ruta.parts)      # ('/', 'home', 'andres', 'proyectos', 'reporte_final.pdf')

# Ejemplo con extensión doble (común en backups y comprimidos)
archivo_tar = Path("backup.tar.gz")
print(archivo_tar.suffix)    # .gz
print(archivo_tar.suffixes)  # ['.tar', '.gz']
print(archivo_tar.stem)      # backup.tar

# Equivalencias con os.path:
#   os.path.basename(r)          → Path(r).name
#   os.path.splitext(r)[0]       → Path(r).stem
#   os.path.splitext(r)[1]       → Path(r).suffix
#   os.path.dirname(r)           → Path(r).parent


# ══════════════════════════════════════════════════════════════════════════════
# 3. MÉTODOS DE CONSULTA — ¿QUÉ HAY EN ESA RUTA?
# ══════════════════════════════════════════════════════════════════════════════
# Estos métodos sí llevan paréntesis porque consultan el disco.

ruta_archivo  = Path("datos.csv")
ruta_carpeta  = Path("uploads")

ruta_archivo.exists()       # True si existe (archivo O carpeta)
ruta_archivo.is_file()      # True solo si es archivo
ruta_carpeta.is_dir()       # True solo si es carpeta
ruta_archivo.is_absolute()  # True si la ruta es absoluta

# Equivalencias con os.path:
#   os.path.exists(r)    → Path(r).exists()
#   os.path.isfile(r)    → Path(r).is_file()
#   os.path.isdir(r)     → Path(r).is_dir()

# ── stat() — metadatos del archivo ───────────────────────────────────────────
# Retorna información como tamaño, fecha de modificación, permisos.

# info = Path("datos.csv").stat()
# print(info.st_size)   # tamaño en bytes
# print(info.st_mtime)  # timestamp de última modificación

# Caso real: validar tamaño de un upload
def upload_valido(ruta: Path, max_mb: int = 5) -> bool:
    return ruta.is_file() and ruta.stat().st_size <= max_mb * 1024 * 1024


# ══════════════════════════════════════════════════════════════════════════════
# 4. RUTAS ABSOLUTAS Y RELATIVAS
# ══════════════════════════════════════════════════════════════════════════════

# ── resolve() ────────────────────────────────────────────────────────────────
# Convierte cualquier ruta a absoluta, resolviendo ".." y enlaces simbólicos.
# Equivalente a os.path.abspath() pero más potente.

relativa = Path("uploads/foto.jpg")
absoluta = relativa.resolve()
print(absoluta)   # /home/andres/BACKEND/uploads/foto.jpg

# ── __file__ con pathlib ──────────────────────────────────────────────────────
# Patrón muy común en backend: localizar archivos relativos al script actual.

# DIRECTORIO_SCRIPT = Path(__file__).parent
# CONFIG_FILE       = DIRECTORIO_SCRIPT / "config" / "settings.json"
# UPLOADS_DIR       = DIRECTORIO_SCRIPT / "uploads"

# Esto es más limpio que:
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# CONFIG   = os.path.join(BASE_DIR, "config", "settings.json")


# ══════════════════════════════════════════════════════════════════════════════
# 5. CREAR Y ELIMINAR CARPETAS
# ══════════════════════════════════════════════════════════════════════════════

# ── mkdir() ──────────────────────────────────────────────────────────────────
# Parámetros clave:
#   parents=True   → crea todos los padres intermedios (como os.makedirs)
#   exist_ok=True  → no lanza error si ya existe

Path("uploads/imagenes/2024").mkdir(parents=True, exist_ok=True)
# Si uploads/ o uploads/imagenes/ no existen, los crea. Sin error si ya existen.

# Crear una sola carpeta (el padre debe existir)
# Path("logs").mkdir()

# ── rmdir() ──────────────────────────────────────────────────────────────────
# Elimina una carpeta vacía. Para carpetas con contenido usa shutil.rmtree().

# Path("carpeta_vacia").rmdir()

# Caso real: preparar estructura de carpetas al iniciar la app
def inicializar_estructura(base: Path):
    for carpeta in ("uploads", "logs", "exports", "tmp"):
        (base / carpeta).mkdir(parents=True, exist_ok=True)


# ══════════════════════════════════════════════════════════════════════════════
# 6. LISTAR CONTENIDO DE UN DIRECTORIO
# ══════════════════════════════════════════════════════════════════════════════

# ── iterdir() ────────────────────────────────────────────────────────────────
# Itera sobre el contenido DIRECTO de una carpeta (no recursivo).
# Retorna objetos Path, no strings. Eso es la ventaja clave vs os.listdir().

carpeta = Path("/tmp")

for item in carpeta.iterdir():
    print(item)           # /tmp/archivo.txt, /tmp/subcarpeta, ...
    print(item.name)      # solo el nombre
    print(item.is_file()) # es archivo?

# Filtrar solo archivos
solo_archivos = [item for item in carpeta.iterdir() if item.is_file()]

# Equivalencia:
# os.listdir() retorna strings → tienes que reconstruir la ruta con os.path.join
# iterdir()    retorna Paths   → ya tienes la ruta completa lista para usar

# ── glob() — buscar por patrón ───────────────────────────────────────────────
# Busca archivos que coincidan con un patrón en la carpeta (no recursivo).
# Retorna un generador de objetos Path.

carpeta = Path(".")

# Todos los .csv en la carpeta actual
csvs = list(carpeta.glob("*.csv"))

# Todos los .py en la carpeta actual
scripts = list(carpeta.glob("*.py"))

# Todos los archivos (cualquier extensión)
todos = list(carpeta.glob("*.*"))

# Caso real: procesar todos los logs de hoy
# logs_hoy = list(Path("logs").glob("2024-01-15_*.log"))

# ── rglob() — glob recursivo ─────────────────────────────────────────────────
# Como glob() pero recorre todas las subcarpetas. Equivalente a os.walk() + filtro.

todos_los_py = list(Path(".").rglob("*.py"))     # busca en todo el árbol
todos_los_json = list(Path(".").rglob("*.json"))

# Caso real: encontrar todos los logs en un árbol de directorios
# todos_logs = list(Path("/var/log/mi_app").rglob("*.log"))


# ══════════════════════════════════════════════════════════════════════════════
# 7. LEER Y ESCRIBIR ARCHIVOS
# ══════════════════════════════════════════════════════════════════════════════
# pathlib incluye métodos para leer y escribir archivos directamente,
# sin necesidad de open(). Útil para archivos pequeños.

# ── read_text() / write_text() ───────────────────────────────────────────────
# Lee o escribe el contenido completo como string.

# archivo = Path("config.txt")
# archivo.write_text("clave=valor\n", encoding="utf-8")
# contenido = archivo.read_text(encoding="utf-8")

# ── read_bytes() / write_bytes() ─────────────────────────────────────────────
# Lee o escribe el contenido como bytes (imágenes, PDFs, binarios).

# imagen = Path("foto.jpg")
# datos = imagen.read_bytes()
# Path("copia.jpg").write_bytes(datos)

# Para archivos grandes o procesamiento línea a línea, sigue usando open():
# with open(archivo, "r", encoding="utf-8") as f:
#     for linea in f:
#         ...

# También puedes pasar un Path directamente a open():
# with open(Path("datos.csv"), "r") as f:   # funciona perfectamente
#     ...


# ══════════════════════════════════════════════════════════════════════════════
# 8. RENOMBRAR Y ELIMINAR ARCHIVOS
# ══════════════════════════════════════════════════════════════════════════════

# ── rename() ─────────────────────────────────────────────────────────────────
# Renombra o mueve un archivo dentro del mismo filesystem.
# Retorna un nuevo objeto Path con la ruta destino.

# Path("reporte_v1.pdf").rename("reporte_final.pdf")
# Path("datos/archivo.csv").rename("backups/archivo.csv")

# ── unlink() ─────────────────────────────────────────────────────────────────
# Elimina un archivo. missing_ok=True evita error si no existe (Python 3.8+).

# Path("temporal.txt").unlink()
# Path("temporal.txt").unlink(missing_ok=True)   # seguro si no existe

# Caso real: limpiar archivos temporales
def limpiar_temporales(carpeta: Path):
    for archivo in carpeta.glob("*.tmp"):
        archivo.unlink(missing_ok=True)


# ── with_name() y with_suffix() ──────────────────────────────────────────────
# Crear una ruta nueva cambiando solo el nombre o la extensión.

original = Path("uploads/reporte.csv")
print(original.with_name("informe.csv"))     # uploads/informe.csv
print(original.with_suffix(".pdf"))          # uploads/reporte.pdf
print(original.with_suffix(""))             # uploads/reporte  (sin extensión)

# Caso real: generar el nombre de un archivo procesado
def ruta_procesada(ruta_original: Path) -> Path:
    return ruta_original.with_name(f"{ruta_original.stem}_procesado{ruta_original.suffix}")

# ruta_procesada(Path("datos/ventas.csv"))  → Path("datos/ventas_procesado.csv")


# ══════════════════════════════════════════════════════════════════════════════
# 9. CONVERTIR ENTRE Path Y STRING
# ══════════════════════════════════════════════════════════════════════════════
# La mayoría de funciones de Python ya aceptan objetos Path directamente.
# Si alguna librería antigua necesita un string, usa str().

ruta = Path("uploads/foto.jpg")

str(ruta)          # "uploads/foto.jpg"   — conversión explícita a string
ruta.as_posix()    # "uploads/foto.jpg"   — siempre con "/" (útil en Windows)

# open(), os.remove(), shutil.move() todos aceptan Path directamente:
# open(ruta, "r")         ← funciona
# os.remove(ruta)         ← funciona
# shutil.move(ruta, dest) ← funciona


# ══════════════════════════════════════════════════════════════════════════════
# 10. RESUMEN — EQUIVALENCIAS os.path → pathlib
# ══════════════════════════════════════════════════════════════════════════════
"""
CONSTRUIR RUTAS
    os.path.join(a, b, c)        →  Path(a) / b / c

ATRIBUTOS
    os.path.basename(r)          →  Path(r).name
    os.path.dirname(r)           →  Path(r).parent
    os.path.splitext(r)[0]       →  Path(r).stem
    os.path.splitext(r)[1]       →  Path(r).suffix
    os.path.abspath(r)           →  Path(r).resolve()

CONSULTAS
    os.path.exists(r)            →  Path(r).exists()
    os.path.isfile(r)            →  Path(r).is_file()
    os.path.isdir(r)             →  Path(r).is_dir()
    os.path.getsize(r)           →  Path(r).stat().st_size

LISTAR
    os.listdir(r)                →  Path(r).iterdir()   (retorna Paths, no strings)
    os.walk(r)                   →  Path(r).rglob("*")  (más simple para filtrar)

CARPETAS
    os.mkdir(r)                  →  Path(r).mkdir()
    os.makedirs(r, exist_ok=True)→  Path(r).mkdir(parents=True, exist_ok=True)
    os.rmdir(r)                  →  Path(r).rmdir()

ARCHIVOS
    os.remove(r)                 →  Path(r).unlink()
    os.rename(src, dst)          →  Path(src).rename(dst)

LO QUE os SIGUE MANEJANDO (pathlib NO cubre esto)
    os.environ.get()             →  variables de entorno
    os.getcwd()                  →  directorio actual (o usa Path.cwd())
    os.getpid()                  →  PID del proceso
    shutil.copy/move/rmtree      →  copiar, mover, borrar árboles completos
"""