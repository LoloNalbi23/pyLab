"""1 Define una lista de diccionarios que 
represente información personal.
nombre,edad. Luego, accede a
elementos específicos de la lista, 
como el primer diccionario, el nombre 
de la primera persona y la edad de la 
segunda persona, para finalmente imprimir
los resultados en la consola."""

"""1.2. Del punto 1, recorrer y mostrar k,v"""

#1
lista = [{'name':"Lolo",'edad':17},
         {'name':"Mateo",'edad':17},
         {'name':"Samu",'edad':16},
         {'name':"Misa",'edad':16},
         {'name':"Jesús",'edad':2026}]

print(lista)

#2
print(f"La primera persona se llama {lista[0]['name']}")
print(f"La segunda persona tiene {lista[1]['edad']} años")
print(f"La tercera persona se llama {lista[2]['name']}")
print(f"La ultima persona se llama {lista[-1]['name']} y tiene {lista[-1]['edad']}")

for k in lista:
    for v in k:
        print(f"k es {k} y v es {v}")