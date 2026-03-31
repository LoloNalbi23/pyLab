"""Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
Muestra la lista de tareas agregadas.
Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.
"""

tareas = []
agregar = True
no_fin = True

class Tarea:
    def __init__(self):
        self.name = input("Nombre de la tarea: ")
        self.descripcion = input("Descripción de la tarea: ")
        self.dia = int(input("Introduzca día de vencimiento: "))
        self.mes = int(input("Introduzca mes de vencimiento: "))
        self.completada = False
    
    def completed(self):
        self.completada = True
        print("Tarea completada, felicitaciones!")
        tareas.remove(self)
        for i in tareas:
            i.show()
    
    def delete(self):
        tareas.remove(self)
        print("Tarea eliminada con éxito")
        for i in tareas:
            i.show()
    
    def show(self):
        print(f"Tarea: {self.name}\nDescripcion: {self.descripcion}\nFecha de vencimiento: {self.dia}/{self.mes}")

while agregar:
    resp = input("Quiere seguir agregando tareas? Si/No: ").lower()
    if resp == "si":
        tarea = Tarea()
        tareas.append(tarea)
    elif resp == "no":
        agregar = False
        for i in tareas:
            i.show()
    else:
        print("No escribió ni si ni no, vuelva a escribir")

while no_fin:
    print("Opciones:\n1 Marcar tarea como completada\n2 Eliminar tarea\n3 Eliminar lista de tareas\n4 Fin")
    accion = int(input("Qué desea hacer?"))
    if accion==1:
        name = input("Introduzca el nombre de la tarea a completar")
        for i in tareas:
            if name==i.name:
                i.completed()
    elif accion==2:
        name = input("Introduzca el nombre de la tarea a eliminar")
        for i in tareas:
            if name==i.name:
                i.delete()
    elif accion==3:
        tareas.clear
        print("Tareas eliminadas con éxito")
    elif accion==4:
        print("Suerte con sus tareas,tenga lindo día")
        no_fin = False