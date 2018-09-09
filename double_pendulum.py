import numpy as np
import math as m
import random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import integration_functions as fncs

n = int(input ("2pi/n, n = ...")) #try n = 50

g = 9.81
w = 1
F = 0.4
d = 1
initials = [m.pi,m.pi,0.5,0]

timescale = (2*m.pi)/(w*n)

maxt_unround = 100
cycles = m.ceil(maxt_unround/(2*m.pi))
maxt = cycles*2*m.pi

length = int(round((maxt/timescale)+1)) #slightly hacky, including 0th element

for p in range(0,1):

    noise_rate = 50
    noiseA = [0,2.5]
    (rand) = fncs.noise(length, timescale, noise_rate, noiseA[p])

    # FUNCTIONS

    def f1(th1,th2,p1,p2):
        a = 6*(2*p1-3*m.cos(th1-th2)*p2)/(16-9*(m.cos(th1-th2))**2)
        return a

    def f2(th1,th2,p1,p2):
        a = 6*(8*p2-3*m.cos(th1-th2)*p1)/(16-9*(m.cos(th1-th2))**2)
        return a

    def f3(th1,th2,p1,p2):
        a = (-1/2)*(f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*m.sin(th1-th2)+3*g*m.sin(th1))
        return a

    def f4(th1,th2,p1,p2):
        a = (-1/2)*(-1*f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*m.sin(th1-th2)+g*m.sin(th2))
        return a
    flist = [f1,f2,f3,f4]

    ## APPLYING RK4 ALGO

    from rk4_fnc import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    y = y.tolist()

    ## CONVERT ANGLES TO POSITION

    length = len(y[0])
    

    pos1 = fncs.zerolistmaker(length)
    pos2 = fncs.zerolistmaker(length)
    
    for i in range(0,length):
        pos1[i] = m.sin(y[0][i])
        pos2[i] = m.sin(y[0][i])+ m.sin(y[1][i])
   
    ## PLOTS

    fncs.plot_2d(pos1, y[2], 'Position 1', 'Velocity 1', str(p)+ '.1',lw = 0.5)
    fncs.plot_2d(pos2, y[3], 'Position 2', 'Velocity 2', str(p)+ '.2',lw = 0.5)
    fncs.plot_2d(time, pos1, 'Time', 'Position 1', str(p)+ '.3',lw = 0.5)
    fncs.plot_2d(time, pos2, 'Time', 'Position 2', str(p)+ '.3',lw = 0.5)
    fncs.plot_2d(time, y[2], 'Time', 'Velocity 1', str(p)+ '.4',lw = 0.5)
    fncs.plot_2d(time, y[3], 'Time', 'Velocity 2', str(p)+ '.4',lw = 0.5)
    
##    ## POINCARE
##    
##    (p_maps_pos,p_maps_vel) = fncs.poincare_map(y[0],y[1],n,cycles)
##    
##    fncs.plot_2d(p_maps_pos, p_maps_vel,
##                 'Position', 'Velocity', str(p)+ '.1',
##                 linestyle = 'none', marker = '.')
##
##
##    ## EMBEDDED DIMENSION
##
##    start = 5
##    length = len(y[0])
##    
##    position_add1 = fncs.embed_dim(y[0],length,start)
##    fncs.plot_2d(position_add1,y[0],
##                                'Position + ' + str(start), 'Position',
##                                str(p)+ '.3', lw = 0.5)
##    
##    (p_maps_pos,p_maps_vel) = fncs.poincare_map(position_add1,y[0],n,cycles)
##    
##    fncs.plot_2d(p_maps_pos, p_maps_vel,
##                 'Position + ' + str(start), 'Position', str(p)+ '.3',
##                 linestyle = 'none', marker = '.')
    
##
plt.show()

