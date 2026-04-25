# ============================================================
#           CLASES EN PYTHON - GUÍA DE REFERENCIA
#           Orientada a Backend | MoureDev + Conceptos clave
# ============================================================

# ¿Qué es una clase?
# Una clase es una PLANTILLA o MOLDE para crear objetos.
# Define qué propiedades (datos) y métodos (acciones) tendrán
# los objetos creados a partir de ella.
#
# En backend se usan para modelar entidades del sistema:
#   → Usuarios, Productos, Pedidos, Conexiones a BD, etc.
#
# Terminología clave:
#   - Clase     : la plantilla (ej. Person)
#   - Objeto    : una instancia concreta de la clase (ej. my_person)
#   - Atributo  : variable que pertenece al objeto
#   - Método    : función que pertenece a la clase
#   - Instanciar: crear un objeto a partir de una clase

# ============================================================
# 0. PARTES DE UNA CLASE 
# ============================================================

class Libro:              # ← la CLASE (el molde)

    def __init__(self, titulo, autor, anio):   # ← el CONSTRUCTOR
        self.titulo = titulo    # ← ATRIBUTOS (guardan la info)
        self.autor = autor
        self.anio = anio

    def __str__(self):          # ← MÉTODO (una acción/función del objeto)
        return f"..."

# ============================================================
# 1. CLASE VACÍA
# ============================================================

class MyEmptyPerson:
    pass  # 'pass' permite dejar el cuerpo de la clase vacío por ahora

# Imprimir la CLASE (la plantilla en sí)
print(MyEmptyPerson)       # → <class '__main__.MyEmptyPerson'>

# Imprimir un OBJETO (una instancia de la clase)
print(MyEmptyPerson())     # → <__main__.MyEmptyPerson object at 0x...>

# USO EN BACKEND:
# Clases vacías sirven como punto de partida al diseñar modelos.
# También se usan como clases base (herencia) o para errores personalizados.
# Ejemplo: class DatabaseError(Exception): pass


# ============================================================
# 2. CLASE CON CONSTRUCTOR, MÉTODOS Y PROPIEDADES
# ============================================================

class Person:

    # ── CONSTRUCTOR ──────────────────────────────────────────
    # __init__ es el constructor: se ejecuta AUTOMÁTICAMENTE
    # cada vez que se crea un objeto de esta clase.
    # 'self' es una referencia al objeto que se está creando.
    # Los parámetros se reciben igual que en cualquier función.
    # 'alias="Sin alias"' es un parámetro con valor por defecto.

    def __init__(self, name, surname, alias="Sin alias"):

        # Propiedad PÚBLICA: accesible desde fuera de la clase
        self.full_name = f"{name} {surname} ({alias})"

        # Propiedad PRIVADA: el doble guion bajo (__) indica que
        # no debe accederse directamente desde fuera de la clase.
        # Python la "ofusca" como _Person__name internamente.
        self.__name = name

    # ── GETTER (método de acceso) ─────────────────────────────
    # Permite leer una propiedad privada de forma controlada.
    # En backend esto es clave: nunca expones datos sensibles
    # (contraseñas, tokens) directamente; los devuelves procesados.

    def get_name(self):
        return self.__name

    # ── MÉTODO DE COMPORTAMIENTO ──────────────────────────────
    # Acción que el objeto puede realizar.
    # En backend: send_email(), hash_password(), to_json(), etc.

    def walk(self):
        print(f"{self.full_name} está caminando")


# ============================================================
# 3. CREAR OBJETOS (INSTANCIAR)
# ============================================================

# Sin alias → usa el valor por defecto "Sin alias"
my_person = Person("Brais", "Moure")
print(my_person.full_name)    # → Brais Moure (Sin alias)
print(my_person.get_name())   # → Brais   (acceso controlado a __name)
my_person.walk()              # → Brais Moure (Sin alias) está caminando

# Con alias personalizado
my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)   # → Brais Moure (MoureDev)
my_other_person.walk()             # → Brais Moure (MoureDev) está caminando


# ============================================================
# 4. MODIFICAR PROPIEDADES PÚBLICAS
# ============================================================

# Las propiedades públicas se pueden cambiar directamente.
# ⚠️ Python NO valida el tipo de dato → puedes asignar cualquier cosa.
# En backend esto es un riesgo: si full_name debe ser str,
# asignar un int puede romper lógica más adelante.

my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)   # → Héctor de León (El loco de los perros)

my_other_person.full_name = 666    # ⚠️ Python lo permite, pero es incorrecto
print(my_other_person.full_name)   # → 666


# ============================================================
# 5. PROPIEDADES PRIVADAS - INTENTO DE ACCESO DIRECTO
# ============================================================

# Intentar acceder a __name directamente lanzará AttributeError:
# print(my_person.__name)  → ❌ AttributeError

# La forma correcta siempre es el getter:
print(my_person.get_name())  # ✅ → Brais


# ============================================================
# 6. RESUMEN VISUAL DE LA ESTRUCTURA
# ============================================================

# class NombreClase:
# │
# ├── def __init__(self, param1, param2, param_opcional="default"):
# │       self.atributo_publico  = valor      # accesible desde fuera
# │       self.__atributo_privado = valor     # solo accesible dentro
# │
# ├── def get_atributo_privado(self):         # getter
# │       return self.__atributo_privado
# │
# └── def metodo(self):                       # comportamiento
#         # lógica del método


# ============================================================
# 7. USO EN BACKEND - EJEMPLOS REALES
# ============================================================

# En un servidor FastAPI o Django, las clases modelan los datos:
#
#   class User:
#       def __init__(self, username, email, password):
#           self.username = username
#           self.email = email
#           self.__password = hash_password(password)  # nunca en claro
#
#       def check_password(self, raw_password):
#           return verify_hash(raw_password, self.__password)
#
#       def to_dict(self):  # para serializar a JSON en la API
#           return {"username": self.username, "email": self.email}
#
#   class APIResponse:
#       def __init__(self, data, status=200):
#           self.data = data
#           self.status = status
#
#       def to_json(self):
#           return {"status": self.status, "data": self.data}


# ============================================================
# 8. PRÓXIMOS CONCEPTOS RELACIONADOS
# ============================================================

# → Herencia        : una clase hija reutiliza y extiende una clase madre
# → @property       : decorador para getters/setters más limpios en Python
# → Métodos de clase (@classmethod) y estáticos (@staticmethod)
# → __str__ / __repr__: controlar cómo se imprime un objeto
# → Dataclasses     : forma moderna y concisa de crear clases de datos
# → ORM (SQLAlchemy, Django ORM): las clases se mapean a tablas de BD

# ============================================================
# GETTER Y SETTER EN PYTHON
# ============================================================

# GETTER: método para OBTENER el valor de un atributo privado
# SETTER: método para CAMBIAR el valor de un atributo privado

# Los atributos privados se definen con doble guion bajo (__)
# No son accesibles directamente desde fuera de la clase

class Book():
    def __init__(self, title, author):
        self.title = title       # atributo publico
        self.__author = author   # atributo privado

    # GETTER - obtiene el valor del atributo privado
    def obtener_author(self):
        return self.__author

    # SETTER - cambia el valor del atributo publico
    def cambiar_title(self, nuevo_title):
        self.title = nuevo_title

libro = Book("mi gatito miau", "el gatito")

# Usando getter
print(libro.obtener_author())     # "el gatito"

# Usando setter
libro.cambiar_title("mi perrito guau")
print(libro.title)                # "mi perrito guau"