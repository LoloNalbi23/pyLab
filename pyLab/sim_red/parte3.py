"""Una vez que tenemos el código de la simulación de red básico con el agregado de la parte 2 (reconexión dinámica)  vamos a agregar 
un buffer para simular la congestión del nodo.

Agregar un método: procesar_buffer, Su función es procesar los mensajes que se encuentran almacenados en el buffer del nodo.
Se utiliza la biblioteca random para simular eventos de pérdida de paquetes en la comunicación entre nodos. El módulo random en 
Python proporciona funciones para generar números aleatorios, lo cual se utiliza aquí para simular comportamientos aleatorios en la 
red, específicamente la pérdida de paquetes. debemos Importar “randon”

También utilizaremos el pop(), que se usa para eliminar y devolver un elemento de una lista. Cuando se le pasa un argumento, pop(index)
, eliminará y devolverá el elemento en la posición de índice especificada.  

Una vez agregados los elementos tendrá como resultado, información sobre el proceso de comunicación, incluida la recepción de mensajes,
la congestión del buffer y la pérdida de paquetes.
"""

import time
import random
"""pop(index), eliminará y devolverá el elemento"""
class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre #Constructor
        self.conexiones = []
        self.buffer = []
    
    def agregar_conexiones(self,nodo):
        self.conexiones.append(nodo) #Agrega conexión

    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} envía {mensaje}") #Muestra que envía mensaje
        for i,nodo in enumerate(self.conexiones):
            self.procesar_buffer(mensaje,nodo)#Envía mensaje a buffer
            time.sleep(1)
    
    def recibir_mensaje(self,mensaje,emisor):
        print(f"{self.nombre} recibió de {emisor}:{mensaje}") #Recibe mensaje
        self.conexión_dinamica(emisor)
    
    def eliminar_conexion(self,nodo):
        self.conexiones.remove(nodo) #Elimina conexión
    
    def conexión_dinamica(self,nodo):
        if nodo in self.conexiones:
            self.eliminar_conexion(nodo)
            time.sleep(1)
            print("Simulando desconexión y reconexión dinámica…") #Reconexión automática
            self.agregar_conexiones(nodo)
            print("¡Hola de nuevo a todos!")
    
    def procesar_buffer(self,mensaje,nodo,prob_perdida=0.3):
        if random.random() > prob_perdida: #probabilidad de perder mensaje
            self.buffer.append(mensaje)
            self.buffer.pop(-1)
            nodo.recibir_mensaje(mensaje,self.nombre) #recibe el mensaje cada nodo
        else:
            print(f"{nodo.nombre} perdió el mensaje") #Se pierde el mensaje

server = Nodo("servidor")
compu1 = Nodo("compu1")  #Creación de objetos
compu2 = Nodo("compu2")
compu3 = Nodo("compu3")

server.agregar_conexiones(compu1)
server.agregar_conexiones(compu2)
server.agregar_conexiones(compu3) #Creación de conexiones
compu1.agregar_conexiones(server)
compu2.agregar_conexiones(server)
compu3.agregar_conexiones(server)

server.enviar_mensaje("Hola a todos")