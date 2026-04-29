# 1. Crea una variable con la fecha y hora actual.

# importar datetime
# crear variable fecha_hora
# hacer que se visualice con print
from datetime import datetime, date, time, timedelta, timezone

def fecha_hora():
 ahora= datetime.now()
 return ahora
 
print(fecha_hora())

# 2. Imprime solo el año, mes y di­a de la fecha actual.
fecha_local= datetime.now()
print(fecha_local.year)        
print(fecha_local.month)       
print(fecha_local.day)
# 3. Crea una fecha especi­fica: 25 de diciembre de 2025 y muestrala.
fecha_especifica= datetime(2025,12,25)
print(fecha_especifica)
# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hora= time(23,54,00)
print(hora.hour)
print(hora.minute)
print(hora.second)
# 5. Calcula cuantos di­as faltan para el 1 de enero del año siguiente.
dia_hoy= datetime.now()
primero_enero= datetime(2027,1,1)
dias_faltantes= primero_enero - dia_hoy
print(f"faltan: {dias_faltantes}, para el nuevo año")
# 6. Crea una funcion que reciba una fecha y devuelva su timestamp.
fecha= datetime.now()

def conversion_stamp(dato):
    ts= int(dato.timestamp())
    return ts

print(conversion_stamp(fecha))

# 7. Suma 30 di­as a la fecha actual usando timedelta.

treinta_dias= timedelta(days=30)
actualidad = datetime.now()
total_dias= actualidad + treinta_dias
print(f"En 30 dias sera la fecha sera: {total_dias}")

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 dias como simplificacion).

fecha_especifica= datetime(2025,12,25)
treinta_dias= timedelta(days=30)
fecha_mas_dias= fecha_especifica + treinta_dias
print(fecha_mas_dias)

# 9. Compara dos fechas y muestra cual es anterior.

fecha_1= datetime(2025,12,25)
fecha_2= datetime(2027,4,23)

def fechas_anterior(fecha_1,fecha_2):
    if fecha_1 < fecha_2:
        return (f"fecha 1 es anterior {fecha_1}") 
    else:
        return (f"fecha 2 es anterior {fecha_2}")
    
print(fechas_anterior(fecha_1,fecha_2))

# 10. Crea una lista con varias fechas y ordenalas cronologicamente.