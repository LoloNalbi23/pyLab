"""Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
Muestra el número de intentos necesarios para adivinar.
"""
import random
numero = random.randint(1, 100)
no_adivino = True

while no_adivino:
    n = int(input("Introduzca el numero que piensa que es: "))
    if n>numero:
        print("Incorrecto, el numero es menor")
    elif n<numero:
        print("Incorrecto, el numero es mayor")
    elif n==numero:
        print("Correcto, ganaste")
        no_adivino = False