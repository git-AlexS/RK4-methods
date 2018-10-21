import numpy as np
import math as m
import random as rnd

def duffing_funcs(rand, t, timescale):

    g = 0.25
    w = 1
    F = 0.4
    d = 1

    #f1 = a(y2-y1)
    def f1(x,y,z):
        a = y
        return a

    #f2 = r*y1-y2-y1*y3
    def f2(x,y,z):
        a = -g*y+x-d*x**3 + F*(rand[t(z)]+m.cos(z))
        #a = -g*y+x-d*x**3 + F #(step)
        return a

    #f3 = y1*y2-b*y3
    def f3(x,y,z):
        a = w
        return a

    return [f1,f2,f3] 

def vanderpol_funcs():
    
    mu = 8.5
    F = 1.2
    w = 10

    #f1 = a(y2-y1)
    def f1(x,y,z):
        a = y
        return a

    #f2 = r*y1-y2-y1*y3
    def f2(x,y,z):
        a = mu*(1-x**2)*y - x + F*m.sin(z)
        #a = -g*y+x-d*x**3 + F #(step)
        return a

    #f3 = y1*y2-b*y3
    def f3(x,y,z):
        a = w
        return a

    return [f1,f2,f3]

def simple_damped_funcs(step_var, b,timescale):

    c = 0.1

    def f1(x,y,t):
        a = y
        return a

    def f2(x,y,t):
        a = -(c*x+b*y) +step_var[int(round(t/timescale))]
        return a

    def f3(x,y,t):
        a = 1
        return a


    return [f1,f2,f3]
