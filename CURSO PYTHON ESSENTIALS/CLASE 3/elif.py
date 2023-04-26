# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:24:17 2023

@author: USUARIO
"""

acl = int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("LA ACL es estandar")
elif acl>=100 and acl<=199:
    print("LA ACL es extendida")
else:
    print("No es ACL")