"""Creación de una simulación de red de 3 computadoras y un servidor con una clase Nodo que crea los respectivos equipos y sus conexiones
permimte enviar mensajes en la red"""

class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre  #Contructor
        self.conexiones = []
    
    def agregar_conexiones(self,nodo):
        self.conexiones.append(nodo) #Agrega conexion

    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} envía {mensaje}") #Muestra que envía mensaje
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje,self.nombre) #Envía mensaje
    
    def recibir_mensaje(self,mensaje,emisor):
        print(f"{self.nombre} recibió de {emisor}:{mensaje}") #Recibe mensaje
    

server = Nodo("servidor")
compu1 = Nodo("Compu1") #Creación de objetos
compu2 = Nodo("Compu2")
compu3 = Nodo("Compu3")

server.agregar_conexion(compu1)
server.agregar_conexion(compu2)
server.agregar_conexion(compu3) #Creación de conexiones
compu1.agregar_conexion(server)
compu2.agregar_conexion(server)
compu3.agregar_conexion(server)