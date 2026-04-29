from datetime import datetime, date, time, timedelta, timezone

# 10. Crea una lista con varias fechas y ordenalas cronologicamente.


fecha_1= datetime(2025,11,11)
fecha_2= datetime(2024,11,11)
fecha_3= datetime(2027,11,11)
fecha_4= datetime(2029,11,11)
fecha_5= datetime(2000,11,11)

fechas= [fecha_1,fecha_2,fecha_3, fecha_4,fecha_5]
orden= sorted(fechas)
print(orden)
