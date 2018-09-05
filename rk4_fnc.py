import numpy as np

#flist: list of functions
#list of initial conditions
#timescale (minimum time step dt/gridspacing d)

def rk4_gen(flist, initials, timescale, maxt):
    
    time = [0]
    i = 0
    t = 0
    n = len(initials)

    y = np.ndarray(shape=(n,1), dtype=float)
    y[:,0] = initials
    yadd = np.ndarray(shape=(n,1), dtype=float)
    dt = timescale

    
    n = len(initials)
    k = np.ndarray(shape=(n,4), dtype=float)  #RK coeffs for all n variables

    while t < maxt:
    
        for j in range(0,n):
            k[j,0] = flist[j](*y[:,i])
            k[j,1] = flist[j](*(y[:,i]+(k[:,0]*(dt/2))))
            k[j,2] = flist[j](*(y[:,i]+(k[:,1]*(dt/2))))
            k[j,3] = flist[j](*(y[:,i]+(k[:,2]*(dt))))

        for l in range(0,n):
            
            yadd[l,0] = y[l,i] + (k[l,0] + 2*k[l,1] + 2*k[l,2] + k[l,3])*(dt/6)

        y = np.concatenate((y,yadd),axis = 1)

        #TODO:  research efficiency of concatenate and method -
        #       maybe worthwhile just predefining dim of y array

        t = t + dt
        i = i +1
        time.append(t)

    return(y,time)


