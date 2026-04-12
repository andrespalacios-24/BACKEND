# Ejercicio 10
# Tienes esta lista de intentos de login con su resultado:
# intentos = [
#     {"usuario": "ana", "exitoso": True},
#     {"usuario": "luis", "exitoso": False},
#     {"usuario": "ana", "exitoso": False},
#     {"usuario": "pedro", "exitoso": True},
#     {"usuario": "luis", "exitoso": False},
#     {"usuario": "luis", "exitoso": False},
# ]
# Usa un bucle for para:
# - Contar los intentos fallidos por usuario
# - Imprimir los usuarios que tengan 2 o más intentos fallidos (posible ataque)
# Resultado esperado: luis tiene 3 intentos fallidos — ALERTA

intentos = [
     {"usuario": "ana", "exitoso": True},
     {"usuario": "luis", "exitoso": False},
     {"usuario": "ana", "exitoso": False},
     {"usuario": "pedro", "exitoso": True},
     {"usuario": "luis", "exitoso": False},
     {"usuario": "luis", "exitoso": False},
        ]

fallido=0
aceptado=0
for login in intentos:
    if (login["exitoso"]) ==False:
        fallido+=1

print(fallido)
    #else:
       # aceptado+=1
       