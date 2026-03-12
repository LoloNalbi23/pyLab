"""8.  crearemos un programa que verifica si
un número ingresado por el usuario es positivo,
negativo o cero, y también si es un número par o impar."""

n = float(input("Ingrese el numero que quiere comprobar"))

if(n>0):
    print(f"{n} es positivo")
elif(n<0):
    print(f"{n} es negativo")
else:
    print(f"{n} es 0\ny no es ni par ni impar")

if(n%2==0):
    print(f"{n} es par")
else:
    print(f"{n} es impar")