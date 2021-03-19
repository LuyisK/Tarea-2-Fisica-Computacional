# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:51:14 2021

@author: valec
"""
import scipy.integrate as spint
import numpy as np

def F(y,p):
    M = 28.9647/1000
    R = 8.314462
    g = 9.8
   # Se define la función f(y,p).
    valorF = (-200*M*p*g)/(58600*R-y*R)
    return valorF

#Se crea una función que permite ejecutar el método RK45. 
def RungeKutta45(yi, yf, n, pi):
    p0 = [pi]
    #Se definen los parámetros para la función solve_ivp. 
    fun = F
    t_span = (yi,yf)
    y0 = p0
    method = 'RK45'
    t_eval = np.linspace(yi, yf, n+1)
    Solución_Aprox_RK45 = spint.solve_ivp(fun, t_span, y0, method, t_eval)
    print ("Altura (y): \n",Solución_Aprox_RK45.t)
    print("Solución Aproximada RK45, Presión (p): \n",Solución_Aprox_RK45.y)
    
#Se llama a la función RungeKutta45 para obtener la aproximación deseada. 
RungeKutta45(0, 3000, 30)

