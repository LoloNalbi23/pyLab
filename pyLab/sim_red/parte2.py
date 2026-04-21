"""Creación de una simulación de red de 3 computadoras y un servidor con una clase Nodo que crea los respectivos equipos y sus conexiones"""
"""permite enviar mensajes en la red , eliminar conexiones y por último, simular una desconexion y reconección automática"""

import time

class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre #Constructor
        self.conexiones = []
    
    def agregar_conexiones(self,nodo):
        self.conexiones.append(nodo) #Agrega conexión

    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} envía {mensaje}") #Muestra que envía mensaje
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje,self.nombre) #Envía mensaje
            time.sleep(1)
    
    def recibir_mensaje(self,mensaje,emisor):
        print(f"{self.nombre} recibió de {emisor}:{mensaje}") #Recibe mensaje
        self.conexión_dinámica(emisor)
    
    def eliminar_conexion(self,nodo):
        self.conexiones.remove(nodo) #Elimina conexión
    
    def conexión_dinámica(self,nodo):
        self.name.eliminar_conexión(nodo)
        time.sleep(1)
        print("Simulando desconexión y reconexión dinámica…") #Reconexión automática
        self.name.agregar_conexiones(nodo)
        print("¡Hola de nuevo a todos!")

server = Nodo("servidor")
compu1 = Nodo("Compu1")  #Creación de objetos
compu2 = Nodo("Compu2")
compu3 = Nodo("Compu3")

server.agregar_conexion(compu1)
server.agregar_conexion(compu2)
server.agregar_conexion(compu3) #Creación de conexiones
compu1.agregar_conexion(server)
compu2.agregar_conexion(server)
compu3.agregar_conexion(server)