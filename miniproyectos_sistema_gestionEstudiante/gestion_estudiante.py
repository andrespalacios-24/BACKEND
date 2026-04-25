# =============================================================
# MINIPROYECTO 2: Gestión de estudiantes
# Temas integrados: OOP, módulos, excepciones, funciones, bucles
# =============================================================

# ESTRUCTURA DE ARCHIVOS:
# miniproyectos/
# ├── estudiantes/
# │   ├── estudiante.py    ← módulo con la clase Estudiante
# │   ├── estadisticas.py  ← módulo con funciones media y mediana
# │   └── main.py          ← programa principal

# -------------------------------------------------------------
# ARCHIVO 1: estudiante.py
# -------------------------------------------------------------
# Clase Estudiante con:
#   - atributos: nombre, notas (lista)
#   - metodo agregar_nota(nota):
#       excepcion si nota < 0 o nota > 10
#   - metodo promedio():
#       retorna promedio de notas
#       excepcion si no hay notas aun

# -------------------------------------------------------------
# ARCHIVO 2: estadisticas.py
# -------------------------------------------------------------
# Funcion media(lista): retorna el promedio
# Funcion mediana(lista): retorna el valor central
# (Reutilizar la logica del ejercicio 8 de modulos)

# -------------------------------------------------------------
# ARCHIVO 3: main.py
# -------------------------------------------------------------
# Crear al menos 3 estudiantes con diferentes notas
# Mostrar promedio de cada uno
# Usar estadisticas.py para calcular media y mediana
#   de todos los promedios juntos
# Manejar excepciones de notas invalidas