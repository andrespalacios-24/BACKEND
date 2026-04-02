### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

# len() devuelve la cantidad de caracteres del string
print(len(my_string))
print(len(my_other_string))

# Concatenación: une dos strings con +
print(my_string + " " + my_other_string)

# \n genera un salto de línea dentro del string
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

# \t genera una tabulación (sangría) dentro del string
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# \\ escapa el carácter especial, lo imprime literalmente
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo
# Las 4 formas producen el mismo resultado
# En Python moderno se usan f-strings (forma 4)
# Las otras formas son antiguas, útiles para reconocerlas en código ajeno

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # Forma 1 - antigua
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))      # Forma 2 - antigua
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))  # Forma 3 - incómoda, hay que convertir todo a str manualmente
print(f"Mi nombre es {name} {surname} y mi edad es {age}")              # Forma 4 - f-string, estándar actual

# Desempaquetado de caracteres
# Python asigna cada letra a una variable, en orden
# El número de variables debe coincidir exactamente con el número de letras
# Si hay más o menos variables → ValueError

language = "python"
a, b, c, d, e, f = language
print(a)  # p → posición 0
print(e)  # o → posición 4

# División (Slicing)
# Permite extraer partes de un string usando la estructura [inicio:fin:paso]
# Las posiciones empiezan desde 0:
# p  y  t  h  o  n
# 0  1  2  3  4  5

# Toma desde posición 1 hasta 3, sin incluir el 3
language_slice = language[1:3]
print(language_slice)  # yt

# Toma desde posición 1 hasta el final
language_slice = language[1:]
print(language_slice)  # ython

# Posición negativa cuenta desde el final hacia atrás
# n=-1, o=-2 → devuelve "o"
language_slice = language[-2]
print(language_slice)  # o

# Toma desde 0 hasta 6, avanzando de 2 en 2 (paso)
# Posición 0=p, 2=t, 4=o → posición 6 no existe, para
language_slice = language[0:6:2]  #python incia desde el 0 o la P 
print(language_slice)  # pto  el 0 es desde la posicion que inicia, el 6 las casilas o letras que recorrera el 2 es de cuanto en cuanto se correran 

# Reverse: paso -1 recorre el string al revés
reversed_language = language[::-1]
print(reversed_language)  # nohtyp este empieza desde atras y lo recorre alrevez 

# Funciones del lenguaje
# Son herramientas incorporadas de Python para trabajar con strings
# Los nombres en inglés son descriptivos — úsalos para deducir qué hacen

language = "python"

language.capitalize()  # Python → solo la primera letra en mayúscula
language.upper()       # PYTHON → todo en mayúscula
language.lower()       # python → todo en minúscula

# Python es case sensitive → mayúsculas y minúsculas no son lo mismo
# Por eso se usa lower() antes de comparar datos del usuario
language.startswith("Py")  # False → "python" empieza con "p" minúscula, no "P"
language.startswith("py")  # True
"Py" == "py"               # False → no son iguales para Python

# count() cuenta cuántas veces aparece un carácter dentro del string
language.count("t")  # 1 → la letra "t" aparece una vez en "python"

# Las funciones que empiezan con "is" verifican y responden True o False
language.isnumeric()   # False → "python" no es un número
"1".isnumeric()        # True  → "1" sí es numérico

# Encadenamiento: se pueden aplicar varias funciones seguidas
# Python ejecuta de izquierda a derecha
language.lower().isupper()  # False → primero pasa a minúscula, luego verifica si está en mayúscula

# Operador "in"
# Verifica si un valor está dentro de un string
# Responde True o False
# Se lee literalmente: "¿está X en Y?"

email = "andres.palacios@gmail.com"
print("@" in email)       # True  → "@" sí está en el email
print("@" not in email)   # False → "not in" es lo contrario, verifica si NO está
print("z" in email)       # False → "z" no está en el email
print("gmail" in email)   # True  → también funciona con palabras completas

# Método strip()
# Elimina espacios en blanco al inicio y al final de un string
# No elimina espacios en el medio
# Muy usado en backend para limpiar datos que vienen del usuario

usuario = "  andres_palacios  "
print(usuario.strip())   # "andres_palacios" → eliminó espacios de ambos extremos

# También existen versiones más específicas:
print(usuario.lstrip())  # "andres_palacios  " → solo elimina espacios a la izquierda (left)
print(usuario.rstrip())  # "  andres_palacios" → solo elimina espacios a la derecha (right)

# Caso real: un usuario escribe su email con espacios accidentales
email = "  andres@gmail.com  "
print(email.strip())     # "andres@gmail.com" → limpio y listo para guardar en base de datos