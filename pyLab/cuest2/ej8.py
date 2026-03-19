"""8. Integrador:
Escribe un programa que permita a un usuario crear
una lista de nombres. El programa continuará pidiendo
nombres hasta que el usuario ingrese "fin". Luego, 
el programa mostrará la lista de nombres en orden alfabético,
indicará cuántos nombres empiezan con la letra 'A' o 'E', 
y mostrará si un nombre específico está en la lista."""

sigue = True
counta = 0
counte = 0
lista = []

while sigue:
    name = input(f"Introduzca un nombre, fin si no quiere agregar más: ").lower()
    if name=="fin":
        sigue = False
    else:
        lista.append(name)

lista.sort()
print(lista)

for i in lista:
    if i.startswith('a'):
        counta+=1
    elif i.startswith('e'):
        counte+=1

print(f"{counta} son las cantidad de palabras que empiezan con a")
print(f"{counte} son las cantidad de palabras que empiezan con e")

buscar = input(f"Que nombre quiere buscar en la lista de nombres? ")
for index,nombre in enumerate(lista):
    if nombre==buscar:
        print(f"{buscar} esta en la lista, en la posicion {index+1}")