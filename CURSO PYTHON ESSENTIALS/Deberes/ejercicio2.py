# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:13:33 2023

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

def dias_en_mes(anio, mes):
    """
    Devuelve el número de días en un mes y año dados.
    """
    # Verificar si el mes y el año son válidos
    if mes < 1 or mes > 12:
        return "Mes inválido"
    if anio < 1:
        return "Año inválido"

    # Lista de días en cada mes
    dias_por_mes = [31, 28 + es_bisiesto(anio), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Devolver el número de días en el mes dado
    return dias_por_mes[mes - 1]

dias_en_mes(2020, 4)