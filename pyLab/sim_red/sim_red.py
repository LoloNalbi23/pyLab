class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.conexiones = []
    
    def agregar_conexiones(self,nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} envía {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje,self.nombre)
    
    def recibir_mensaje(self,mensaje,emisor):
        print(f"{self.nombre} recibió de {emisor}:{mensaje}")

server = Nodo("servidor")
compu1 = Nodo("Compu1")
compu2 = Nodo("Compu2")
compu3 = Nodo("Compu3")

server.agregar_conexion(compu1)
server.agregar_conexion(compu2)
server.agregar_conexion(compu3)
compu1.agregar_conexion(server)
compu2.agregar_conexion(server)
compu3.agregar_conexion(server)