"""
REFERENCIA — Crear una carpeta nueva y subirla a GitHub desde cero
===================================================================
Paso a paso completo desde crear la carpeta hasta el primer push.
Guarda este archivo en tu carpeta de notas personales.
"""


# ══════════════════════════════════════════════════════════════════════════════
# PASO 1 — Crear la carpeta del proyecto
# ══════════════════════════════════════════════════════════════════════════════

# Desde cualquier lugar de la terminal, usa ~ para referirte a tu carpeta home.
# No necesitas moverte a ningún lado primero.

#   mkdir ~/nombre_carpeta
#   mkdir ~/nombre_carpeta/subcarpeta

# Ejemplo real:
#   mkdir ~/proyecto_portafolio
#   mkdir ~/proyecto_portafolio/etapa1

# Con -p creas toda la ruta de una sola vez aunque la carpeta padre no exista:
#   mkdir -p ~/proyecto_portafolio/etapa1

# ── Comandos de navegación útiles ─────────────────────────────────────────────
#   cd ~/nombre_carpeta     entra a la carpeta (~ siempre es home)
#   cd ..                   sube un nivel
#   cd -                    vuelve a la carpeta anterior
#   pwd                     muestra en qué carpeta estás parado ahora mismo
#   ls                      lista el contenido de la carpeta actual


# ══════════════════════════════════════════════════════════════════════════════
# PASO 2 — Inicializar git en la carpeta
# ══════════════════════════════════════════════════════════════════════════════

# Entra a la carpeta raíz del proyecto (no a una subcarpeta):
#   cd ~/proyecto_portafolio

# Inicializa el repositorio local:
#   git init

# Cambia el nombre de la rama a 'main' (por defecto crea 'master'):
#   git branch -m main

# ── ¿Dónde va el git init? ────────────────────────────────────────────────────
# SIEMPRE en la carpeta raíz del proyecto, no dentro de subcarpetas.
# Un solo git init cubre todas las subcarpetas que estén adentro.
# Ejemplo: git init en ~/proyecto_portafolio cubre etapa1/, etapa2/, etc.


# ══════════════════════════════════════════════════════════════════════════════
# PASO 3 — Crear el repositorio en GitHub
# ══════════════════════════════════════════════════════════════════════════════

# 1. Ve a github.com y haz clic en "New repository"
# 2. Ponle nombre (igual que tu carpeta local, por consistencia)
# 3. Agrega una descripción corta (los reclutadores la ven)
# 4. Déjalo en Public
# 5. NO actives README, .gitignore ni license — los agregas tú después
# 6. Clic en "Create repository"

# GitHub te mostrará una página con instrucciones. Lo que necesitas es la URL SSH:
#   git@github.com:tu_usuario/nombre_repo.git


# ══════════════════════════════════════════════════════════════════════════════
# PASO 4 — Conectar la carpeta local con GitHub
# ══════════════════════════════════════════════════════════════════════════════

# Desde la terminal, dentro de tu carpeta del proyecto:
#   git remote add origin git@github.com:tu_usuario/nombre_repo.git

# Verifica que quedó bien conectado:
#   git remote -v
# Debe mostrar dos líneas: una para fetch y otra para push, con tu URL.


# ══════════════════════════════════════════════════════════════════════════════
# PASO 5 — Primer commit y push
# ══════════════════════════════════════════════════════════════════════════════

# Agrega todos los archivos al staging area:
#   git add .

# Crea el primer commit:
#   git commit -m "primer commit"

# Sube al repositorio de GitHub por primera vez.
# El -u conecta tu rama local 'main' con la de GitHub.
# Solo se necesita una vez — los push siguientes son solo 'git push':
#   git push -u origin main


# ══════════════════════════════════════════════════════════════════════════════
# FLUJO DIARIO (después del primer push)
# ══════════════════════════════════════════════════════════════════════════════

# Antes de empezar a trabajar (especialmente si usas dos PCs):
#   git pull

# Al terminar el trabajo del día:
#   git add .
#   git commit -m "descripción de lo que hiciste"
#   git push

# ── Buenas prácticas para mensajes de commit ──────────────────────────────────
#   "agrega función obtener_extension"        <- describe qué agregaste
#   "corrige validación en organizar_carpeta" <- describe qué corregiste
#   "refactoriza cuenta_regresiva"            <- describe qué reorganizaste
#   NO usar: "cambios", "update", "fix", "wip" <- no dicen nada útil


# ══════════════════════════════════════════════════════════════════════════════
# RESUMEN DE COMANDOS — orden completo de una vez
# ══════════════════════════════════════════════════════════════════════════════

#   mkdir -p ~/nombre_proyecto/subcarpeta
#   cd ~/nombre_proyecto
#   git init
#   git branch -m main
#   git remote add origin git@github.com:tu_usuario/nombre_proyecto.git
#   git add .
#   git commit -m "primer commit"
#   git push -u origin main