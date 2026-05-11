import re
palabra= "Hola este es un ejemplo jejeje"

# 1. Busca si una cadena empieza por "Hola".
#pseudocode.
#se crea una variable donde ira el re.
#se usa el match porque especificamente necesitamos saber si empieza por una palabra especifica
#se usa r para colocar el patron especifico de str
# se especifica despues del patron con una coma la variable donde esta la cadena
# se imprime el resultado
#-------------------------------------------------------------------------------------------------
inicial= re.match(r"Hola", palabra)
print(inicial)
# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.
palabra= "uno de los lenguajes de programacion mas usados es Python"
#pseudocodigo
#se crea la variable donde ira el re.
#se una search ya que necesita buscar en la cadena no al inicio
#dentro se search se pone la r y el patron a buscar
#se pone el reI ya que necesitamos ignorar si son mayusculas o minusculas
#---------------------------------------------------------------------------
busqueda= re.search(r"python", palabra, re.I)
print(busqueda)
#----------------------------------------------------------------------------
# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
texto="Inscribirse en este curso online es el primer paso para mejorar tu perfil profesional. Nuestro curso de marketing digital incluye materiales actualizados y tutorías personalizadas. Además, al finalizar el curso intensivo, recibirás un certificado oficial. No pierdas la oportunidad de acceder a un curso diseñado por expertos del sector."
#pseudocode
#se crea variable donde ira el re.
#se usa findall para que retorne una lista con el patron a buscar
#se pone la variable que contiene la cadena de texto donde se buscara
#se pone re.I 
#---------------------------------------------------------------------
todo_texto= re.findall(r"curso",texto, re.I)
print(todo_texto)
#---------------------------------------------------------------------

# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".
#pseudocode
#se crear la variable para el re.
#se una sub para reemplazar un patron por otro en una cadena
#dentro de sub se pone la palabra:  cambiar, seguido de la palabra que sera el reemplazo 
#se puede usar un [] con la primera letra en mayuscula y minuscula para que no se queda alguna por fuera
#----------------------------------------------------------------------------------------------------------
texto="Cada lección de este programa está diseñada para ser breve pero efectiva. Al completar una lección, el sistema desbloquea automáticamente la siguiente lección del módulo. Es fundamental no saltarse ninguna lección para comprender el concepto global, ya que cada lección construye la base del examen final."
reemplazo= re.sub(r"[lL]ección", "LECCIÓN",texto)
print(reemplazo)
#----------------------------------------------------------------------------------------------------------
# 5. Divide un texto en partes separadas por comas.
#pseudocodoe
#se crea una variable con el re
#se usa split para dividir el str que este separado en este caso por comas (,)
#dentro de split se pone la separacion y la variable que contiene el str
#------------------------------------------------------------------------------
texto="La vida es una lección constante, aprendí una lección de mis errores, cada lección nos ayuda a crecer, valora cada lección aprendida, no olvides la lección del pasado, la mejor lección es la experiencia."

split= re.split(r",", texto)
print(split)
#------------------------------------------------------------------------------
# 6. Busca la primera palabra que comience con "A" o "a".
#pseudocode
#se crea la variable con el re.
#se una search para buscar entre todo
#se pone re.I para que no distinga de mayuscula o minuscula 
#---------------------------------------------------------------------------------
letras="La vida es una lección constante, aprendí una lección de mis errores, cada lección nos ayuda a crecer, valora cada lección aprendida, no olvides la lección del pasado, la mejor lección es la experiencia."

busca= r"\b[Aa]\w*\b"
resultado= re.search(busca,letras)
print(resultado)
#-------------------------------------------------------------------------------------
# 7. Encuentra todas las palabras en una cadena que terminen en "ción".
#pseudocode
#se crea variable para re.
#se usa findall para buscar entre toda la str
#se crear variable donde ira el patron de los parametros:
#\b\w* \b donde al ir w antes que la palabra o letra donde reemplaza lo que va antes de la palabra fija a buscar 
#----------------------------------------------------------------------------------------------------------------
patron= r"\b\w*ción\b"
terminal= re.findall(patron, letras)
print(terminal)
# 8. Verifica si una cadena contiene solo números.
#pseudocode
#crear funcion donde se verifique que la cadena contiene solo numeros
#crear el patron de busqueda = r"^\d+$" donde ^$ indican que debe iniciar y terminar con el patron requerido
#usar if para retornar true y else para retornar false
#-------------------------------------------------------------------------------------------------------------
def solo_numeros(str):
   condicion= r'^\d+$'
   if re.search(condicion, str):
      return True
   else:
      return False
#--------------------------------------------------------------------------------------------------------------
#con una sola linea 
def solo_numeros(str):
    return bool(re.search(r'^\d+$', str))
#---------------------------------------------------------------------------------------------------------------
print(solo_numeros("231934209423"))
print(solo_numeros("olik"))
# 9. Reemplaza todos los números de una cadena por el texto "[número]".
#pseudocode
#crear variable para usar el re.
#usar sub para sustituir numeros por texto 
#donde usaremos [0-9] y que se reemplace por numero
#-------------------------------------------------------------
texto= "su numero de cuenta es: 12345678, por favor confirmar"
reemplaza_numeral= re.sub(r"\d+","***número***",texto)
print(reemplaza_numeral)
#--------------------------------------------------------------
# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
#pseudocode
#crear variable para usar el re.
#se usa findall para buscar en todo el str
#se usa el patron= r"\b\w{n}\b" donde \b indica el limite de la palabra
# \w indica que es cualquier caracter alfanumerico y {n} indica el numero de letras que contiene
#--------------------------------------------------------------------------
texto="Sol, camino, luna, mar, puente, casa, pájaro, pan, vida, espejo, luz, gato, fuerte, flor, verano, sal, mano, jardín, ojo, nube, cocina, río, azul, tomate"
patron= r"\b\w{4}\b"
cuatro_letras= re.findall(patron, texto)
print(cuatro_letras)
#------------------------------------------------------------------------------