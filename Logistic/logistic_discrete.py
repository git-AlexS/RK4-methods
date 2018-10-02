import matplotlib.pyplot as plt
import integration_functions as fncs

maxt = 20
timescale = 0.1

length = int(maxt/timescale)
idx = 0

def listmake(n):
    return [0]*n

xA = listmake(length)
tA = listmake(length)


alist = [0.5, 0.75, 0.87, 0.9]

for p in range(0,len(alist)):

    idx = 0
    initial = 0.2
    xA[0] = initial
    tA[0] = 0

    
    while idx < length-1:

        xA[idx+1] = 4 * alist[p] * xA[idx] * (1- xA[idx])
        tA[idx+1] = tA[idx] + timescale
        idx = idx + 1

    fncs.plot_2d(tA, xA, 'Time', 'Position', str(p)+ '.0',lw = 0.5)

plt.show()
    
