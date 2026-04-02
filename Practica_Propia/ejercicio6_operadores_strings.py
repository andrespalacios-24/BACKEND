### Práctica: Operadores y Strings ###

# Ejercicio 1
# Un usuario se registra con el email "andres.palacios@gmail.com"
# Verifica si el email contiene una "@" usando el método adecuado e imprime True o False.
email="andres.palacios@gmail.com"
print("@" in email)
# Ejercicio 2
# Tienes un servidor con 512 GB de almacenamiento total. Está ocupado en un 75%.
# Calcula cuántos GB quedan libres e imprímelo con f-string.
almacenamiento= int(512)
almacenamiento_libre= int(almacenamiento - (almacenamiento * 75) / 100)
print(almacenamiento_libre)
print(f"quedan {almacenamiento_libre}GB de {almacenamiento} disponible en el servidor")
# Ejercicio 3
# Un usuario ingresa su contraseña como "MiClave123".
# Conviértela a minúsculas y verifica si es igual a "miclave123". Imprime el resultado.
contraseña="MiClave123"
print (contraseña.lower()== "miclave123") 

# Ejercicio 4
# Tienes un token de acceso "tkn_AB12CD34EF".
# Extrae usando slicing solo la parte "AB12CD34EF" — sin el prefijo "tkn_".
token="tkn_AB12CD34EF"
slicing= token[4:]
print(slicing)
# Ejercicio 5
# Un sistema recibe el nombre de usuario "  andres_palacios  " con espacios.
# Investiga el método strip() y úsalo para eliminar los espacios. Luego imprímelo en mayúsculas.
usuario="  andres_palacios  "
print(usuario.strip().upper())