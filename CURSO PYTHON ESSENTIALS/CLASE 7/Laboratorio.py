# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:52:58 2023

@author: USUARIO
"""

def readint(prompt, min, max):
    while(True):
        
        try:
            print("Ingrese un numero entre",min,"y",max)
            x = int(input(prompt)) 
            assert x>= min and x <= max
            return x
       
        except ValueError:
            print("Error en el ingreso")
        except:
            print("Error, el valor debe estar dentro del rango")
            

v = readint("Ingrese un valor en el rango ", -100, 100)

print("The number is:", str(v))
