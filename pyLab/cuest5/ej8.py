"""Solicita al usuario que ingrese la longitud deseada para la contraseña.
Genera una contraseña aleatoria con la longitud especificada.
Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
Muestra la contraseña generada al usuario."""

import random
import string
"""
string.ascii_uppercase (mayusculas)
string.ascii_lowercase (minusculas)
string.digits          (numeros)
string.punctuation     (especiales)
"""
def generar(l):
    mezcla = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    a = "".join(random.choices(mezcla,k=l))
    b = "".join(random.sample(mezcla,k=l))
    print(a)
    print(b)

longitud = int(input("Cuanto quiere que tenga de largo la contraseña? "))
generar(longitud)
