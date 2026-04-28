# =============================================================
# REFERENCIA: Leer archivos — ¿solo mostrar o reconstruir?
# Andrés Palacios — Python Básico
# Basado en documentación oficial: docs.python.org
# =============================================================

# -------------------------------------------------------------
# EL CONCEPTO CLAVE
# -------------------------------------------------------------
# Cuando lees un archivo .txt, Python te da texto plano — strings.
# Lo que hagas CON ese texto determina qué tan complejo es el código.
#
# Tienes dos casos posibles:
#
# CASO 1 → Solo mostrar el contenido en pantalla.
# CASO 2 → Reconstruir objetos para seguir operando con ellos.

# -------------------------------------------------------------
# ¿QUÉ SIGNIFICA "RECONSTRUIR"?
# -------------------------------------------------------------
# Cuando guardas un objeto en un .txt, Python lo convierte a texto:
#
#   Libro("El principito", "Saint-Exupéry", 1943)
#   → se guarda como: "El principito,Saint-Exupéry,1943"
#
# El archivo no guarda el objeto — guarda sus DATOS como texto.
# Cuando vuelves a leer ese archivo, Python te da el string:
#   "El principito,Saint-Exupéry,1943"
#
# Reconstruir = tomar ese string, separar sus partes,
# y volver a crear el objeto Libro con esos datos.
# Es como desempacar una caja: guardaste piezas, ahora las armas.

# -------------------------------------------------------------
# CASO 1: SOLO MOSTRAR (lectura_registro — mini banco)
# -------------------------------------------------------------
# ¿Cuándo usarlo?
# Cuando el único objetivo es que el usuario VEA la información.
# No necesitas operar con los datos después de leerlos.
#
# def lectura_registro():
#     try:
#         with open("historial.txt", "r") as r:
#             for historial in r:
#                 print(historial)
#     except FileNotFoundError:
#         print("no hay registro del historial")
#
# ¿Por qué es tan simple?
# → No necesitas separar los datos (no usas split)
# → No creas objetos (no reconstruyes nada)
# → No retornas nada (no hay return)
# → Solo lees línea por línea y muestras
#
# El archivo guarda: "Andrés,deposito,500"
# Tú solo imprimes:  "Andrés,deposito,500"
# No necesitas saber qué es cada parte.

# -------------------------------------------------------------
# CASO 2: RECONSTRUIR OBJETOS (leer_libro — miniproyecto 1)
# -------------------------------------------------------------
# ¿Cuándo usarlo?
# Cuando necesitas usar los datos del archivo como objetos
# para seguir operando con ellos en el programa.
#
# def leer_libro():
#     try:
#         with open("biblioteca.txt", "r") as book:
#             lista = []
#             for contenido in book:
#                 partes = contenido.strip().split(",")
#                 objeto = Libro(partes[0], partes[1], partes[2])
#                 lista.append(objeto)
#         return lista
#     except FileNotFoundError:
#         print("el libro no existe aún")
#         return []
#
# ¿Por qué es más complejo?
# → strip()     elimina el \n al final de cada línea
# → split(",")  separa "titulo,autor,año" en ["titulo","autor","año"]
# → Libro(...)  reconstruye el objeto con esas partes
# → lista       guarda todos los objetos para usarlos después
# → return      devuelve la lista para que main.py pueda operarla
#
# El archivo guarda: "El principito,Saint-Exupéry,1943"
# Tú reconstruyes:   Libro("El principito", "Saint-Exupéry", 1943)
# Y ahora puedes:    libro.titulo, libro.autor, libro.año

# -------------------------------------------------------------
# TABLA COMPARATIVA
# -------------------------------------------------------------
#
# Característica         Solo mostrar         Reconstruir objetos
# ─────────────────────────────────────────────────────────────────
# strip()                No necesitas         Sí — quita el \n
# split(",")             No necesitas         Sí — separa los datos
# Crear objeto           No                   Sí — arma el objeto
# Lista                  No                   Sí — guarda los objetos
# return                 No                   Sí — devuelve la lista
# Complejidad            Simple               Más elaborado
# Objetivo               Mostrar en pantalla  Operar con los datos

# -------------------------------------------------------------
# ¿CÓMO DECIDIR CUÁL USAR?
# -------------------------------------------------------------
# Hazte esta pregunta:
#
# "Después de leer el archivo, ¿necesito hacer algo con los datos?"
#
# NO → solo mostrar → CASO 1 (simple)
# SÍ → reconstruir  → CASO 2 (elaborado)
#
# Ejemplos:
# ¿Mostrar el historial de un banco?         → CASO 1
# ¿Cargar libros para agregar uno nuevo?     → CASO 2
# ¿Mostrar un log de errores?                → CASO 1
# ¿Cargar estudiantes para calcular notas?   → CASO 2

# -------------------------------------------------------------
# LO QUE HACE strip() y split() — documentación oficial
# -------------------------------------------------------------
# str.strip()
#   Elimina espacios y caracteres como \n al inicio y al final.
#   "El principito,Saint-Exupéry,1943\n".strip()
#   → "El principito,Saint-Exupéry,1943"
#   docs.python.org/3/library/stdtypes.html#str.strip
#
# str.split(separador)
#   Divide un string en una lista usando el separador indicado.
#   "El principito,Saint-Exupéry,1943".split(",")
#   → ["El principito", "Saint-Exupéry", "1943"]
#   docs.python.org/3/library/stdtypes.html#str.split
#
# Juntos hacen el "desempaque": texto plano → partes utilizables.

# -------------------------------------------------------------
# RESUMEN FINAL
# -------------------------------------------------------------
# El archivo siempre guarda texto plano.
# La diferencia no está en CÓMO lees — está en QUÉ HACES después.
#
# Solo mostrar   → lees y printeas. Fin.
# Reconstruir    → lees, separas, armas el objeto, lo guardas,
#                  lo retornas para usarlo en el programa.