"""
MÓDULO shutil — Referencia completa con contexto backend
=========================================================
"shutil" viene de "shell utilities". Complementa a os y pathlib cubriendo
las operaciones que ellos no hacen: copiar archivos con su contenido,
mover entre discos distintos, y eliminar árboles de carpetas completos.

PROBLEMA QUE RESUELVE
─────────────────────
os.rename() y Path.rename() mueven archivos, pero solo dentro del mismo
sistema de archivos. Si origen y destino están en discos distintos, fallan.
shutil.move() detecta ese caso y hace la copia + eliminación automáticamente.

os y pathlib tampoco pueden copiar el contenido de un archivo, ni eliminar
una carpeta que tenga cosas adentro. shutil cubre exactamente eso.

CUÁNDO USAR CADA MÓDULO
────────────────────────
    pathlib / os   → trabajar con rutas, listar, crear carpetas, variables de entorno
    shutil         → copiar archivos, mover entre discos, eliminar carpetas con contenido
    Los tres se usan juntos en el mismo proyecto.

import shutil
from pathlib import Path
"""

import shutil
from pathlib import Path


# ══════════════════════════════════════════════════════════════════════════════
# 1. COPIAR ARCHIVOS
# ══════════════════════════════════════════════════════════════════════════════
# shutil tiene varias funciones de copia. La diferencia está en qué metadatos
# (permisos, fechas) se copian junto con el contenido.

# ── shutil.copy(src, dst) ─────────────────────────────────────────────────────
# Copia el CONTENIDO del archivo + los permisos.
# dst puede ser una ruta de archivo o una carpeta destino.
# Si dst es carpeta, el archivo se copia con el mismo nombre dentro de ella.

# shutil.copy("reporte.pdf", "backups/reporte.pdf")    # copia con nombre explícito
# shutil.copy("reporte.pdf", "backups/")               # copia a carpeta, mismo nombre

# Acepta strings y objetos Path:
# shutil.copy(Path("reporte.pdf"), Path("backups"))

# ── shutil.copy2(src, dst) ────────────────────────────────────────────────────
# Como copy() pero también preserva las fechas (creación, modificación).
# Es la opción más completa para hacer backups reales.
# Recomendado cuando quieres que la copia sea idéntica al original.

# shutil.copy2("datos.csv", "backups/datos.csv")

# ── shutil.copyfile(src, dst) ─────────────────────────────────────────────────
# Copia SOLO el contenido, sin permisos ni metadatos.
# dst debe ser una ruta de archivo completa, no una carpeta.
# Más rápido que copy/copy2, pero no preserva nada extra.

# shutil.copyfile("config.json", "config_backup.json")

# ── shutil.copyfileobj(fsrc, fdst) ────────────────────────────────────────────
# Copia entre dos objetos de archivo ya abiertos.
# Útil cuando los archivos ya están abiertos con open(), como en uploads web.

# with open("origen.bin", "rb") as origen:
#     with open("destino.bin", "wb") as destino:
#         shutil.copyfileobj(origen, destino)

# Resumen rápido de las funciones de copia:
# copyfile   → solo contenido, sin metadatos
# copy       → contenido + permisos
# copy2      → contenido + permisos + fechas  (la más completa, usa esta para backups)
# copyfileobj→ entre file objects ya abiertos

# ── Caso real: sistema de backups ────────────────────────────────────────────
def hacer_backup(archivo: Path, carpeta_backup: Path) -> Path:
    """Copia un archivo a la carpeta de backup y retorna la ruta del backup."""
    carpeta_backup.mkdir(parents=True, exist_ok=True)
    destino = carpeta_backup / archivo.name
    shutil.copy2(archivo, destino)   # copy2 preserva fechas → ideal para backups
    print(f"Backup creado: {destino}")
    return destino


# ══════════════════════════════════════════════════════════════════════════════
# 2. COPIAR ÁRBOLES DE CARPETAS COMPLETOS
# ══════════════════════════════════════════════════════════════════════════════

# ── shutil.copytree(src, dst) ────────────────────────────────────────────────
# Copia una carpeta ENTERA con todo su contenido (archivos + subcarpetas)
# de forma recursiva. dst no debe existir previamente (por defecto).

# shutil.copytree("templates/", "mi_proyecto/")
# Crea "mi_proyecto/" con todo lo que hay en "templates/"

# dirs_exist_ok=True (Python 3.8+): permite que dst ya exista y mergea el contenido
# shutil.copytree("actualizaciones/", "produccion/", dirs_exist_ok=True)

# ignore: excluir archivos que coincidan con ciertos patrones
# shutil.copytree(
#     "proyecto/",
#     "proyecto_backup/",
#     ignore=shutil.ignore_patterns("*.pyc", "__pycache__", ".git")
# )

# Caso real: crear un proyecto nuevo desde una plantilla
def crear_proyecto_desde_plantilla(nombre: str, plantilla: Path, destino_base: Path):
    destino = destino_base / nombre
    shutil.copytree(
        plantilla,
        destino,
        ignore=shutil.ignore_patterns("*.pyc", "__pycache__")
    )
    print(f"Proyecto '{nombre}' creado en {destino}")


# ══════════════════════════════════════════════════════════════════════════════
# 3. MOVER ARCHIVOS Y CARPETAS
# ══════════════════════════════════════════════════════════════════════════════

# ── shutil.move(src, dst) ─────────────────────────────────────────────────────
# Mueve un archivo o carpeta de src a dst.
# Si src y dst están en el mismo filesystem: usa os.rename() internamente (rápido).
# Si están en filesystems distintos: copia el contenido y luego elimina el origen.
# Es la función más robusta para mover, siempre funciona.

# shutil.move("datos.csv", "procesados/datos.csv")
# shutil.move("carpeta_entera/", "archivo/carpeta_entera/")

# dst puede ser:
#   - ruta completa del archivo destino: "backups/datos_2024.csv"
#   - carpeta destino:                   "backups/"  (conserva el nombre original)

# Diferencia clave con os.rename / Path.rename:
# os.rename("a.txt", "b.txt")     → falla si src y dst están en discos distintos
# shutil.move("a.txt", "b.txt")   → siempre funciona, maneja el caso cross-device

# Caso real: mover archivo procesado a carpeta de completados
def marcar_como_procesado(archivo: Path, carpeta_completados: Path):
    carpeta_completados.mkdir(parents=True, exist_ok=True)
    shutil.move(str(archivo), str(carpeta_completados / archivo.name))
    print(f"Movido a completados: {archivo.name}")

# Nota: shutil.move acepta strings y Paths, pero es buena práctica
# convertir a str() con rutas complejas para mayor compatibilidad.


# ══════════════════════════════════════════════════════════════════════════════
# 4. ELIMINAR ÁRBOLES DE CARPETAS
# ══════════════════════════════════════════════════════════════════════════════

# ── shutil.rmtree(ruta) ──────────────────────────────────────────────────────
# Elimina una carpeta y TODO su contenido (archivos + subcarpetas).
# Es irreversible. No hay papelera de reciclaje.
# USAR CON PRECAUCIÓN.

# shutil.rmtree("carpeta_con_contenido/")

# ignore_errors=True → continúa aunque haya errores de permisos
# shutil.rmtree("carpeta/", ignore_errors=True)

# Diferencia:
# Path.rmdir()      → solo carpetas VACÍAS
# shutil.rmtree()   → carpetas con todo su contenido adentro

# Caso real: limpiar carpeta temporal al finalizar un proceso
def limpiar_temporales(carpeta_tmp: Path):
    if carpeta_tmp.exists() and carpeta_tmp.is_dir():
        shutil.rmtree(carpeta_tmp)
        print(f"Carpeta temporal eliminada: {carpeta_tmp}")

# Caso real: eliminar y recrear una carpeta (reset limpio)
def resetear_carpeta(carpeta: Path):
    if carpeta.exists():
        shutil.rmtree(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)


# ══════════════════════════════════════════════════════════════════════════════
# 5. INFORMACIÓN DEL SISTEMA DE ARCHIVOS
# ══════════════════════════════════════════════════════════════════════════════

# ── shutil.disk_usage(ruta) ──────────────────────────────────────────────────
# Retorna el uso del disco en la partición donde está la ruta.
# Retorna una namedtuple con: total, used, free (en bytes).

uso = shutil.disk_usage("/")
print(f"Total : {uso.total / (1024**3):.1f} GB")
print(f"Usado : {uso.used  / (1024**3):.1f} GB")
print(f"Libre : {uso.free  / (1024**3):.1f} GB")

# Caso real: verificar espacio antes de un proceso pesado
def hay_espacio_suficiente(carpeta: Path, gb_necesarios: float) -> bool:
    uso = shutil.disk_usage(carpeta)
    return uso.free >= gb_necesarios * (1024 ** 3)

# ── shutil.which(nombre) ──────────────────────────────────────────────────────
# Busca un ejecutable en el PATH del sistema. Equivalente al comando `which`.
# Retorna la ruta completa o None si no se encuentra.

ruta_python = shutil.which("python3")
print(ruta_python)   # /usr/bin/python3  (ejemplo)

ruta_ffmpeg = shutil.which("ffmpeg")
if ruta_ffmpeg is None:
    print("ffmpeg no está instalado")

# Caso real: verificar dependencias del sistema antes de ejecutar un proceso
def verificar_dependencias(herramientas: list) -> bool:
    faltantes = [h for h in herramientas if shutil.which(h) is None]
    if faltantes:
        print(f"Herramientas faltantes: {', '.join(faltantes)}")
        return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
# 6. COMPRIMIR Y DESCOMPRIMIR
# ══════════════════════════════════════════════════════════════════════════════

# ── shutil.make_archive(nombre_base, formato, directorio_raiz) ───────────────
# Comprime una carpeta entera. Formatos: "zip", "tar", "gztar", "bztar", "xztar"
# nombre_base: ruta y nombre del archivo resultante SIN extensión.
# Retorna la ruta del archivo creado.

# shutil.make_archive("backup_2024", "zip", "proyectos/")
# → crea backup_2024.zip con todo el contenido de proyectos/

# shutil.make_archive("backup_2024", "gztar", "proyectos/")
# → crea backup_2024.tar.gz

# Caso real: backup comprimido con fecha
# from datetime import date
# nombre = f"backup_{date.today().isoformat()}"
# shutil.make_archive(nombre, "zip", "datos/")

# ── shutil.unpack_archive(archivo, directorio_destino) ───────────────────────
# Descomprime un archivo. Detecta el formato automáticamente por la extensión.
# Soporta .zip, .tar, .tar.gz, .tar.bz2, .tar.xz

# shutil.unpack_archive("backup_2024.zip", "restaurado/")
# shutil.unpack_archive("datos.tar.gz", "datos_extraidos/")

# Caso real: descomprimir un archivo subido por el usuario
def descomprimir_upload(archivo: Path, destino: Path):
    formatos_soportados = (".zip", ".tar", ".gz", ".bz2", ".xz")
    if archivo.suffix not in formatos_soportados:
        raise ValueError(f"Formato no soportado: {archivo.suffix}")
    destino.mkdir(parents=True, exist_ok=True)
    shutil.unpack_archive(str(archivo), str(destino))
    print(f"Extraído en: {destino}")


# ══════════════════════════════════════════════════════════════════════════════
# 7. PATRÓN COMPLETO — LOS TRES MÓDULOS JUNTOS
# ══════════════════════════════════════════════════════════════════════════════
# En la práctica, pathlib, os y shutil se usan juntos.
# Cada uno cubre lo que los otros no hacen.

import os  # para variables de entorno

def organizar_uploads(carpeta_uploads: Path, carpeta_procesados: Path):
    """
    Lee todos los archivos de uploads/, los procesa según su tipo
    y los mueve a la carpeta correspondiente en procesados/.
    """

    # pathlib: verificar que la carpeta existe y crear la de destino
    if not carpeta_uploads.is_dir():
        print(f"ERROR: {carpeta_uploads} no existe.")
        return

    # os: leer configuración desde variables de entorno
    max_size_mb = int(os.environ.get("MAX_UPLOAD_MB", "10"))

    archivos_procesados = 0

    # pathlib: iterar sobre los archivos
    for archivo in carpeta_uploads.iterdir():
        if not archivo.is_file():
            continue

        # pathlib: validar tamaño
        if archivo.stat().st_size > max_size_mb * 1024 * 1024:
            print(f"Saltando {archivo.name}: supera {max_size_mb} MB")
            continue

        # pathlib: determinar subcarpeta por extensión
        extension = archivo.suffix.lstrip(".").lower() or "sin_extension"
        destino_carpeta = carpeta_procesados / extension

        # pathlib: crear subcarpeta si no existe
        destino_carpeta.mkdir(parents=True, exist_ok=True)

        # shutil: mover el archivo (funciona entre discos distintos)
        shutil.move(str(archivo), str(destino_carpeta / archivo.name))
        print(f"Movido: {archivo.name} → {extension}/")
        archivos_procesados += 1

    print(f"\nTotal procesados: {archivos_procesados}")


# ══════════════════════════════════════════════════════════════════════════════
# 8. RESUMEN — QUÉ USA CADA MÓDULO
# ══════════════════════════════════════════════════════════════════════════════
"""
pathlib (rutas y estructura)
    Path(a) / b              → construir rutas
    .name / .stem / .suffix  → partes del nombre
    .parent / .parents       → carpeta(s) padre
    .exists() / .is_file() / .is_dir()  → verificar qué hay
    .stat().st_size          → tamaño del archivo
    .iterdir()               → listar carpeta (retorna Paths)
    .glob() / .rglob()       → buscar por patrón (normal / recursivo)
    .mkdir(parents, exist_ok)→ crear carpeta y padres
    .rmdir()                 → eliminar carpeta VACÍA
    .unlink(missing_ok)      → eliminar archivo
    .rename()                → renombrar (mismo filesystem)
    .read_text() / .write_text()  → leer/escribir archivos pequeños

os (sistema operativo)
    os.environ.get(k, default)    → leer variables de entorno (API keys, config)
    os.getcwd() / Path.cwd()      → directorio de trabajo actual
    os.getpid()                   → PID del proceso (logs, workers)
    os.name                       → "posix" o "nt" (detección del SO)

shutil (copiar, mover entre discos, borrar árboles, comprimir)
    shutil.copy(src, dst)         → copiar archivo (contenido + permisos)
    shutil.copy2(src, dst)        → copiar archivo (+ fechas, ideal para backups)
    shutil.copytree(src, dst)     → copiar carpeta entera con todo su contenido
    shutil.move(src, dst)         → mover (funciona entre discos distintos)
    shutil.rmtree(ruta)           → eliminar carpeta con TODO su contenido
    shutil.disk_usage(ruta)       → espacio total/usado/libre del disco
    shutil.which(nombre)          → ruta de un ejecutable en el PATH
    shutil.make_archive(...)      → comprimir carpeta a .zip / .tar.gz / etc
    shutil.unpack_archive(...)    → descomprimir cualquier formato soportado
"""