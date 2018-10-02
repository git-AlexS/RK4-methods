# Libraries
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from tkinter import *
import wavenumber_funcs as fncs

### DIALOG BOX

y = np.genfromtxt('foo.txt', delimiter = ',')
#y = np.genfromtxt('dampedpulses.txt', delimiter = ',')
y = np.matrix.transpose(y)
y = y.astype(int)

poincare, drill_in, wavenumbers = fncs.gui_start()

long = 1
short = 0

#comment in/out modules that you want

chunks = fncs.sequential_playback(y) # split data into L/S/L/S... etc.
#chunks = fncs.group_sequential_playback(chunks, short) #group as L/L/L.. or S/S/S...etc.
                                                      #second arg: long or short
#chunks = fncs.summed_playback(y) # split data into total long/total short

chunk_flag = 0

while chunk_flag < len(chunks):

   break_flag = fncs.gui_continue()
   
   if break_flag == 1:
      break

   chunk = chunks[chunk_flag]
   
   direction = chunk[1][0] # short is 0, long is 1

   ### POINCARE (removing repeats)

   if poincare ==1:

      chunk = fncs.poincare(chunk)

   ### SPLIT INTO LONGS AND SHORTS

   longs_bool =  np.array([x==1 for x in chunk[2]])#list of booleans from long/short
   shorts_bool = np.array([x==0 for x in chunk[2]])

   longs =  chunk[:,longs_bool ]
   shorts = chunk[:,shorts_bool]

   longs_shorts = [longs, shorts]
    
   # Create colors
   col=[plt.cm.Blues, plt.cm.OrRd, plt.cm.PuRd, plt.cm.GnBu]

   for i in range(0,2):
      
      if np.size(longs_shorts[1-i]) == 0:
         dummy = np.array([100000,2,1-i,1,0])
         longs_shorts[1-i] = dummy.reshape(dummy.shape[0],-1)
   ### Drill into E, T, O, X or just look at waves

   if drill_in ==1:
      fig = fncs.drill_in(direction,longs_shorts,col)
         
       
   if wavenumbers == 1:
      fig = fncs.wavenumbers(direction,longs_shorts,col)

   plt.show()

   chunk_flag = chunk_flag + 1

