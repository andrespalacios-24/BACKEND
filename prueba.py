# ARCHIVO_JSON = "python_intermedio/agenda.json"


# def cargar_contactos():
#crear una funcion para cargar el archivo json (read)
# usar try except para manejar el error que no exista el archivo
# usar with open para que cierre automaticamente 
# poner la ubicacion del archivo donde abrira el json y se sobreescribira 
# usar el json.load para cargar el archivo. 
# despues del manejo del filenofound retornar una lista vacia     
# 
def cargar_contactos():
    try:
        with open("python_intermedio/agenda.json","r", encoding="utf-8")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []



# def guardar_contactos(contactos):
# crear funcion donde guardar el archivo json    
# usar el with open para cerrado automatico 
#usar la ubicacion donde el archivo se sobreescribira 
# para esto se usa "w" 
# usar el .dump donde adentro ira ident=4 para que sea legible por humanos
# dentro del dump ira el contacto y el archivo donde se sobreescribira 
# usar el ensure_ascii=False para poder que los nombres seal legibles por humanos

def guardar_contactos(contactos):
    with open("python_intermedio/agenda.json","w",encoding="utf-8")as archivo:
        json.dump(contactos, archivo, indent=4, ensure_ascii=False)

# def agregar_contacto(contactos):
# pedir nombre con input()
# pedir telefono con input()
# pedir email con input()
# crear diccionario con esos tres valores
# agregar el diccionario a la lista con append
# llamar a guardar_contactos(contactos)
# pseudocode validacion que correo contenga @ y .
#se agrega bucle while true para que se repita hasta que se agrege un correo valido
#se usa if para validar que contenga el @ y el . con in
#si el correo no es valido imprime correo invalido debe contener @ y .
# si es valido se usa break para parar el while 
def agregar_contacto(contactos):
    nombre= input("escribir nombre de nuevo contacto: ")
    telefono= input("escribir telefono de nuevo contacto: ")
    while True:
        email= input("escribir email de nuevo contacto")
        if "@" in email and "." in email:
            break
        else: print("correo no valido, debe contener (@) y (.) ")

    nuevos = {
        "nombre":nombre,
        "telefono": telefono,
        "email": email
    }
    
    contactos.append(nuevos)
    guardar_contactos(contactos)