# =============================================================================
# EXPLICACIÓN DE EJERCICIOS - PYTHON INTERMEDIO
# MoureDev Roadmap - Andrés Palacios
# Referencia: https://docs.python.org/3/
# =============================================================================


# =============================================================================
# 1. FIZZBUZZ
# =============================================================================
# ¿QUÉ hace?
#   Recorre los números del 1 al 100 e imprime:
#     - "fizzbuzz" si el número es múltiplo de 3 Y de 5 a la vez
#     - "fizz"     si solo es múltiplo de 3
#     - "buzz"     si solo es múltiplo de 5
#     - el número  si no cumple ninguna condición anterior
#
# ¿POR QUÉ así?
#   • range(1, 101): en Python range() excluye el límite superior,
#     por eso se escribe 101 para incluir el 100.
#     Docs: https://docs.python.org/3/library/stdtypes.html#range
#
#   • Operador módulo (%): devuelve el RESTO de una división.
#     Si index % 3 == 0, significa que 3 cabe exactamente, es decir,
#     el número es múltiplo de 3. Lo mismo con 5.
#     Docs: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
#
#   • ORDEN de los if/elif: el caso "múltiplo de 3 Y de 5" se evalúa
#     PRIMERO (con `and`). Si lo pusiéramos después del elif de 3,
#     el 15 caería en "fizz" y nunca llegaría a "fizzbuzz". El orden
#     importa en los condicionales encadenados.
#     Docs: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
#
#   • print() sin argumento extra ya agrega salto de línea por defecto.
#     Docs: https://docs.python.org/3/library/functions.html#print

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()


# =============================================================================
# 2. ¿ES UN ANAGRAMA?
# =============================================================================
# ¿QUÉ hace?
#   Recibe dos palabras y devuelve True si son anagramas, False si no.
#   Un anagrama = mismas letras, diferente orden (ej: "Amor" / "Roma").
#   Dos palabras IGUALES no cuentan como anagrama.
#
# ¿POR QUÉ así?
#   • .lower(): convierte ambas palabras a minúsculas antes de comparar,
#     para que "Amor" y "amor" se traten igual. Sin esto, 'A' != 'a'.
#     Docs: https://docs.python.org/3/library/stdtypes.html#str.lower
#
#   • Primer if — palabras iguales: si word_one.lower() == word_two.lower(),
#     son exactamente la misma palabra → retorna False directamente.
#     Esto cumple la regla "dos palabras iguales no son anagrama".
#
#   • sorted(): convierte el string en una lista de caracteres ordenados
#     alfabéticamente. Si los dos strings tienen exactamente las mismas
#     letras, sus listas ordenadas serán idénticas → True.
#     Ejemplo: sorted("amor") → ['a', 'm', 'o', 'r']
#              sorted("roma") → ['a', 'm', 'o', 'r']  ← iguales!
#     Docs: https://docs.python.org/3/library/functions.html#sorted
#
#   • La función RETORNA el resultado booleano de la comparación.
#     No usa print() porque el enunciado pide retornar verdadero/falso,
#     no imprimirlo. Quien llama a la función decide qué hacer con el valor.
#     Docs: https://docs.python.org/3/reference/simple_stmts.html#return

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))   # True
print(is_anagram("hola", "hola"))   # False  ← misma palabra
print(is_anagram("hola", "adios"))  # False  ← letras distintas


# =============================================================================
# 3. SUCESIÓN DE FIBONACCI
# =============================================================================
# ¿QUÉ hace?
#   Imprime los primeros 50 números de la serie Fibonacci: 0, 1, 1, 2, 3, 5...
#   Cada número es la suma de los dos anteriores.
#
# ¿POR QUÉ así?
#   • Se usan DOS variables (prev, next) para rastrear el estado actual
#     de la serie. No se necesita una lista completa; solo los dos
#     últimos valores en cada momento → más eficiente en memoria.
#
#   • Se evita usar `next` como nombre de variable en código real porque
#     es una función built-in de Python. Aquí se usa por claridad didáctica,
#     pero en producción se usaría `curr` o `b`.
#     Docs built-ins: https://docs.python.org/3/library/functions.html#next
#
#   • range(0, 50): 50 iteraciones, desde índice 0 hasta 49.
#     En cada vuelta se imprime `prev`, luego se calcula el siguiente,
#     y se "deslizan" las variables:
#       fib  = prev + next   ← nuevo número calculado
#       prev = next           ← prev avanza al siguiente
#       next = fib            ← next toma el valor recién calculado
#
#   • ORDEN importa: si actualizáramos prev antes de calcular fib,
#     perderíamos el valor original de prev. La variable temporal `fib`
#     guarda el resultado antes de reasignar.
#     Alternativa Pythónica (sin variable temporal):
#       prev, next = next, prev + next
#     Esto funciona porque Python evalúa TODA la parte derecha
#     antes de asignar. Docs: https://docs.python.org/3/reference/simple_stmts.html#assignment-statements

def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()


# =============================================================================
# 4. ¿ES UN NÚMERO PRIMO?
# =============================================================================
# ¿QUÉ hace?
#   Imprime todos los números primos entre 1 y 100.
#   Un número primo es divisible ÚNICAMENTE por 1 y por sí mismo.
#
# ¿POR QUÉ así?
#   • Se empieza desde 2 porque 1 NO es primo por definición matemática.
#     El if `number >= 2` descarta el 1.
#
#   • is_divisible = False: se asume que el número NO es divisible
#     hasta que se demuestre lo contrario. Es el patrón "inocente hasta
#     que se pruebe culpable".
#
#   • El bucle interno recorre desde 2 hasta number-1 (range(2, number)):
#     si algún número en ese rango divide exactamente a `number`,
#     entonces NO es primo → se marca is_divisible = True y se hace break.
#     Docs break: https://docs.python.org/3/reference/simple_stmts.html#break
#
#   • break: interrumpe el bucle inmediatamente en cuanto se encuentra
#     un divisor. No tiene sentido seguir buscando si ya sabemos que no es primo.
#     Esto optimiza el rendimiento.
#
#   • Si is_divisible sigue siendo False después del bucle interno,
#     significa que nadie lo dividió → es primo → se imprime.
#
#   NOTA: range(2, number) cuando number == 2 produce un rango vacío,
#   así que el bucle no se ejecuta, is_divisible queda False, y 2 se imprime
#   correctamente como primo.

def is_prime():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()


# =============================================================================
# 5. INVIRTIENDO CADENAS
# =============================================================================
# ¿QUÉ hace?
#   Invierte el orden de los caracteres de un string SIN usar slicing [::-1]
#   ni reversed() ni métodos automáticos del lenguaje.
#   "Hola mundo" → "odnum aloH"
#
# ¿POR QUÉ así?
#   • len(text): devuelve el número total de caracteres del string.
#     Docs: https://docs.python.org/3/library/functions.html#len
#
#   • reversed_text = "": se inicializa un string vacío donde se irán
#     concatenando los caracteres en orden inverso.
#
#   • La lógica del índice invertido:
#       text[text_len - index - 1]
#     Cuando index = 0  → text[len-1]  = último carácter
#     Cuando index = 1  → text[len-2]  = penúltimo
#     ...y así hasta el primero.
#     El -1 compensa que los índices en Python empiezan en 0.
#     Docs indexing: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
#
#   • += concatena el nuevo carácter al string acumulado.
#     Equivale a: reversed_text = reversed_text + text[text_len - index - 1]
#
#   • La función RETORNA el string invertido (no lo imprime).
#     Quien la llama decide qué hacer. Aquí el print() está afuera.
#
#   NOTA: En Python los strings son INMUTABLES, así que cada += crea un
#   nuevo objeto string. Para textos muy largos sería más eficiente usar
#   una lista y luego "".join(). Para el alcance de este ejercicio está bien.
#   Docs inmutabilidad: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))   # odnum aloH