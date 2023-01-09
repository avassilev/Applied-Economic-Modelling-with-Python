# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:02:17 2016

@author: Kaloyan Ganev, Sofia University

Illustrates the solution of the discrete-time Harrod-Domar model

"""


import numpy as np
import matplotlib.pyplot as plt

Y0 = 100000 # Initial output
s = 0.1 # Saving rate, as fraction of 1
v = 0.4
T = 5 # Number of periods
index_set = range((T+1))
Y = np.zeros(len(index_set))

if s <= 0 or s >=1 or v <= 0:
    print('The parameters s and/or v cannot take the values you have specified. Check your inputs.')
else:
    Y[0] = Y0
    for t in index_set[1:]:
        Y[t] = (v/(v-s))*Y[t-1]


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


# To see available styles: print(plt.style.available)
with plt.style.context('bmh'):
    if s > 0 and s < 1 and v > 0:    
        pp = plt.figure()
        plt.plot(index_set,Y)
        plt.title('Output', fontdict=font)
        plt.xlabel('$t$', fontdict=font)
        plt.ylabel('$Y_{t}$', fontdict=font)
        
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()
            
        pp.savefig('fig.pdf')
        
        #print('The monthly payment due is %s.' % round(a,2))



             
