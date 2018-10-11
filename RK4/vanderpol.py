import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import integration_functions as fncs

n = int(input ("2pi/n, n = ...")) #try n = 50

mu = 8.5
F = 1.2
w = 10

initials = [1,0,0]

timescale = (2*m.pi)/(w*n)

maxt_unround = 40
cycles = m.ceil(maxt_unround/(2*m.pi))
maxt = cycles*2*m.pi

for i in range(0,1):


    # FUNCTIONS

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

    flist = [f1,f2,f3]

    ## APPLYING RK4 ALGO

    from rk4_fnc_pre import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    y = y.tolist()

    ## PLOTS

    fncs.plot_2d(y[2], y[0], 'Time', 'Position', str(i)+ '.0',lw = 0.5)
    fncs.plot_2d(y[1], y[0], 'Velocity', 'Position', str(i)+ '.1',lw = 0.5)

    ## EMBEDDED DIMENSION

    start = 5
    length = len(y[0])
    
    position_add1 = fncs.embed_dim(y[0],length,start)
    fncs.plot_2d(position_add1,y[0],
                                'Position + ' + str(start), 'Position',
                                str(i)+ '.2', lw = 0.5)

plt.show()
