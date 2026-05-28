"""Crear 3 clases: “Mago” , “Guerrero” y “Elfo”

La clase “Mago”, debe tener un método llamado “hechizos”
la clase “Guerrero” debe tener un método llamado “defensa”
la clase “Elfo” debe tener una método llamado “aura”.

Luego crear una clase llamada “DarkLord” que herede de “Guerrero “ y “Elfo”, en ese orden y por lo tanto puede usar “defensa” y “aura”, además de los hechizos.

por último cambiar el orden de las herencias de la clase “DarkLord” y observa cómo se va modificando el orden del MRO.
"""

class Mago:
    def __init__(self):
        pass
    
    def hechizo(self):
        print("Use hechizo")

class Guerrero:
    def __init__(self):
        pass
    
    def defensa(self):
        print("Use defensa")

class Elfo:
    def __init__(self):
        pass
    
    def aura(self):
        print("Use aura")

class DarkLorda(Guerrero,Elfo):
    def __init__(self):
        super().__init__()
        pass

class DarkLordb(Elfo,Guerrero):
    def __init__(self):
        super().__init__()
        pass

print(DarkLorda.mro())
print(DarkLordb.mro())