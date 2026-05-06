"""Crear un programa donde:
Crear una clase: Alumno
crear sus atributos: Nombre, Apellido, Edad y Curso
crearle un método: programar (), que imprima  “ el alumno (nombre) está programando”

Crear el objeto Alumno instanciando con el método programar()

Los datos solicitados que el alumno completará, tiene que ser indistinto si es en mayuscula o minuscula
"""

class Alumno:
    def __init__(self,nombre,apellido,edad,curso,division):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
        self.division = division
    
    def programar(self):
        print(f"El alumno {self.nombre} está programando")

Alumno("Lorenzo","Nalbandian",17,6,"P").programar()