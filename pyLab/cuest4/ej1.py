def agregar_tarea(tareas, tarea, fecha_limite, prioridad):
    nueva_tarea = {"Tarea": tarea, "Fecha límite": fecha_limite, "Prioridad": prioridad, "Completada":False}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def marcar_completada(tareas,n):
    for i,tarea in enumerate(tareas,1):
        if i == n:
            tareas[i-1]["Completada"] = True
            print("Tarea completada exitosamente.")

def mostrar_tareas(tareas,completadas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                if completadas==True:
                    if tareas[i-1]["Completada"]==True:
                        print(f"{clave}: {valor}")
                elif completadas==False:
                    if tareas[i-1]["Completada"]==False:
                        print(f"{clave}: {valor}")
                elif completadas==None:
                    print(f"{clave}: {valor}")


if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            completed = input("Quiere que se muestren las completadas? si/no/todas: ").lower()
            if completed == "si":
                mostrar_tareas(lista_tareas,True)
            elif completed == "no":
                mostrar_tareas(lista_tareas,False)
            elif completed == "todas":
                mostrar_tareas(lista_tareas,None)

        elif opcion == "3":
            number = int(input("Introduzca el indice de la tarea a eliminar: "))
            if number-1<=len(lista_tareas):
                marcar_completada(lista_tareas,number)
            else:
                print("Error, no existe ese número de tarea")
        
        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente nuevamente.")