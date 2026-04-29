### Dates - Python Intermedio ###
# Módulos del paquete datetime:
# - datetime : fecha + hora combinadas
# - date     : solo fecha (año, mes, día)
# - time     : solo hora (hora, min, seg, microseg)
# - timedelta: representa una DURACIÓN (diferencia entre fechas)
# - timezone : para trabajar con zonas horarias (UTC, etc.)

from datetime import datetime, date, time, timedelta, timezone


# =============================================================================
# 1. DATETIME — Fecha y hora combinadas
# =============================================================================
# datetime.now()     → fecha/hora LOCAL del sistema (sin info de zona horaria)
# datetime.utcnow()  → DEPRECATED en Python 3.12 — todavía funciona pero lanza un warning.
#                      "Deprecated" significa que los creadores del lenguaje avisan que
#                      algo será eliminado en el futuro. Seguís usándolo hoy, pero no
#                      para siempre. Razón: devuelve un datetime sin zona horaria (naive),
#                      entonces Python no puede saber si es UTC, local u otra zona → bugs.
#                      Reemplazar por: datetime.now(timezone.utc)
# datetime.now(tz)   → fecha/hora con zona horaria explícita ✅ recomendado en backend
#                      El argumento tz NO toma la zona del sistema automáticamente.
#                      Vos le pasás explícitamente qué zona querés. Así el resultado
#                      es igual sin importar en qué servidor o país se ejecute el código.
#
# En backend siempre se trabaja con UTC para evitar problemas con usuarios
# de distintos países. La conversión a hora local la hace el frontend.

now_local = datetime.now()                       # Sin zona horaria (naive)
now_utc   = datetime.now(timezone.utc)           # Con UTC (aware) ✅ preferido en backend
# naive = el datetime no sabe en qué zona está. Es un número sin contexto.
# aware = el datetime sabe exactamente su zona. Python puede operar con él de forma segura.
# Mezclar naive y aware lanza TypeError — Python no te deja compararlos ni restarlos.

print("=== datetime ===")
print(now_utc)

# Atributos disponibles en un objeto datetime:
print(now_utc.year)        # Año        → ej: 2025
print(now_utc.month)       # Mes        → 1-12
print(now_utc.day)         # Día        → 1-31
print(now_utc.hour)        # Hora       → 0-23
print(now_utc.minute)      # Minuto     → 0-59
print(now_utc.second)      # Segundo    → 0-59
print(now_utc.microsecond) # Microseg   → 0-999999
print(now_utc.timestamp()) # UNIX timestamp (float) → segundos desde 1970-01-01 UTC
                           # Muy usado en APIs y bases de datos

# Crear un datetime manualmente:
fecha_especifica = datetime(2023, 1, 1, 12, 30, 0)  # año, mes, día, hora, min, seg
print(fecha_especifica)


# =============================================================================
# 2. DATE — Solo fecha
# =============================================================================
# date.today()  → fecha de hoy (sin hora)
# date(y, m, d) → fecha específica

print("\n=== date ===")
hoy = date.today()
print(hoy)
print(hoy.year, hoy.month, hoy.day)

fecha_manual = date(2022, 10, 6)
print(fecha_manual)

# Avanzar un mes (cuidado: date no tiene timedelta para meses directamente)
# Para meses se usa la librería dateutil (más adelante en manejo de paquetes)
fecha_siguiente = date(fecha_manual.year, fecha_manual.month + 1, fecha_manual.day)
print(fecha_siguiente)


# =============================================================================
# 3. TIME — Solo hora
# =============================================================================
# Representa un momento del día, sin fecha.
# Útil para horarios fijos (ej: hora de cierre, turno de trabajo).

print("\n=== time ===")
hora_cierre = time(21, 6, 0)   # hora, minuto, segundo
print(hora_cierre.hour)
print(hora_cierre.minute)
print(hora_cierre.second)


# =============================================================================
# 4. TIMEDELTA — Duración / diferencia entre fechas
# =============================================================================
# timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
# El resultado siempre se normaliza a: days + seconds + microseconds
#
# Casos de uso backend:
#   - Tokens JWT con expiración
#   - Tiempo restante de una sesión
#   - Calcular cuántos días lleva activo un usuario
#   - Ventanas de tiempo para reintentos o bloqueos

print("\n=== timedelta ===")

duracion_sesion = timedelta(hours=2)
inicio_sesion   = datetime.now(timezone.utc)
fin_sesion      = inicio_sesion + duracion_sesion

print(f"Sesión inicia : {inicio_sesion}")
print(f"Sesión expira : {fin_sesion}")

# Diferencia entre dos fechas
# tzinfo= es un parámetro nombrado del constructor de datetime, no una variable inventada.
# Firma completa: datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
# La zona horaria no tiene posición fija, por eso se pasa por nombre: tzinfo=timezone.utc
# Por defecto es None → datetime queda naive. Pasarlo explícitamente lo hace aware.
fecha_registro = datetime(2024, 1, 1, tzinfo=timezone.utc)
dias_activo    = datetime.now(timezone.utc) - fecha_registro
print(f"Días activo   : {dias_activo.days} días")

# Comparar timedeltas
delta_a = timedelta(weeks=10, days=200)
delta_b = timedelta(weeks=13, days=300)
print(delta_b - delta_a)
print(delta_b + delta_a)


# =============================================================================
# 5. FORMATEO — strftime y strptime
# =============================================================================
# strftime (string from time) → datetime → string legible
# strptime (string parse time)→ string   → datetime ← muy usado en APIs que reciben fechas
#
# Códigos más usados:
#   %Y → año 4 dígitos    %m → mes      %d → día
#   %H → hora (24h)       %M → minuto   %S → segundo
#   %f → microsegundos    %Z → zona     %z → offset UTC
#   %A → día nombre       %B → mes nombre (en inglés por defecto)

print("\n=== strftime / strptime ===")

# datetime → string (para mostrar al usuario o guardar en BD)
ahora = datetime.now(timezone.utc)
formato_iso     = ahora.strftime("%Y-%m-%dT%H:%M:%S%z")   # ISO 8601 ← estándar en APIs REST
formato_legible = ahora.strftime("%d/%m/%Y %H:%M")

print(f"ISO 8601  : {formato_iso}")
print(f"Legible   : {formato_legible}")

# string → datetime (para parsear fechas que llegan en un request)
fecha_str    = "2024-06-15T10:30:00+0000"
fecha_parsed = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S%z")
print(f"Parseada  : {fecha_parsed}")


# =============================================================================
# 6. ZONAS HORARIAS — timezone
# =============================================================================
# Un datetime "naive" (sin tz) puede causar bugs silenciosos en backend.
# Siempre trabajar con datetimes "aware" (con zona horaria).
#
# timezone.utc          → UTC puro
# timezone(timedelta()) → offset manual
# Para zonas como "America/Bogota" se usa la librería pytz o zoneinfo (Python 3.9+)

print("\n=== timezone ===")

from datetime import timezone

utc_now    = datetime.now(timezone.utc)
bogota_tz  = timezone(timedelta(hours=-5))          # Colombia UTC-5

# .astimezone(tz) → convierte el datetime a otra zona horaria.
# El instante que representa es el MISMO, solo cambian los números para expresarlo
# en la zona destino. Hace la conversión matemática real.
#
# Ejemplo de lo que produce:
#   utc_now    → 2025-04-29 20:00:00+00:00   (8pm UTC)
#   bogota_now → 2025-04-29 15:00:00-05:00   (3pm Colombia — el mismo instante)
bogota_now = utc_now.astimezone(bogota_tz)

print(f"UTC    : {utc_now}")
print(f"Bogotá : {bogota_now}")

# Diferencia entre .replace(tzinfo=...) y .astimezone(tz):
#
# .replace(tzinfo=...) → le PEGA una etiqueta de zona SIN tocar los números.
#                        Úsalo solo para convertir un naive en aware sin mover la hora.
# .astimezone(tz)      → CONVIERTE los números a la zona destino. ← lo que normalmente querés
#
# Ejemplo concreto de la diferencia:
#   utc = datetime(2025, 4, 29, 20, 0, 0, tzinfo=timezone.utc)
#   utc.replace(tzinfo=bogota_tz)   → 2025-04-29 20:00:00-05:00  ❌ hora incorrecta
#   utc.astimezone(bogota_tz)       → 2025-04-29 15:00:00-05:00  ✅ hora correcta


# =============================================================================
# 7. CONVERSIONES ÚTILES
# =============================================================================

print("\n=== conversiones ===")

# .date() → extrae solo la fecha de un datetime (descarta la hora)
# Útil cuando solo te importa el día, no el momento exacto.
# Ej backend: saber si un usuario se registró hoy, sin importar a qué hora.
solo_fecha = datetime.now().date()
print(solo_fecha)                        # → 2025-04-29

# datetime.combine(date, time) → une un date y un time en un datetime completo.
# Útil cuando tenés la fecha y la hora por separado y necesitás compararlos
# o hacer operaciones con timedelta.
# Ej backend: el usuario manda solo una fecha "2025-04-29", vos le agregás
# medianoche (00:00:00) para comparar con un datetime de BD.
solo_fecha_dt = datetime.combine(date.today(), time(0, 0, 0))
print(solo_fecha_dt)                     # → 2025-04-29 00:00:00

# datetime.fromtimestamp(ts, tz) → convierte un UNIX timestamp a datetime.
# Un UNIX timestamp es un número entero/float que representa los segundos
# transcurridos desde el 1 de enero de 1970 en UTC.
# Muchas APIs externas y bases de datos devuelven fechas en este formato.
# Ej backend: una API de pagos te devuelve {"created": 1700000000} y vos
# necesitás convertirlo a datetime para operar con él.
ts = 1700000000
desde_ts = datetime.fromtimestamp(ts, tz=timezone.utc)
print(f"Desde timestamp: {desde_ts}")    # → 2023-11-14 22:13:20+00:00

# .timestamp() → convierte un datetime a UNIX timestamp (el camino inverso).
# Útil cuando la BD o la API destino espera un número en vez de una fecha.
# Ej backend: guardás eventos en una BD que almacena fechas como enteros.
ts_de_nuevo = int(desde_ts.timestamp())
print(f"De vuelta a ts : {ts_de_nuevo}") # → 1700000000


# =============================================================================
# RESUMEN — ¿Cuándo uso cada cosa en backend?
# =============================================================================
# datetime.now(timezone.utc)   → guardar cuándo ocurrió algo (created_at, updated_at)
# timedelta                    → calcular expiración de tokens, sesiones, periodos
# strftime                     → datetime → string para devolver en una respuesta JSON
# strptime                     → string → datetime para parsear lo que llega en un request
# .timestamp()                 → datetime → número entero/float para BD o APIs que lo esperan
# fromtimestamp()              → número → datetime cuando una API externa te manda un timestamp
# .astimezone()                → convertir UTC a la zona del usuario al momento de responder
# .replace(tzinfo=...)         → convertir un datetime naive en aware SIN mover la hora
# .date()                      → extraer solo la fecha cuando la hora no importa
# datetime.combine(date, time) → unir fecha y hora separadas en un datetime operable
# date.today()                 → lógica de negocio que solo depende del día (sin hora)


#---------------------------------------------------------------------------------------
#                         EJEMPLO BACKEND CREADO POR OPEN AI
#---------------------------------------------------------------------------------------
# La funcion dates en Python se refiere al modulo datetime
# que permite trabajar con fechas y horas de manera efectiva

# Ejemplo 1: Registrar timestamps de operaciones en backend
def registrar_operacion(usuario_id, tipo_operacion):
    timestamp = datetime.now()
    print(f"Usuario: {usuario_id}")
    print(f"Operacion: {tipo_operacion}")
    print(f"Fecha y hora: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    return timestamp

registrar_operacion("USR-001", "login")

# Ejemplo 2: Calcular tiempo de expiracion de sesion
def generar_token_expiracion(minutos_validez=30):
    ahora = datetime.now()
    expiracion = ahora + timedelta(minutes=minutos_validez)
    print(f"Token generado a las: {ahora}")
    print(f"Expira a las: {expiracion}")
    return expiracion

generar_token_expiracion()