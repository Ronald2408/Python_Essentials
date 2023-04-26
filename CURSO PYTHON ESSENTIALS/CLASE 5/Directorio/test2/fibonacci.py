# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:40:13 2023

@author: USUARIO
"""

def fibonacci(n):
    a, b = 0,1
    while a<= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a,b = b, a+b
    print()
