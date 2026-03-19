"""5 Escribe un programa que recorra una lista de 
frutas y muestre cada fruta."""
"""5.1 Agregar otras frutas a la lista."""
"""5.2 Escribe un programa verifique si una fruta 
específica está en una lista de frutas y muestra
un mensaje correspondiente."""

agregar = True
lista = ["sandia", "frutilla","durazno","arandano","ananá"]

while agregar:
    fruit = input(f"Coloque una fruta para agregar, escriba listo si ya terminó: ").lower()
    if fruit=="listo":
        agregar=False
    else:
        lista.append(fruit)

buscar = input(f"Que fruta quieres buscar? ").lower()
for i in lista:
    if i == buscar:
        print(f"{buscar} está en la lista de frutas")
    elif i==lista[-1]:
        print(f"{buscar} no esta en la lista de frutas")

for i in lista:
    print(i)