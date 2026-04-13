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

fallo_usuario={}
aceptado_usuario=[]
fallido=0
aceptado=0
for login in intentos:
    if (login["exitoso"]) ==False:
       fallo_usuario["usuario"[login]] +=1
    else:
        aceptado_usuario["usuario"[login]] +=1
if fallido >=2:
    print("posible ataque")
else:
    print("siga")