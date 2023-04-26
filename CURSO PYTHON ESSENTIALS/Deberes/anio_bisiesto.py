# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:53:32 2023

@author: USUARIO
"""

def es_bisiesto(anio):
   
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

es_bisiesto(2021)