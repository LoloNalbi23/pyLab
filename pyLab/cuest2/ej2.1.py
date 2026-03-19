"""2.1. Escribe un programa que solicita al usuario
que ingrese números enteros positivos y muestre
la suma de esos números. La entrada de números
continuará hasta que el usuario ingrese un 
número negativo, momento en el que el programa 
mostrará la suma total."""
sigue = True
cont = 0
while sigue:
    n = int(input("Ingrese un numero entero"))
    if n>=0:
        cont+=n
    else:
        sigue = False
        print(f"La suma es {cont}")