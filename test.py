import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dt = float(input ("Timescale: "))
a = 10
b = 8/3
r = 28
init = [4,5,6]

#f1 = a(y2-y1)
def f1(y1,y2):
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

time = [0]
i = 0
t = 0

y1 = [init[0]]
y2 = [init[1]]
y3 = [init[2]]

while t < 100:

    ky1_1 = f1(y1[i],y2[i])
    ky2_1 = f2(y1[i],y2[i],y3[i])
    ky3_1 = f3(y1[i],y2[i],y3[i])

    ky1_2 = f1(y1[i]+ky1_1*dt/2,y2[i]+ky2_1*dt/2)
    ky2_2 = f2(y1[i]+ky1_1*dt/2,y2[i]+ky2_1*dt/2,y3[i]+ky3_1*dt/2)
    ky3_2 = f3(y1[i]+ky1_1*dt/2,y2[i]+ky2_1*dt/2,y3[i]+ky3_1*dt/2)
    
    ky1_3 = f1(y1[i]+ky1_2*dt/2,y2[i]+ky2_2*dt/2)
    ky2_3 = f2(y1[i]+ky1_2*dt/2,y2[i]+ky2_2*dt/2,y3[i]+ky3_2*dt/2)
    ky3_3 = f3(y1[i]+ky1_2*dt/2,y2[i]+ky2_2*dt/2,y3[i]+ky3_2*dt/2)

    ky1_4 = f1(y1[i]+ky1_3*dt,y2[i]+ky2_3*dt)
    ky2_4 = f2(y1[i]+ky1_3*dt,y2[i]+ky2_3*dt,y3[i]+ky3_1*dt)
    ky3_4 = f3(y1[i]+ky1_3*dt,y2[i]+ky2_3*dt,y3[i]+ky3_1*dt)

    y1.append(y1[i]+(ky1_1+2*ky1_2+2*ky1_3+ky1_4)*dt/6)
    y2.append(y2[i]+(ky2_1+2*ky2_2+2*ky2_3+ky2_4)*dt/6)
    y3.append(y3[i]+(ky3_1+2*ky3_2+2*ky3_3+ky3_4)*dt/6)

    
    t = t + dt
    i = i+1
    time.append(t)

fig = plt.figure(100)
ax = fig.gca(projection='3d')

ax.plot(y1, y2, y3, lw=0.5)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

fig = plt.figure(200)
ax1 = fig.gca(projection='3d')

ax1.plot(y1, y2, time, lw=0.5)

ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.set_zlabel("Time")
ax1.set_title("Lorenz Attractor")

plt.show()

##plt.plot(time,y1)
##plt.xlabel('time (s)')
##plt.ylabel('voltage (mV)')
##plt.title('About as simple as it gets, folks')
##plt.grid(True)
##plt.show()
##
##plt.plot(y2,y1)
##plt.xlabel('y2')
##plt.ylabel('y1')
##plt.title('About as simple as it gets, folks')
##plt.grid(True)
##plt.show()
##
##plt.plot(y3,y1)
##plt.xlabel('y3')
##plt.ylabel('y1')
##plt.title('About as simple as it gets, folks')
##plt.grid(True)
##plt.show()
##
##plt.plot(y3,y2)
##plt.xlabel('y3')
##plt.ylabel('y2')
##plt.title('About as simple as it gets, folks')
##plt.grid(True)
##plt.show()





