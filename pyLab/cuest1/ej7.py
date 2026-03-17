"""7. crear un programa que le pida al usuario
nombre, edad y ciudad de residencia, realizar
cálculos basados en la edad, y luego mostrará
la información en pantalla 
(# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5).
"""
name = input("Coloque su nombre")
edad= int(input("Coloque su edad"))
city = input("Coloque su ciudad")

año = 2026 - edad
print(f"Hola {name}\n tiene {edad} años \n y vive en {city}")
if(edad>=18):
    print(f"es mayor de edad")
if(edad%5==0):
    print(f"Es multiplo de 5")