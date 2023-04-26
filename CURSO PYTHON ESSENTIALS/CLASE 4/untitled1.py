# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:33:10 2023

@author: USUARIO
"""

while True:
    x = input("Ingrese u numero a contar: ")
    if x == 10 or x == 5:
        break
    
    x = int(x)
    y = 1
    while True:
        print (y)
        y = y+1
        if y>x:
            break