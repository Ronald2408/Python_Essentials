# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:26:18 2023

@author: USUARIO
"""


def crearlist(n):
    lista = []
    for item in range(1,n+1,1):
        lista.append(item)
    return lista

print(crearlist(10))