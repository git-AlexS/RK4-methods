import numpy as np
import math as m
from math import sin
from math import cos
from math import pi
import matplotlib.pyplot as plt
import integration_functions as fncs
import matplotlib.animation as animation
from timeit import default_timer as timer

n = int(input ("2pi/n, n = ...")) #try n = 1200

g = 9.81

initials = [pi,pi,0.3,0] #theta of first mass, theta of second mass 
                             #,ang momentum of first mass, "  " second mass

timescale = (2*pi)/(n)

maxt = 50
start = fncs.zerolistmaker(1)
end = fncs.zerolistmaker(1)
timed = fncs.zerolistmaker(1)

for p in range(0,1):

    start[p] = timer()
    # FUNCTIONS

    def f1(th1,th2,p1,p2):
        a = 6*(2*p1-3*cos(th1-th2)*p2)/(16-9*(cos(th1-th2))**2)
        return a

    def f2(th1,th2,p1,p2):
        a = 6*(8*p2-3*cos(th1-th2)*p1)/(16-9*(cos(th1-th2))**2)
        return a

    def f3(th1,th2,p1,p2):
        a = (-1/2)*(f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*sin(th1-th2)+3*g*sin(th1))
        return a

    def f4(th1,th2,p1,p2):
        a = (-1/2)*(-1*f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*sin(th1-th2)+g*sin(th2))
        return a
    flist = [f1,f2,f3,f4]

    ## APPLYING RK4 ALGO

    from rk4_fnc_pre import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    nparray = y

    y = y.tolist()
    

    ## CONVERT ANGLES TO POSITION

    length = len(y[0])

    xpos1 = fncs.zerolistmaker(length)
    xpos2 = fncs.zerolistmaker(length)
    ypos1 = fncs.zerolistmaker(length)
    ypos2 = fncs.zerolistmaker(length)
    
    for i in range(0,length):
        xpos1[i] = m.sin(y[0][i])
        xpos2[i] = m.sin(y[0][i])+ m.sin(y[1][i])
        ypos1[i] = -m.cos(y[0][i])
        ypos2[i] = -m.cos(y[0][i]) -m.cos(y[1][i])
        
    # Poincare section when bob goes from -ve to +ve

    filtered_array = fncs.bools_spatial_1var(xpos2, 0, 1)
    poincare_array = nparray[:,filtered_array]

    fncs.plot_2d(poincare_array[0], poincare_array[2], 'Position 1', 'Velocity 1', str(p)+ '.1',
                 linestyle = 'none', marker = '.')
    ## PLOTS

##    fncs.plot_2d(xpos1, y[2], 'Position 1', 'Velocity 1', str(p)+ '.1',lw = 0.5)
##    fncs.plot_2d(xpos2, y[3], 'Position 2', 'Velocity 2', str(p)+ '.2',lw = 0.5)
##    fncs.plot_2d(time, xpos1, 'Time', 'Position 1', str(p)+ '.3',lw = 0.5)
##    fncs.plot_2d(time, xpos2, 'Time', 'Position 2', str(p)+ '.3',lw = 0.5)
##    fncs.plot_2d(time, y[2], 'Time', 'Velocity 1', str(p)+ '.4',lw = 0.5)
##    fncs.plot_2d(time, y[3], 'Time', 'Velocity 2', str(p)+ '.4',lw = 0.5)
    fncs.plot_2d(time, y[1], 'Time', 'Angle 2', str(p)+ '.5',lw = 0.5)
    fncs.plot_2d(time, y[0], 'Time', 'Angle 1', str(p)+ '.6',lw = 0.5)

### ANIMATION 

    
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(timescale, 0.9, '', transform=ax.transAxes)

def init():                #just draws a clear frame at start
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    currentx = [0, xpos1[3*i], xpos2[3*i]]
    currenty = [0, ypos1[3*i], ypos2[3*i]]

    line.set_data(currentx, currenty)
    time_text.set_text(time_template % (3*i*timescale))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, m.ceil(len(y[0])/3)),
                              interval=timescale*3300, blit=True, init_func=init)
##
### ani.save('double_pendulum.mp4', fps=15)
##

plt.show()



