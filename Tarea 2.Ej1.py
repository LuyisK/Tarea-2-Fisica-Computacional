# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:40:45 2021

@author: valec
"""
import numpy as np

# Se tiene la EDO de primer orden: p'= f(y,p), que expresa la variación de la presión con respecto a la altura.
# Se crea la función F para obtener el valor de la función del lado derecho de la EDO.
def F(y,p):
    M = 28.9647/1000
    R = 8.314462
    g = 9.8
   # Se define la función f(y,p).
    valorF = (-200*M*p*g)/(58600*R-y*R)
    return valorF

#Se define la condición inicial de la presión para la altura a nivel del mar. 
y0 = 0
p0 = 101325

#Se crea la función que permite la ejecución del método de cálculo Runge Kutta Orden 4 que para así obtener los valores aproximados de la presión para cada valor de altura dentro del intervalo [0,3000]m cada 100m.
def RungeKutta_Orden4(f, y0, p0, n, y1):
    h = (y1-y0)/n
    p = [p0]
    y = np.linspace(y0,y1,n+1)
    for i in range(n):
        k1 = h*f(y[i],p[i])
        k2 = h*f(y[i]+h/2, p[i]+k1/2)
        k3 = h*f(y[i]+h/2, p[i]+k2/2)
        k4 = h*f(y[i]+h, p[i]+k3)
        presión = p[i] + (k1+2*k2+2*k3+k4)/6
        
        p.append(presión)
        
    return p
    
Solución_Aprox_RK4 = RungeKutta_Orden4(F,y0, p0, 30, 3000)
print ("Solución Aproximada RK4: \n", Solución_Aprox_RK4)



    
