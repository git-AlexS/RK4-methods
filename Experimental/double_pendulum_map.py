import numpy as np
import math as m
import matplotlib.pyplot as plt
import integration_functions as fncs
import matplotlib.animation as animation

n = 1200 #int(input ("2pi/n, n = ...")) #try n = 1200

g = 9.81


## for circular poincare map, use [0.2,-0.2828,0,0]

initials = [m.pi-.1,m.pi-.6,0.001,0.02] #theta of first mass, theta of second mass 
                             #,ang momentum of first mass, "  " second mass

timescale = (2*m.pi)/(n)

maxt_unround = 15
cycles = m.ceil(maxt_unround/(2*m.pi))
maxt = cycles*2*m.pi #making maxt an integer multiple of 2pi

for p in range(0,1):

    # FUNCTIONS

    def f1(th1,th2,p1,p2):
        a = 6*(2*p1-3*m.cos(th1-th2)*p2)/(16-9*(m.cos(th1-th2))**2)
        return a

    def f2(th1,th2,p1,p2):
        a = 6*(8*p2-3*m.cos(th1-th2)*p1)/(16-9*(m.cos(th1-th2))**2)
        return a

    def f3(th1,th2,p1,p2):
        a = (-1/2)*(f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*m.sin(th1-th2)+3*g*m.sin(th1)) - 0.1*f1(th1,th2,p1,p2)
        return a

    def f4(th1,th2,p1,p2):
        a = (-1/2)*(-1*f1(th1,th2,p1,p2)*f2(th1,th2,p1,p2)*m.sin(th1-th2)+g*m.sin(th2)) -  0.01*f2(th1,th2,p1,p2)
        return a
    flist = [f1,f2,f3,f4]

    ## APPLYING RK4 ALGO

    from rk4_fnc_pre import rk4_gen

    (y, time) = rk4_gen(flist, initials, timescale, maxt)

    nparray = y

    y = y.tolist()

    ## CONVERT ANGLES TO POSITION

    length = len(y[0])

    phases = [( phases + np.pi) % (2 * np.pi ) - np.pi for phases in y[1]]

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
    poin_phases = [( phases + np.pi) % (2 * np.pi ) - np.pi for phases in poincare_array[0]]

    fncs.plot_2d(poin_phases, poincare_array[2], 'Theta 1', 'Velocity 1', str(p)+ '.1',
                 linestyle = 'none', marker = '.')

    ## Mapping to pie plot

    import operator as op
    
    pie_plot_raw = np.ndarray(shape=(5,length), dtype=float)
    pie_plot_raw[0] = time

    #Overall direction (column 2)
    
    direc_top = fncs.bools_spatial_2var(xpos1, op.ge, 0, ypos1, op.gt,0)
    posi_direc_moment = np.array([x < 0 for x in y[2]]).astype(bool) #long is clockwise
    nega_direc_moment = np.array([x > 0 for x in y[2]]).astype(bool) #short anticlockwise

    posi_bool = direc_top & posi_direc_moment #boolean list for when it is a clockwise/positive/long cross
    nega_bool = direc_top & nega_direc_moment

    comb_bool = posi_bool*1 + nega_bool*-1

    debug = np.ndarray(shape=(4,length), dtype=float)
    debug[0] = time
    debug[1] = comb_bool
    debug[2] = posi_bool



    if nparray[2,1] < 0:
        comb_bool[0] = 1
    else:
        comb_bool[0] = -1
        
    for i in range(1,len(comb_bool)):
        if comb_bool[i-1] == -1 and comb_bool[i] != 1:
            comb_bool[i] = -1
        elif comb_bool[i-1] == 1 and comb_bool[i] != -1:
            comb_bool[i] = 1

    for idx, item in enumerate(comb_bool):
        if item == -1:
            comb_bool[idx] = 0 
    debug[3] = comb_bool
    pie_plot_raw[1] = (comb_bool).astype(int)

    debug = np.matrix.transpose(debug)
    np.savetxt("comb.txt", debug, delimiter=",", fmt= '%i')
    #Local direction (column 3)

    local_direc_cross1 = fncs.bools_spatial_v2(phases, 0)
    local_direc_cross2 = np.array([(phase > 3*m.pi/4 or phase < (-3*m.pi/4)) for phase in phases])

    local_crosses = local_direc_cross1 & local_direc_cross2

    local_momentum_long = np.array([x < 0 for x in y[3]]).astype(bool)
    local_momentum_short = np.array([x > 0 for x in y[3]]).astype(bool)

    comb_bool = local_momentum_long*1 + local_momentum_short*-1

    if nparray[3,1] < 0:
        comb_bool[0] = 1
    else:
        comb_bool[0] = -1
        
    for i in range(1,len(comb_bool)):
        if comb_bool[i-1] == -1 and comb_bool[i] != 1:
            comb_bool[i] = -1
        elif comb_bool[i-1] == 1 and comb_bool[i] != -1:
            comb_bool[i] = 1

    for idx, item in enumerate(comb_bool):
        if item == -1:
            comb_bool[idx] = 0 
    
    pie_plot_raw[2] = (comb_bool).astype(int)
    
    #Wave number (num of rotations while overall direction is constant)

    wavenumber_mem = 0
    state = int(pie_plot_raw[1,0]) # general direction
    state_temp = pie_plot_raw[1,0] # general direction
    local_state = pie_plot_raw[2,0]
    local_state_temp = pie_plot_raw[2,0]
    pie_plot_raw[3,0] = 0
    i = 0

    while i < len(pie_plot_raw[1])-1:
        
        wavenumber = 0
        wavenumber_temp = 0
        state = int(pie_plot_raw[1,i])
        local_state = pie_plot_raw[2,i]

        while local_state_temp == local_state and i < len(pie_plot_raw[1])-1:
            
            wavenumber_temp = abs(m.ceil((nparray[1,i]-m.pi)/(2*m.pi)) - wavenumber_mem)

            if wavenumber_temp > wavenumber:
                wavenumber = wavenumber_temp
                
            i = i + 1
            pie_plot_raw[3,i] = wavenumber
            
            state_temp = pie_plot_raw[1,i]
            local_state_temp = pie_plot_raw[2,i]
            
        wavenumber_mem = m.ceil((nparray[1,i]-m.pi)/(2*m.pi))
    pie_plot_raw[3] = [ x + 1 for x in pie_plot_raw[3]]
    #Levels 

    long_levels = pie_plot_raw[1].astype(bool)
    short_levels = [not x for x in long_levels]
    
    E_bools1 = fncs.bools_spatial_v2(phases, m.pi/2)
    E_bools2 = np.array([(phase < 3*m.pi/4 and phase > (m.pi/4)) for phase in phases])
    E_bools = E_bools1 & E_bools2
    
    T_bools1 = fncs.bools_spatial_v2(phases, 0)
    T_bools2 = np.array([(phase < m.pi/4 and phase > (-m.pi/4)) for phase in phases])
    T_bools = T_bools1 & T_bools2
    
    O_bools1 = fncs.bools_spatial_v2(phases, -m.pi/2)
    O_bools2 = np.array([(phase < -m.pi/4 and phase > (-3*m.pi/4)) for phase in phases])
    O_bools = O_bools1 & O_bools2
    
    X_bools1 = fncs.bools_spatial_v2(phases, 0)
    X_bools2 = np.array([(phase > 3*m.pi/4 or phase < (-3*m.pi/4)) for phase in phases])
    X_bools = X_bools1 & X_bools2
    
    E_vector_long = 1*(E_bools & long_levels)
    T_vector_long = 2*(T_bools & long_levels)
    O_vector_long = 3*(O_bools & long_levels)
    X_vector_long = 4*(X_bools & long_levels)

    E_vector_short = 1*(O_bools & short_levels)
    T_vector_short = 2*(T_bools & short_levels)
    O_vector_short = 3*(E_bools & short_levels)
    X_vector_short = 4*(X_bools & short_levels)
    
    long_level_vector = E_vector_long + T_vector_long + O_vector_long + X_vector_long
    short_level_vector = E_vector_short + T_vector_short + O_vector_short + X_vector_short

    level_vector = long_level_vector + short_level_vector
    
    pie_plot_raw[4] = level_vector

    ### FINAL FILTERING

    transition_filter = np.array([x != 0 for x in level_vector]).astype(bool)
    pie_plot_data = pie_plot_raw[:,transition_filter]

    pie_plot_data[4] = [x-1 for x in pie_plot_data[4]]
    
    ## PLOTS

##    fncs.plot_2d(xpos1, y[2], 'Position 1', 'Velocity 1', str(p)+ '.1',lw = 0.5)
##    fncs.plot_2d(xpos2, y[3], 'Position 2', 'Velocity 2', str(p)+ '.2',lw = 0.5)
##    fncs.plot_2d(time, xpos1, 'Time', 'Position 1', str(p)+ '.3',lw = 0.5)
##    fncs.plot_2d(time, xpos2, 'Time', 'Position 2', str(p)+ '.3',lw = 0.5)
##    fncs.plot_2d(time, y[2], 'Time', 'Velocity 1', str(p)+ '.4',lw = 0.5)
##    fncs.plot_2d(time, y[3], 'Time', 'Velocity 2', str(p)+ '.4',lw = 0.5)


##
### ani.save('double_pendulum.mp4', fps=15)
##


# Libraries
from collections import Counter
from tkinter import *
import wavenumber_funcs as fncs2

### DIALOG BOX
pie_plot_data = np.matrix.transpose(pie_plot_data)
pie_plot_data[1:4].astype(int)
np.savetxt("foo.txt", pie_plot_data, delimiter=",", fmt= '%i')



### ANIMATION ATTEMPTS

    
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(timescale, 0.9, '', transform=ax.transAxes)

def init():                #just draws a clear frame
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, xpos1[3*i], xpos2[3*i]]
    thisy = [0, ypos1[3*i], ypos2[3*i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (3*i*timescale))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, m.ceil(len(y[0])/3)),
                              interval=timescale*3300, blit=True, init_func=init)

plt.show()
