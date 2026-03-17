"""5. Escribe un programa que compare dos números
y muestre si son iguales o no utilizando operadores
de comparación (por ejemplo, ==, !=)"""

n1 = int(input("Introduzca el primer numero"))
n2 = int(input("Introduzca el segundo numero"))

if(n1==n2):
    print(f"Los numeros {n1} y {n2} son iguales")
elif(n1!=n2):
    print(f"Los numeros {n1} y {n2} son distintos")