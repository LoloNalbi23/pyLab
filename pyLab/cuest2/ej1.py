"""1. Escribe un programa que identifique el color
de un objeto y muestre un mensaje según el color."""
preguntar = True
while preguntar:
    color = input(f"Ingrese el color del objeto: ").lower()

    if color == "rojo":
        print(f"El objeto es de color rojo")
        preguntar = False
    else:
        print(f"El objeto no es rojo")