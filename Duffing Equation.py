import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

n = int(input ("2pi/n, n = ...")) #try n = 50

damp = [0.05,0.25,0.8,2]
force = [0.4, 0.1, 0.2, 0.5]

g = 0.25
w = 1
F = 0.4
d = 1
initials = [0,0,0]

timescale = (2*m.pi)/(w*n)

maxt_unround = 3000
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
        a = -g*y+x-d*x**3 + F*m.cos(z)
        #a = -g*y+x-d*x**3 + F #(step)
        return a

    #f3 = y1*y2-b*y3
    def f3(x,y,z):
        a = w

        return a

    flist = [f1,f2,f3]

    ## APPLYING RK4 ALGO

    from rk4_fnc import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    y = y.tolist()

    ## PLOTS
    
    fig = plt.figure(i)
    plt.plot(y[2],y[0], lw=0.5)

    plt.xlabel("Time")
    plt.ylabel("X axis")
    
    fig=plt.figure(i + 1)
    plt.plot(y[1],y[0], lw=0.5)

    plt.xlabel("Velocity")
    plt.ylabel("X axis")

    ## POINCARE
    
    p_maps_pos = []
    p_maps_vel = []
    
    for l in range(0,cycles):
        p_maps_pos.append(y[0][l*n])
        p_maps_vel.append(y[1][l*n])

    fig=plt.figure(i + 2)
    plt.plot(p_maps_vel,p_maps_pos,'.')
    
    plt.xlabel("Velocity")
    plt.ylabel("X axis")


##fig = plt.figure(1)
##ax = fig.gca(projection='3d')
##
##ax.plot(y[0], y[1], y[2], lw=0.5)
##
##ax.set_xlabel("X Axis")
##ax.set_ylabel("Y Axis")
##ax.set_zlabel("Z Axis")
##ax.set_title("Lorenz Attractor")
##
##fig = plt.figure(2)
##ax1 = fig.gca(projection='3d')
##
##ax1.plot(y[0], y[1], time, lw=0.5)
##
##ax1.set_xlabel("X Axis")
##ax1.set_ylabel("Y Axis")
##ax1.set_zlabel("Time")
##ax1.set_title("Lorenz Attractor")

plt.show()
