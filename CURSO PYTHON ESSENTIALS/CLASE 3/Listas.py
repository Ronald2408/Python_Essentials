# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:15:17 2023

@author: USUARIO
"""

lista = [1,5.3,"Ronald",True]
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[0])
print(lista[-1])


tupla = (1,5.3,"Ronald",True)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])

"""
No funcionara si pongo asi 
print(lista[5])  o
print(lista[-4])

xq no estan en el rango del indice
"""

lista[3]="Jessica"
print(lista)
del lista[3]
print(lista)

print(len(lista))