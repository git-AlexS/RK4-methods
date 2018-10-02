from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

### GUI

def gui_start():

    master = Tk()

    Label(master, text="Run which functions:").grid(row=0, sticky=W)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    Checkbutton(master, text="Poincare", variable=var1).grid(row=1, sticky=W)
    Checkbutton(master, text="Drill In", variable=var2).grid(row=2, sticky=W)
    Checkbutton(master, text="Wavenumbers", variable=var3).grid(row=3, sticky=W)
    Button(master, text='Start', command=master.destroy).grid(row=4, sticky=W, pady=4)
    

    mainloop()

    poincare=    int(var1.get())
    drill_in=    int(var2.get())
    wavenumbers= int(var3.get())

    return poincare, drill_in, wavenumbers

def gui_continue():

    master = Tk()
    
    Label(master, text="Continue?").grid(row=0, sticky=W)

    var1 = IntVar()
    Checkbutton(master, text="Quit?", variable=var1).grid(row=1, sticky=W)
    
    Button(master, text='Contiue', command=master.destroy).grid(row=2, sticky=W, pady=4)

    mainloop()

    break_flag = int(var1.get())

    return break_flag

### MISC functions

def sequential_playback(y):
    
    chunks = []

    diff = np.insert(np.diff(y[1]),0,0)
    indexobj = np.where(diff != 0 )

    indices = list(indexobj[0])
    indices.insert(0,0)
    indices.append(len(y[1]))

    for j in range(0,len(indices)-1):

        chunks.append(y[:,indices[j]:indices[j+1]])

    return chunks

def group_sequential_playback(chunks, direction):

    j=0
    chunks_even = []
    chunks_odd = []
    
    while 2*j < len(chunks):
        chunks_even.append(chunks[2*j])
        j = j+1

    j=0
    
    while 2*j+1 < len(chunks):
        chunks_odd.append(chunks[2*j+1])
        j = j+1
        
    if ((direction == 1 and chunks_even[0][1,0] == 1) or (direction == 0 and chunks_even[0][1,0] == 0)):    
        chunks = chunks_even
    else:
        chunks =  chunks_odd

    return chunks

def summed_playback(y):

    chunks = []

    long_bool = np.array([x == 1 for x in y[1]]).astype(bool)
    chunks.append(y[:,long_bool])

    short_bool = np.array([x == 0 for x in y[1]]).astype(bool)
    chunks.append(y[:,short_bool])
    
    return chunks
    
 
def arraynums(length,number):
    return [number]*length

def poincare(y):
    
    if len(y[1]) == 1:
        return y
    
    else:
        dif_direc = np.diff(y[2])

        direc_bool = np.array([x!=0 for x in dif_direc]).astype(bool)

        direc_bool = np.append(direc_bool,True)

        bools = direc_bool 

        y = y[:,bools]

        return y
    
def bools_spatial_v2(pos, threshold):

    pos_filter = np.array([x > threshold for x in pos])
    pos_filter_ints = np.multiply(pos_filter,1)

    diff = np.diff(pos_filter_ints)
    diff = np.insert(diff,0,0) 
    pos_bool = np.array([x != 0 for x in diff]).astype(bool) 

    return pos_bool

def bools_diff(pos):
    diff = np.diff(pos)
    diff = np.insert(diff,0,0) 

    return np.array([x!=0 for x in diff]).astype(bool)

### PLOTTING FUNCTIONS

def drill_in(direction,longs_shorts,col):

    fig, axes = plt.subplots(nrows=1, ncols=2)
    fig.suptitle('Starting date: ' + str(longs_shorts[1 - direction][0,0]))
    
    for i in range(0,2):

        group_size= arraynums(4,1)
        array = longs_shorts[i]
        if len(array[3]) > 0 :
            
            max_wavenumber = max(array[3])

            mypie = arraynums(max_wavenumber,0)
            e = arraynums(max_wavenumber,0)

            for j in range(1,max_wavenumber+1):

                wave_bool = np.array([x==j for x in array[3]]).astype(bool)
                e[j-1] = Counter(array[:,wave_bool][4])
                
            length = len(longs_shorts[0][1])+ len(longs_shorts[1][1]) #not necessarily the way dad wants to do this, will affect colouring

            
            for n in range(0,max_wavenumber):
                colcoeffs = arraynums(4,0)
                nums = arraynums(4,0)
                for m in range(0,4):
                    if e[n][m] ==0 :
                        nums[m] = ' '
                    else:
                        nums[m] = e[n][m]
                        
                    colcoeffs[m] = col[i](e[n][m]*7/(length))
                

                label = [str(nums[0]) , str(nums[1]) ,str(nums[2]) ,str(nums[3])]

                mypie[n], _ = axes[i].pie(group_size, radius= (0.5+n*0.1), labels=label,
                                          labeldistance=0.65+n*0.035,
                                          colors=colcoeffs )
            
                plt.setp( mypie[n], width=0.2, edgecolor='white')

        label = ['E','T','O','X']
        solidpie, _ = axes[i].pie(group_size, radius = 0.2, colors = ['w'], labels = label)
        plt.setp(solidpie, width = 0.2, edgecolor = 'white')
        
        if (direction == 0 and i == 1):
                solidpie, _ =  axes[i].pie([1],radius = 0.0001, colors = [col[i](0.99)])
                plt.setp(solidpie, width = 0.2, edgecolor = 'white')
        elif (direction == 1 and i == 0):
                solidpie, _ =  axes[i].pie([1],radius = 0.0001, colors = [col[i](0.99)])
                plt.setp(solidpie, width = 0.2, edgecolor = 'white')
                
    return fig

def wavenumbers(direction,longs_shorts,col):

    fig, axes = plt.subplots(nrows=1, ncols=2)
    earliest_date = min([min(longs_shorts[0][0]),min(longs_shorts[1][0])])
    fig.suptitle('Starting date: ' + str(earliest_date))
    
    for i in range(0,2):

        group_size= arraynums(1,1)
        array = longs_shorts[i]
        print(i,'1#',array)
        new_wave_bool = np.array([x == 0 for x in array[4]]).astype(bool)
        array = array[:,new_wave_bool]

        print(i,'2#',array)
        max_wavenumber = max(array[3])
        mypie = arraynums(max_wavenumber,0)
        d = Counter(array[3])
        print(d)
        length = len(longs_shorts[0][1])+ len(longs_shorts[1][1])
    
        for n in range(0,max_wavenumber):
            
            colcoeff = d[n+1]*2/(length)
            mypie[n], _ = axes[i].pie(group_size, radius= (0.5+n*0.1), labels=[ str(d[n+1])],
                                 labeldistance=0.5+n*0.1, colors=[col[i](colcoeff)], startangle=n*5 )
            plt.setp( mypie[n], width=0.2, edgecolor='white')

        if (direction == 0 and i == 1):
            solidpie, _ =  axes[i].pie([1],radius = 0.0001, colors = [col[i](0.99)])
            plt.setp(solidpie, width = 0.2, edgecolor = 'white')
        elif (direction == 1 and i == 0):
            solidpie, _ =  axes[i].pie([1],radius = 0.0001, colors = [col[i](0.99)])
            plt.setp(solidpie, width = 0.2, edgecolor = 'white')

    return fig
