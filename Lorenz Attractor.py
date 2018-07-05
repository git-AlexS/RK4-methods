import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

timescale = float(input ("Timescale: "))
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

(y, time) = rk4_gen(flist, initials, timescale)

y = y.tolist()

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






