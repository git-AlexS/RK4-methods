import numpy as np
import math as m
import random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import integration_functions as fncs

n = int(input ("2pi/n, n = ...")) #try n = 50

K = 5
r = [1.1, 2, 3]

initials = [0.05]

timescale = (2*m.pi)/(n)

maxt_unround = 50
cycles = m.ceil(maxt_unround/(2*m.pi))
maxt = cycles*2*m.pi

length = int(round((maxt/timescale)+1)) #slightly hacky, including 0th element

def t(x):
    return int(round(x / (w*timescale)))

for p in range(0,3):

    # FUNCTIONS

    #f1 = a(y2-y1)
    def f1(x):
        a = r[p]*x*(1-x/K)
        return a



    flist = [f1]

    ## APPLYING RK4 ALGO

    from rk4_fnc_pre import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    y = y.tolist()
    
    ## PLOTS
    
    fncs.plot_2d(time, y[0], 'Time', 'Position', str(p)+ '.0',lw = 0.5)
    
    ## POINCARE
    
##    (p_maps_pos,p_maps_vel) = fncs.poincare_map(y[0],y[1],n,cycles)
##    
##    fncs.plot_2d(p_maps_pos, p_maps_vel,
##                 'Position', 'Velocity', str(p)+ '.1',
##                 linestyle = 'none', marker = '.')
##

    ## EMBEDDED DIMENSION

##    start = 5
##    length = len(y[0])
##    
##    position_add1 = fncs.embed_dim(y[0],length,start)
##    fncs.plot_2d(position_add1,y[0],
##                                'Position + ' + str(start), 'Position',
##                                str(p)+ '.3', lw = 0.5)
##    
##    (p_maps_pos2,p_maps_vel2) = fncs.poincare_map(position_add1,y[0],n,cycles)
##    
##    fncs.plot_2d(p_maps_pos2, p_maps_vel2,
##                 'Position + ' + str(start), 'Position', str(p)+ '.3',
##                 linestyle = 'none', marker = '.')
##
plt.show()

