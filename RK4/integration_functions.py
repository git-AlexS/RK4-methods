import numpy as np
import math as m
import random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

def zerolistmaker(n):
    return [0]*n

def randlistmaker(n,upper,lower):
    a = rnd.uniform(upper,lower)
    return [a]*n

def noise(length, timescale, noise_rate, noise_amp):
    rand = []
    while len(rand) < length:
        rand.extend(randlistmaker(noise_rate,noise_amp,(-1*noise_amp)))
    return rand    

## PLOTTING TOOLS

def plot_2d(x,y,xlab,ylab,fig_no,**style):
    
    fig = plt.figure(fig_no)
    plt.plot(x,y, **style)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    
    return fig


def poincare_map(x, v, stepsize, n_cycles):
    
    p_map_pos = []
    p_map_vel = []

    for l in range(0,n_cycles):
        p_map_pos.append(x[l*stepsize])
        p_map_vel.append(v[l*stepsize])
        
    return (p_map_pos,p_map_vel)


def embed_dim(x,length,start):
    
    position_add1 = zerolistmaker(length)
    for j in range(start,length):
        position_add1[j] = x[j-start]
        
    return position_add1

def bools_spatial_1var(pos, threshold, extract_from_diff):

    pos_filter = np.array([x > threshold for x in pos])
    pos_filter_ints = np.multiply(pos_filter,1)

    diff = np.diff(pos_filter_ints)
    diff = np.insert(diff,0,0) 
    pos_bool = np.array([x == extract_from_diff for x in diff]).astype(bool) 

    return pos_bool

def bools_spatial_v2(pos, threshold):

    pos_filter = np.array([x > threshold for x in pos])
    pos_filter_ints = np.multiply(pos_filter,1)

    diff = np.diff(pos_filter_ints)
    diff = np.insert(diff,0,0) 
    pos_bool = np.array([x != 0 for x in diff]).astype(bool) 

    return pos_bool

import operator as op 

def bools_spatial_2var(pos1, op1, thr1, pos2, op2, thr2):

    pos_filter1 = np.array([op1(x,thr1) for x in pos1])
    pos_filter_ints = np.multiply(pos_filter1,1)
    
    diff = np.diff(pos_filter_ints)
    diff = np.insert(diff,0,0)
    pos_bool = np.array([x != 0 for x in diff]).astype(bool)
    
    pos_filter2 = np.array([op2(x,thr2) for x in pos2])
    
    comb_pos_bool = pos_bool & pos_filter2

    return comb_pos_bool    

    
    
