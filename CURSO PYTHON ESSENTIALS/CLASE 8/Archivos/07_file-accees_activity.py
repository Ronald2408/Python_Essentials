# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:24:22 2023

@author: USUARIO
"""


file= open("devices.txt","a")
while True:
    print("Ingrese nuevo dispositivo2: ")
    newItem = input(" ")
    if newItem == "exit":
        print("OK")
        break
    else:
       file.write(newItem + "\n" )  
file.close()   
print("All done")
    

    