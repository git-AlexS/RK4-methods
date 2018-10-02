import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

timescale = 0.1 #float(input ("Timescale: "))
#maxt = [50,100,150]
maxt=150
damp = [0.18,0.27,0.6]
initials = [0,0,0]
c = 0.1

def listmaker(value,length):
        return [value]*length


Step =[1,2,1,0.5,0,1,0,-3,-2.5] # Time series 
#Step =[1,3,4.5,4]          # Elliott Wave
#Step =[1]                 # Step Input
n = len(Step)
step_var = []

#Create the continous Step function
for j in range(0,n):
        lengths = m.floor(maxt/(timescale*n))
        step_var.extend(listmaker(Step[j],lengths))

#End of Step array padding 
while len(step_var) <= round(int(maxt/timescale))+1:
       step_var.append(Step[n-1]) 
       #print(Step[n-1])


for i in range (0,3):
        
        b = damp[i]
           
        # FUNCTIONS

        #f1 
        def f1(x,y,t):
            a = y
            return a

        #f2 
        def f2(x,y,t):
            a = -(c*x+b*y) +step_var[int(round(t/timescale))]
            return a

        def f3(x,y,t):
            a = 1
            return a


        flist = [f1,f2,f3]

        ## APPLYING RK4 ALGO

        from rk4_fnc_pre import rk4_gen

        (y, time) = rk4_gen(flist, initials, timescale,maxt)

        y = y.tolist()

        ## PLOTS


        fig = plt.figure(0) # 0 instead of i creates overlay chart


        plt.plot(time,y[0], lw=0.5)

        plt.xlabel("Time")
        plt.ylabel("Target Levels ")



plt.show()
