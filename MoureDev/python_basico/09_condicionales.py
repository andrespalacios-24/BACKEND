# ============================================================
# CONDICIONALES EN PYTHON - Guía de referencia
# Curso MoureDev | Andrés Palacios
# ============================================================
"""
>  # mayor que
<   # menor que
>=  # mayor o igual que
<=  # menor o igual que 
"""

# ------------------------------------------------------------
# 1. IF BÁSICO
# Ejecuta el bloque solo si la condición es verdadera.
# Un valor False, 0, "" o None NO entra al bloque.
# ------------------------------------------------------------

edad = 20

if edad >= 18:
    print("Eres mayor de edad")

# La variable puede cambiar de valor antes del siguiente if.
# my_condition empieza en False (no entra), luego se reasigna a 25.
my_condition = False

if my_condition:  # No se ejecuta, my_condition es False
    print("Esto no se imprime")

my_condition = 5 * 5  # Ahora vale 25

if my_condition == 10:
    print("Esto tampoco se imprime, 25 != 10")


# ------------------------------------------------------------
# 2. IF / ELSE
# Si la condición es falsa, entra al bloque else
# ------------------------------------------------------------

nota = 4.5

if nota >= 6.0:
    print("Aprobado")
else:
    print("Reprobado")


# ------------------------------------------------------------
# 3. IF / ELIF / ELSE
# Evalúa múltiples condiciones en orden.
# Solo entra al primer bloque verdadero.
# ------------------------------------------------------------

temperatura = 35

if temperatura >= 38:
    print("Fiebre alta")
elif temperatura >= 37.5:
    print("Fiebre leve")
elif temperatura >= 36:
    print("Temperatura normal")
else:
    print("Temperatura baja")

# Importante: lo que está FUERA del bloque (indentación 0)
# siempre se ejecuta, sin importar qué rama se tomó.
print("La ejecución continúa aquí siempre")


# ------------------------------------------------------------
# 4. CONDICIONALES ANIDADOS
# Un if dentro de otro if.
# Úsalos con cuidado: demasiado anidamiento dificulta la lectura.
# ------------------------------------------------------------

usuario = "andres"
contrasena_correcta = True

if usuario == "andres":
    if contrasena_correcta:
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no existe")


# ------------------------------------------------------------
# 5. OPERADORES LÓGICOS EN CONDICIONES
# Combina condiciones con: and, or, not
# ------------------------------------------------------------

edad = 25
tiene_cuenta = True

if edad >= 18 and tiene_cuenta:
    print("Puede hacer la compra")

if edad < 18 or not tiene_cuenta:
    print("No puede completar el pedido")


# ------------------------------------------------------------
# 6. CONDICIONAL EN UNA LÍNEA (TERNARIO)
# Forma corta para asignar un valor según una condición.
# Útil cuando el resultado es simple.
# ------------------------------------------------------------

stock = 0

estado = "Disponible" if stock > 0 else "Agotado"
print(estado)  # Agotado


# ------------------------------------------------------------
# 7. VERIFICAR SI ALGO ESTÁ EN UNA LISTA (operador in)
# El operador "in" funciona directamente dentro de un if
# ------------------------------------------------------------

roles_admin = ["admin", "superadmin"]
rol_usuario = "admin"

if rol_usuario in roles_admin:
    print("Acceso al panel de administración")
else:
    print("Sin permisos")


# ------------------------------------------------------------
# 8. VERIFICAR SI UN VALOR EXISTE (None, vacío)
# En el backend es muy común revisar si un dato llegó o no.
# None, "", 0, [] son todos "falsy" (se evalúan como False)
# ------------------------------------------------------------

token = None

if token:
    print("Token válido, procesando...")
else:
    print("Token no encontrado, acceso denegado")

# También funciona con strings vacíos y listas vacías
nombre = ""
if not nombre:
    print("El campo nombre es obligatorio")


# ------------------------------------------------------------
# 9. USO REAL EN BACKEND
# Así se usan los condicionales en una API real:
# validación de una solicitud HTTP paso a paso.
# ------------------------------------------------------------

# Simulación de una solicitud a una API
metodo = "POST"
body = {"usuario": "andres", "clave": "1234"}
usuario_existe = True
clave_correcta = True

if metodo != "POST": # el (!=) significa: no es igual a. # el opuesto a == 
    print("405 - Método no permitido")
elif "usuario" not in body or "clave" not in body:
    print("400 - Datos incompletos")
elif not usuario_existe:
    print("404 - Usuario no encontrado")
elif not clave_correcta:
    print("401 - Contraseña incorrecta")
else:
    print("200 - Login exitoso. Bienvenido, andres")

# ------------------------------------------------------------
# 10. MATCH / CASE (Python 3.10+)
# Equivalente moderno al switch de otros lenguajes.
# Ideal cuando evalúas un mismo valor contra muchas opciones.
# Más limpio que una cadena larga de elif.
# ------------------------------------------------------------

color_semaforo = "rojo"

match color_semaforo:
    case "rojo":
        print("Detente")
    case "amarillo":
        print("Precaución")
    case "verde":
        print("Avanza")
    case _:           # _ es el "default": cualquier otro valor
        print("Color no reconocido")

# Comparación: el mismo código con elif sería más verboso:
# if color_semaforo == "rojo":
#     print("Detente")
# elif color_semaforo == "amarillo":
#     ...


# ------------------------------------------------------------
# 11. CORTOCIRCUITO LÓGICO (short-circuit evaluation)
# Python evalúa and/or de izquierda a derecha
# y se detiene en cuanto el resultado está determinado.
#
# Con "and": si el primer valor es falsy, no evalúa el segundo.
# Con "or":  si el primer valor es truthy, no evalúa el segundo.
# ------------------------------------------------------------

# Ejemplo con "and" — útil para evitar errores con None:
usuario = None

# Sin cortocircuito esto daría error: None no tiene .startswith()
# Con "and", si usuario es None (falsy), Python no llega al segundo lado.
if usuario and usuario.startswith("admin"):
    print("Es administrador")
else:
    print("Usuario no válido")

# Ejemplo con "or" — útil para valores por defecto:
nombre_recibido = ""  # Llegó vacío desde un formulario

nombre = nombre_recibido or "Invitado"
print(nombre)  # "Invitado" — porque nombre_recibido es falsy


# ------------------------------------------------------------
# 12. WALRUS OPERATOR := (Python 3.8+)
# Asigna una variable y evalúa la condición al mismo tiempo.
# Evita repetir la misma expresión dos veces.
# ------------------------------------------------------------

# Sin walrus — calculas el valor y luego lo usas por separado:
datos = {"usuario": "andres", "rol": "admin"}
rol = datos.get("rol")   # primero asignas
if rol:                  # luego evalúas
    print(f"Rol encontrado: {rol}")

# Con walrus — asignas y evalúas en una sola línea:
if rol := datos.get("rol"):
    print(f"Rol encontrado: {rol}")

# Lo verás seguido en validaciones de APIs:
# if token := request.headers.get("Authorization"):
#     procesar_token(token)
# else:
#     print("401 - No autorizado")

#-----------------------------------------------------------------------------------
# IF NOT - Condicional negado
#------------------------------------------------------------------------------------
# "not" invierte el valor booleano de una condición
# True  → False
# False → True

# En Python, los strings tienen valor booleano implícito:
# - String con contenido → True
# - String vacío ""     → False

cadena_de_texto = input("cadena de texto: ")

if not cadena_de_texto:        # Si NO hay contenido (vacío → False → not False → True)
    print("cadena de texto vacia")
else:                          # Si SÍ hay contenido (tiene texto → True → not True → False)
    print("Contiene texto")

# "not" funciona con cualquier valor booleano, no solo strings:
# if not True  → False
# if not False → True

# Aplicación backend real: validar que un campo no llegue vacío
# antes de guardarlo en una base de datos.