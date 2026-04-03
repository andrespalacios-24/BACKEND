# ============================================================
# EJERCICIO - Sistema de usuarios
# ============================================================

# 1. Crea un diccionario con tus datos reales
datos= {"nombre":"ANDRES", "edad": 28, "ciudad": "buga", "profesion":"Programador"}

# 2. Pide al usuario con input() una nueva ciudad y actualiza el diccionario
#nueva_ciudad= print (input("defina nueva ciudad: "))
datos["ciudad"] = input("defina nueva ciudad:") #en este caso al input se le pueden quitar los ()
print(datos)
# 3. Agrega la clave "activo" con valor True
datos["activo"] =True #en estos casos va sin comillas porque lo convierte en str y no en boleano
print(datos)
# 4. Imprime un resumen con f-string
# Usuario: Andrés | Ciudad: Medellín | Profesión: Programador | Activo: True
print(f"usuario:{datos['nombre']} | ciudad: {datos['ciudad']} | profesion: {datos['profesion']} | activo: {datos['activo']}")
# procurar siempre dentro de los [] que no sea "" si no  '' estos simples ya que en algunas versiones de python puede dar error

# 5. Crea una lista "historial" con tres ciudades y agrégala al diccionario
lista_historial= ["tulua","popayan","caicedonia"]
datos["historial"]= lista_historial
# 6. Imprime cuántas ciudades tiene en el historial
print(len(datos["historial"])) #para contar el numero de datos en un diccionario se debe poner[] y no poner "" porque sino cuenta el numero de letras de la palabra
print(datos)
# 7. Verifica si "Bogotá" está en el historial
print("bogota"in datos["historial"])