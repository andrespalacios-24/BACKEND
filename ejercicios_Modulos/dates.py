# 10 Crea un modulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este modulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especificas.
import datetime
def fecha_actual():
    return datetime.date.today()

def diferencia_fechas(año,mes,dia):
    fecha_actual= datetime.date.today()
    fecha_pasada= datetime.date(año,mes,dia)
    diferencia= (fecha_actual - fecha_pasada)
    return diferencia

print(diferencia_fechas(2026,3,23))