"""3. Escribe un programa que realice operaciones
aritméticas simples, como suma, resta, 
multiplicación y división, utilizando 
números enteros y flotantes."""

num1 = float(input('Introduzca un numero: '))
num2 = float(input('Introduzca otro numero: '))
print(f"1 para suma\n2 para resta\n3 para multiplicacion\n4 para division")
opr = int(input(f"Que operacion desea realizar? "))

if(opr==1):
    print(f"La suma es igual a {num1 + num2}")
elif(opr==2):
    print(f"La suma es igual a {num1 - num2}")
elif(opr==3):
    print(f"La suma es igual a {num1 * num2}")
elif(opr==4):
    print(f"La suma es igual a {num1 / num2}")