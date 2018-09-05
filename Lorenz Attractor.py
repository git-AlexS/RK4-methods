import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

timescale = float(input ("Timescale: "))
maxt = 100
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

from rk4_fnc import rk4_gen

(y, time) = rk4_gen(flist, initials, timescale, maxt)

y = y.tolist()

print(y[0][0])

## ANIMATION

##fig = plt.figure(0)
##ax = fig.gca(projection='3d')
##line = ax.plot([], [], [], lw=2)
##
##
##def init():
##    line = ax.plot([], [], [], lw=2)
##    return line
##
##def animate(i):
##    line = ax.plot(y[0][i], y[1][i], y[2][i], lw=2)
##    return line
##
##anim = animation.FuncAnimation(fig, animate, init_func=init,
##                               frames=100, interval=20, blit=False)
##
##ax.relim()
##ax.autoscale_view(True,True,True)
##
##plt.show()

## PLOTS

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






