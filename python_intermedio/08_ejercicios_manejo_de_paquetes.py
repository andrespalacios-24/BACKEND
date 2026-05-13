import numpy   
import requests
# 1. Importa el módulo math y muestra el valor de pi.
import math
print(math.pi)
     
# 2. Crea un array de números usando numpy y multiplícalo por 3.
lista= numpy.array([14,1,59,2,65,35,897,93])
print(lista * 3)

# 3. Muestra la versión instalada de numpy.
version= numpy.version.version
print(version)

# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.
api_requests= requests.get("https://pokeapi.co/api/v2/pokemon?")
print(api_requests.status_code)

# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.
from my_package import arithmetics
print(arithmetics.sum_two_values(5,5))

# 6. Usa pandas para crear un DataFrame con nombres en español.
import pandas as pd 
usuarios= {
    "nombres":["maikel","robert","kiyo","reinaldo"],
    "edad": [99,98,105,100]
}
df= pd.DataFrame(usuarios)
print(df)

# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.
# pip3 install requests

# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.
api_requests= requests.get("https://pokeapi.co/api/v2/pokemon?")
nombres= api_requests.json()["results"]
for x in nombres:
 print(x["name"]) 


# 9. Muestra todos los paquetes instalados con pip desde la terminal.
# pip3 list
# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.
help(numpy)