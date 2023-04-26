# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:10:15 2023

@author: USUARIO
"""

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f" HOla mi nombre es {self.nombre} y tengo {self.edad}")
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Mi nombre ha sido cambiado a {self.nombre}.")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False 
        
persona1 = persona("Juan",16)
persona2 = persona("Ronald",29)
persona3 = persona("Jessica",23)
persona4 = persona("Joss",27)