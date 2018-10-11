import numpy as np
import math as m
import random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import integration_functions as fncs

n = int(input ("2pi/n, n = ...")) #try n = 50

g = 0.25
w = 1
F = 0.4
d = 1
initials = [0,0,0]

timescale = (2*m.pi)/(w*n)

maxt_unround = 300
cycles = m.ceil(maxt_unround/(2*m.pi))
maxt = cycles*2*m.pi

length = int(round((maxt/timescale)+1)) #slightly hacky, including 0th element

def t(x):
    return int(round(x / (w*timescale)))

for p in range(1,2):

    noise_rate = 50
    noiseA = [0,2.5]
    (rand) = fncs.noise(length, timescale, noise_rate, noiseA[p])

    # FUNCTIONS

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

    flist = [f1,f2,f3]

    ## APPLYING RK4 ALGO

    from rk4_fnc_pre import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    yA = y
    y = y.tolist()
    
    ## PLOTS
    
    fncs.plot_2d(y[2], y[0], 'Time', 'Position', str(p)+ '.0',lw = 0.5)
    fncs.plot_2d(y[0], y[1], 'Position', 'Velocity', str(p)+ '.1',lw = 0.5)
    
    ## POINCARE
    
    (p_maps_pos,p_maps_vel) = fncs.poincare_map(y[0],y[1],n,cycles)
    
    fncs.plot_2d(p_maps_pos, p_maps_vel,
                 'Position', 'Velocity', str(p)+ '.1',
                 linestyle = 'none', marker = '.')


    ## EMBEDDED DIMENSION

    start = 5
    length = len(y[0])
    
    position_add1 = fncs.embed_dim(y[0],length,start)
    fncs.plot_2d(position_add1,y[0],
                                'Position + ' + str(start), 'Position',
                                str(p)+ '.3', lw = 0.5)
    
    (p_maps_pos2,p_maps_vel2) = fncs.poincare_map(position_add1,y[0],n,cycles)
    
    fncs.plot_2d(p_maps_pos2, p_maps_vel2,
                 'Position + ' + str(start), 'Position', str(p)+ '.3',
                 linestyle = 'none', marker = '.')

    ## ANIMATION
    
    fig_ani = plt.figure(str(p)+ '.2')
    ax1 = plt.gca()
    
    speed = 6 #increases speed of playback by skipping values
    trail_par = round((1/timescale)*0.3) # vary the length of the trail

    def update(num, data, line, trail_line, speed, trail_par):
        line.set_data(data[:2, :speed*num])
        trail_line.set_data(data[:2,speed*num:(speed*num+trail_par)])

    line, = ax1.plot(yA[0,0:1], yA[1,0:1], lw = 0.5)
    trail_line, = ax1.plot(yA[0,0:1], yA[1,0:1], lw = 1.5)
    
    ax1.set_xlim([min(y[0])-0.2, max(y[0])+0.2])
    ax1.set_xlabel('X')

    ax1.set_ylim([min(y[1])-0.2, max(y[1])+0.2])
    ax1.set_ylabel('Y')

    anim = animation.FuncAnimation(fig_ani, update,
                                   fargs = (yA, line,trail_line, speed, trail_par),
                                   blit=False, interval = 10,
                                   save_count=m.ceil(len(y[0])/speed))
    #anim.save('duffing_noise.mp4', fps = 30)
    
plt.show()

