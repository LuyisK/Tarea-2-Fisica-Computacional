# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:42:40 2021

@author: valec
"""
import numpy as np

#Se declara la función que permite calcular la presión de forma teórica. 
def Presión_Teórica(y):
     M = 28.9647/1000
     R = 8.314462
     g = 9.8
     presión = (1.45225e-12)*(293-y/200)**(200*M*g/R)
     return presión
 
#Se crea la función que permite obtener el arreglo de presiones teóricas para cada altura del intervalo. 
def Arreglo_Presión_Teo(y0,y1,n):
    p = [101325]
    y = np.linspace(y0,y1,n)
    for i in range(n):
        pi=Presión_Teórica(y[i])
        p.append(pi)
        
    return p

print("Solución Teórica: \n",Arreglo_Presión_Teo(0, 3000, 30))