"""4. Crear una lista de frutas y mostrar en consola
algunas frutas de la lista, también por rebanadas."""

lista = ["Sandía","Melón","Frutilla","Durazno","Manzana","Arandano","Naranja"]

for i,fruta in enumerate(lista):
    print(fruta)
    print(fruta[0:3])
    print(fruta[3:])