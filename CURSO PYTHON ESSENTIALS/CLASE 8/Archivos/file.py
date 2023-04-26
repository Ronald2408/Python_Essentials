# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:21:21 2023

@author: USUARIO
"""

lista = []
file = open("devices.txt","r")
for item in file:
    item = item.strip("Cisco")
    lista.append(item)
    print(item)
file.close()