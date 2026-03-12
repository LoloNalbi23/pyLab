"""6. Escribe un programa que utilice operadores
de asignación para realizar operaciones como 
incrementar o decrementar el valor de una variable."""

n1 = int(input("Introduzca el numero principal"))
n2 = int(input("Cuanto se va a cambiar el numero? "))

n1+=n2
print(f"El numero incrementado es {n1}")

n1+=2*n2
print(f"El numero decrementado es {n1}")
