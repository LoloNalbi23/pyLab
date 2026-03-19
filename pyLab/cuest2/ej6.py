"""6. Escribe un programa que recorra una lista
de números y muestre si cada número es par o impar."""

lista = [1,4,7,2,6,1,9,3,6,10,178]

for i in lista:
    if i%2==0:
        print(f"{i} es par")
    elif i%2!=0:
        print(f"{i} es impar")