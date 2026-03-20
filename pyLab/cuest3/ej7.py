"""Integrador: Crear programa que permita
al usuario agregar tareas con descripción, 
fecha límite y prioridad, así como mostrar 
la lista de tareas. 
Este menú se repite hasta que el usuario elige salir."""
salir=True
tasks = []

while salir:
    name = input("Nombre de la tarea: ")
    desc = input("Descripcion de la tarea: ")
    dia = int(input("Dia de vencimiento: "))
    mes = int(input("Mes de vencimiento: "))
    prioridad = input("Urgente, Importante o normal? ")
    task = [name,desc,dia,mes,prioridad]
    tasks.append(task)
    s = input("Salir o seguir? ").lower()
    if s == "salir":
        salir = False

for task in tasks:
    print(f"Prioridad: {task[4]}\nNombre: {task[0]}\nDescripcion: {task[1]}\nFecha de vencimiento: {dia}/{mes}")