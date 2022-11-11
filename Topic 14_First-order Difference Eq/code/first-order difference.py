# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:02:17 2016

@author: Kaloyan Ganev, Sofia University

Illustrates first-order linear difference equations (autonomous case, 
constant coefficients):

y[t+1] = a*y[t] + b

"""


import numpy as np
import matplotlib.pyplot as plt

y0 = 2 # Initial value
a = -0.6
b = 11
T = 30 # Number of periods
index_set = range(T+1)
y = np.zeros(len(index_set))
ystar =  np.zeros(len(index_set))

# Compute solution
if a == 0:
    print('This is not a difference equation, check your inputs!')
elif a == 1:
    print("Equilibrium does not exist!")
    y[0] = y0
    for t in index_set[1:]:
        y[t] = y0 + t*b
else:
    y[0] = y0
    for t in index_set[1:]:
        y[t] = a*y[t-1] + b

    for t in index_set[0:]:
        ystar[t] = b/(1-a)
        
    print('The equilibrium value of y is %s.' % ystar[T])

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

if a < -1:
    say = '$a < -1$'
elif a == -1:
    say = '$a = -1$'
elif a > -1 and a < 0:
    say = '$-1 < a < 0$'
elif a > 0 and a < 1:
    say = '$0 < a < 1$'
elif a == 1:
    say = '$a = 1$'
elif a > 1:
    say = '$a > 1$'
else:
    say = '$a = 0$'
   

# To see available styles: print(plt.style.available)
with plt.style.context('bmh'):
    if a != 0:    
        pp = plt.figure()
        plt.plot(index_set,y)
        if a != 1:
            plt.plot(index_set,ystar)
        plt.title(say, fontdict=font)
        plt.xlabel('$t$', fontdict=font)
        plt.ylabel('$y_{t}$', fontdict=font)
        
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()
            
        pp.savefig('fig.pdf')
                


