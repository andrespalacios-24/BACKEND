# encargado de la conexion a la base de datos
import os
from pymongo import MongoClient


# 1. Leemos la URI oculta desde las variables de entorno del servidor
MONGO_URL = os.environ.get("MONGO_URL")

# Creamos la conexión general al clúster usando la variable segura
client = MongoClient(MONGO_URL)

# 2. Especificamos la base de datos y la guardamos en la variable db_client que usan tus rutas
db_client = client.test