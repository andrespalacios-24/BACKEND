"""
PROYECTO 2 — Reloj de cuenta regresiva (Pomodoro)
==================================================
Temporizador Pomodoro por consola con ciclos de trabajo y descanso.

Ciclo Pomodoro estándar:
    - 25 min de trabajo
    - 5 min de descanso corto
    - Después de 4 pomodoros: 15 min de descanso largo

Módulos que vas a necesitar:
    - time      : time.sleep() para pausar la ejecución segundo a segundo
    - datetime  : (opcional) si quieres mostrar la hora de inicio/fin
    - os        : (opcional) os.system("clear") o os.system("cls") para limpiar pantalla

Flujo general del programa:
    1. Mostrar menú o configuración inicial
    2. Ejecutar un ciclo Pomodoro:
        a. Countdown de trabajo (25 min)
        b. Avisar que terminó el trabajo
        c. Countdown de descanso (5 o 15 min según el ciclo)
        d. Avisar que terminó el descanso
    3. Preguntar si continuar con otro ciclo
"""

import time


# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────────

TIEMPO_TRABAJO = 5        # 25 minutos en segundos
TIEMPO_DESCANSO_CORTO = 3  # 5 minutos en segundos
TIEMPO_DESCANSO_LARGO = 5 # 15 minutos en segundos
CICLOS_PARA_DESCANSO_LARGO = 4  # cada cuántos pomodoros hay descanso largo


# ── FUNCIONES ──────────────────────────────────────────────────────────────────

def formatear_tiempo(segundos_totales):
    """
    Convierte segundos a formato MM:SS.
    Ejemplo: 90 -> "01:30"

    Pista: usa división entera (//) y módulo (%) para separar minutos y segundos.
    Para el formato usa f-string con relleno de ceros: f"{minutos:02d}:{segundos:02d}"
    """
    # TODO: 
    minutos, segundos = divmod(segundos_totales,60)
    return f"{minutos:02d}:{segundos:02d}"


def cuenta_regresiva(segundos_totales, etiqueta):
    """
    Ejecuta una cuenta regresiva mostrando el tiempo restante en consola.
    Actualiza la misma línea en lugar de imprimir una nueva cada vez.

    Parámetros:
        segundos_totales : int   — duración total en segundos
        etiqueta         : str   — texto que acompaña el contador ("Trabajo", "Descanso", etc.)

    Pista para actualizar la misma línea:
        print(f"...", end="\r", flush=True)
        El \r mueve el cursor al inicio de la línea sin hacer salto.

    Pista para el loop:
        Itera desde segundos_totales hasta 0.
        En cada iteración: imprime, espera 1 segundo con time.sleep(1), resta 1.
        Al terminar imprime una línea vacía para limpiar el \r.
    """
    # TODO: tu código aquí
    while segundos_totales >0:
        print(f"{etiqueta}: {formatear_tiempo(segundos_totales)}", end="\r", flush=True)
        time.sleep(1)
        segundos_totales -=1
    print("Tiempo Cumplido")
    print()



def ejecutar_pomodoro(numero_ciclo):
    """
    Ejecuta un ciclo completo de Pomodoro:
        1. Cuenta regresiva de trabajo
        2. Mensaje de fin de trabajo
        3. Decidir si descanso corto o largo según numero_ciclo
        4. Cuenta regresiva de descanso
        5. Mensaje de fin de descanso

    Parámetro:
        numero_ciclo : int — número del ciclo actual (empieza en 1)
    """
    # TODO: 
    cuenta_regresiva(TIEMPO_TRABAJO, "TRABAJO")
    print("tiempo de trabajo finalizado")
    if numero_ciclo %4 == 0:
        cuenta_regresiva(TIEMPO_DESCANSO_LARGO, "DESCASO")
    else:
        cuenta_regresiva(TIEMPO_DESCANSO_CORTO, "DESCANSO")
    print("descanso finalizado, A TRABAJAAARRRR!!!")

def mostrar_bienvenida():
    """
    Imprime un encabezado con el nombre del programa y las instrucciones básicas.
    Solo texto, sin lógica.
    """
    # TODO: 
    print("-"*30)
    print("este es un metodo pomodoro, para ayudarte a enfocarte por periodos de 20 minutos")
    print("por cada 4 ciclos tendras 15 minutos de descanso")
    print("enfocate y aprovecha el tiempo")
    print("-"*30)

# ── PUNTO DE ENTRADA ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    mostrar_bienvenida()

    ciclo_actual = 1
    continuar = True

    while continuar:
        print(f"\n--- Pomodoro #{ciclo_actual} ---")
        ejecutar_pomodoro(ciclo_actual)
        ciclo_actual += 1

        # TODO: 
        respuesta = input("¿Quieres continuar con otro ciclo pomodoro ? (s/n): ")
        if respuesta.lower() != "s":
            continuar = False

    print("\nSesión terminada. Buen trabajo.")


   
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    """
Reloj Pomodoro — versión comentada
====================================
Esta es la versión de estudio. La versión limpia para portafolio
está en proyecto_portafolio/etapa1/pomodoro.py
"""

import time
# time es un módulo de la librería estándar de Python.
# Se usa time.sleep(n) para pausar la ejecución n segundos.
# No necesita instalación — viene incluido con Python.


# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────────
# Las constantes van arriba del todo, fuera de las funciones.
# Se escriben en MAYÚSCULAS por convención — indica que no deben cambiar
# durante la ejecución del programa.
# Multiplicar por 60 aquí hace el código más legible que poner 1500 directamente.

TIEMPO_TRABAJO = 25 * 60
TIEMPO_DESCANSO_CORTO = 5 * 60
TIEMPO_DESCANSO_LARGO = 15 * 60
CICLOS_PARA_DESCANSO_LARGO = 4
# Esta constante se usa en ejecutar_pomodoro con el operador %.
# Si cambias el número acá, el resto del programa se adapta solo.


# ── FUNCIONES ──────────────────────────────────────────────────────────────────

def formatear_tiempo(segundos_totales):
    """Convierte segundos a formato MM:SS. Ejemplo: 90 -> '01:30'"""

    # divmod(a, b) retorna una tupla (cociente, resto) — equivale a hacer
    # minutos = segundos_totales // 60
    # segundos = segundos_totales % 60
    # pero en una sola línea. Es más limpio cuando necesitas los dos valores.
    minutos, segundos = divmod(segundos_totales, 60)

    # :02d dentro del f-string rellena con ceros a la izquierda hasta 2 dígitos.
    # Ejemplo: 5 -> "05", 12 -> "12"
    # Sin esto el formato quedaría "1:5" en vez de "01:05".
    return f"{minutos:02d}:{segundos:02d}"


def cuenta_regresiva(segundos_totales, etiqueta):
    """Ejecuta una cuenta regresiva actualizando la misma línea en consola."""

    while segundos_totales > 0:
        # end="\r" reemplaza el salto de línea normal (\n) por un retorno de carro.
        # Esto mueve el cursor al inicio de la misma línea sin bajar.
        # El siguiente print sobreescribe lo anterior — así se ve el contador
        # actualizándose en el mismo lugar en vez de imprimir una línea nueva
        # por cada segundo.
        #
        # flush=True fuerza que Python muestre el texto inmediatamente.
        # Sin esto, Python podría guardar el texto en un buffer interno
        # y mostrarlo todo de golpe al final, arruinando el efecto del contador.
        print(f"{etiqueta}: {formatear_tiempo(segundos_totales)}", end="\r", flush=True)

        # time.sleep(1) pausa el programa 1 segundo real.
        # Va DESPUÉS del print porque el orden correcto es:
        # mostrar → esperar → restar
        # Si fuera antes: esperarías sin mostrar nada.
        # Si fuera después del -=1: el contador nunca mostraría el valor inicial.
        time.sleep(1)

        segundos_totales -= 1

    # print() vacío después del loop limpia la línea que quedó con \r.
    # Sin esto, el texto "Tiempo cumplido" podría quedar solapado
    # con el último valor del contador.
    print("Tiempo cumplido.")
    print()


def ejecutar_pomodoro(numero_ciclo):
    """Ejecuta un ciclo completo: trabajo + descanso corto o largo."""

    cuenta_regresiva(TIEMPO_TRABAJO, "Trabajo")
    print("Tiempo de trabajo finalizado.")

    # El operador % retorna el resto de la división.
    # numero_ciclo % 4 == 0 es True cuando numero_ciclo es múltiplo de 4.
    # Ejemplos: ciclo 4 -> 4%4=0 (descanso largo)
    #           ciclo 5 -> 5%4=1 (descanso corto)
    #           ciclo 8 -> 8%4=0 (descanso largo)
    #
    # Se usa la constante CICLOS_PARA_DESCANSO_LARGO en vez del número 4
    # para que si en el futuro cambias el valor, solo lo cambias arriba.
    if numero_ciclo % CICLOS_PARA_DESCANSO_LARGO == 0:
        cuenta_regresiva(TIEMPO_DESCANSO_LARGO, "Descanso largo")
    else:
        cuenta_regresiva(TIEMPO_DESCANSO_CORTO, "Descanso corto")

    print("Descanso finalizado. ¡A trabajar!")


def mostrar_bienvenida():
    """Muestra el encabezado del programa."""
    print("-" * 40)
    print("Método Pomodoro — enfócate por ciclos de 25 minutos.")
    print("Cada 4 ciclos tendrás 15 minutos de descanso.")
    print("Aprovecha el tiempo.")
    print("-" * 40)


# ── PUNTO DE ENTRADA ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    mostrar_bienvenida()

    ciclo_actual = 1
    continuar = True

    # El while controla si el usuario quiere seguir con otro ciclo.
    # ciclo_actual se incrementa después de cada pomodoro y se pasa
    # a ejecutar_pomodoro para que sepa si toca descanso largo o corto.
    while continuar:
        print(f"\n--- Pomodoro #{ciclo_actual} ---")
        ejecutar_pomodoro(ciclo_actual)
        ciclo_actual += 1

        # input() muestra el mensaje y espera que el usuario escriba algo.
        # .lower() convierte la respuesta a minúsculas para que "S" y "s"
        # funcionen igual.
        respuesta = input("¿Quieres continuar con otro ciclo? (s/n): ")
        if respuesta.lower() != "s":
            continuar = False

    print("\nSesión terminada. Buen trabajo.")