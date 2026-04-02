### Práctica Propia: Listas ###

# Ejercicio 1
# Tienes una lista de usuarios registrados: ["andres", "juan", "maria", "carlos", "pedro"]
# Imprime cuántos usuarios hay, el primero y el último.
usuarios=["andres", "juan", "maria", "carlos", "pedro"]
print(len(usuarios))
print(usuarios[0])
print(usuarios[-1])
# Ejercicio 2
# Un servidor maneja estos códigos de error: [404, 500, 403, 401, 500, 404, 200]
# Imprime cuántas veces aparece el error 500 y en qué posición aparece por primera vez el 403.
cod_error=[404, 500, 403, 401, 500, 404, 200]
print(cod_error.count(500))
print(cod_error.index(403))
# Ejercicio 3
# Tienes la lista de precios de tres planes: [9.99, 19.99, 49.99]
# Agrega un nuevo plan de 99.99 al final e inserta un plan de 4.99 en la posición 0.
# Imprime la lista final.
lista_precios=  [9.99, 19.99, 49.99]
lista_precios.append(99.99)
lista_precios.insert(0, 4.99)
print(lista_precios)
# Ejercicio 4
# Lista de endpoints activos: ["/login", "/registro", "/perfil", "/admin", "/logout"]
# Elimina "/admin" con remove(), luego elimina el último endpoint con pop() y guárdalo en una variable.
# Imprime la variable y la lista final.
lista_endpoint=["/login", "/registro", "/perfil", "/admin", "/logout"]
lista_endpoint.remove("/admin")
borrador= lista_endpoint.pop()
print(borrador)
print(lista_endpoint)
# Ejercicio 5
# Tienes los tiempos de respuesta de un servidor en ms: [320, 150, 480, 90, 210]
# Ordénalos de menor a mayor, imprímelos, luego inviértelos e imprímelos.
# Crea una sublista con los 3 tiempos del medio e imprímela.
tiempos_de_respuesta= [320, 150, 480, 90, 210]
tiempos_de_respuesta.sort()
print(tiempos_de_respuesta)
tiempos_de_respuesta.reverse()
print(tiempos_de_respuesta)
sublista= tiempos_de_respuesta[1:4]
print(sublista)