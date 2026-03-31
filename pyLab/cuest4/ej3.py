n = int(input("Introduzca la cantidad de numeros de Fibonacci quiere mostrar: "))

fibonacci = [0,1]

for i in range(2,n):
    j = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(j)

print(fibonacci)