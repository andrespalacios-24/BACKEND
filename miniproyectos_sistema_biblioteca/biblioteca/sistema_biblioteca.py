# =============================================================
# MINIPROYECTO 1: Sistema de biblioteca
# Temas integrados: OOP, módulos, excepciones, archivos de texto
# =============================================================

# ESTRUCTURA DE ARCHIVOS:
# miniproyectos/
# ├── biblioteca/
# │   ├── libro.py         ← módulo con la clase Libro
# │   ├── almacen.py       ← módulo para guardar/leer libros en .txt
# │   └── main.py          ← programa principal

# -------------------------------------------------------------
# ARCHIVO 1: libro.py
# -------------------------------------------------------------
# Crear clase Libro con:
#   - atributos: titulo, autor, anio
#   - metodo __str__ que retorne info formateada del libro

# -------------------------------------------------------------
# ARCHIVO 2: almacen.py
# -------------------------------------------------------------
# Importar modulo libro
# Funcion guardar_libro(libro):
#   - recibe un objeto Libro
#   - lo guarda en "biblioteca.txt" en modo append
#   - cada libro en una linea: "titulo,autor,anio"
#
# Funcion leer_libros():
#   - lee "biblioteca.txt"
#   - retorna lista de objetos Libro
#   - excepcion si el archivo no existe (FileNotFoundError)

# -------------------------------------------------------------
# ARCHIVO 3: main.py
# -------------------------------------------------------------
# Importar modulos libro y almacen
# Crear al menos 3 libros
# Guardarlos con guardar_libro()
# Leerlos con leer_libros() y mostrarlos con un bucle
# Manejar la excepcion si biblioteca.txt no existe aun