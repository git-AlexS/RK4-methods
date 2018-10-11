import numpy as np
import matplotlib.pyplot as plt
import math as m
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3

timescale = float(input ("Timescale: ")) #try 0.01
maxt = 30
a = 10
b = 8/3
r = 28
initials = [4,5,6]

# FUNCTIONS

#f1 = a(y2-y1)
def f1(y1,y2,y3):
    x = a*(y2-y1)
    return x

#f2 = r*y1-y2-y1*y3
def f2(y1,y2,y3):
    x = r*y1-y2-y1*y3
    return x

#f3 = y1*y2-b*y3
def f3(y1,y2,y3):
    x = y1*y2-b*y3
    return x

flist = [f1,f2,f3]

## APPLYING RK4 ALGO

from rk4_fnc_pre import rk4_gen

(y, time) = rk4_gen(flist, initials, timescale, maxt)

## ANIMATION

fig = plt.figure(0)
ax = p3.Axes3D(fig)

speed = 8 #increases speed of playback by skipping values
trail_par = round((1/timescale)*0.1) # vary the length of the trail

def update(num, data, line, trail_line, speed, trail_par):
    line.set_data(data[:2, :speed*num])
    line.set_3d_properties(data[2, :speed*num])

    
    trail_line.set_data(data[:2,speed*num:(speed*num+trail_par)])
    trail_line.set_3d_properties(data[2,speed*num:(speed*num+trail_par)])
    
line, = ax.plot(y[0,0:1], y[1,0:1], y[2,0:1], lw = 0.5) #initial line values
trail_line, = ax.plot(y[0,0:1], y[1,0:1], y[2,0:1], lw = 1.5)

ax.set_xlim3d([round(min(y[0])-1), round(max(y[0])+1)])
ax.set_xlabel('X')

ax.set_ylim3d([round(min(y[1])-1), round(max(y[1])+1)])
ax.set_ylabel('Y')

ax.set_zlim3d([round(min(y[2])-1), round(max(y[2])+1)])
ax.set_zlabel('Z')
         
anim = animation.FuncAnimation(fig, update, fargs = (y, line,trail_line, speed, trail_par),
                               blit=False, interval = 10
                               ,save_count=m.ceil(len(y[0])/speed))

##anim.save('lorenz.mp4', fps = 30)

plt.show()


## PLOTS

y = y.tolist()

fig = plt.figure(1)
ax = fig.gca(projection='3d')

ax.plot(y[0], y[1], y[2], lw=0.5)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

fig = plt.figure(2)
ax1 = fig.gca(projection='3d')

ax1.plot(y[0], y[1], time, lw=0.5)

ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.set_zlabel("Time")
ax1.set_title("Lorenz Attractor")

plt.show()






