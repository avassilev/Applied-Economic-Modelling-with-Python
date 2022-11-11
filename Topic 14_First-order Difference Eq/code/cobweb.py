# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:02:17 2016

@author: Kaloyan Ganev, Sofia University

Illustrates the solution of the cobweb model

"""


import numpy as np
import matplotlib.pyplot as plt

p0 = 5 # Initial price after shock
alpha = 10 # 
beta = 1.5 #
gamma = 1 # 
delta = 1.5 #
T = 10 # Number of periods
index_set = range((T+1))
p = np.zeros(len(index_set))

if alpha <= 0 or beta <= 0 or delta <= 0:
    print('The parameters cannot take the values you have specified. Check your inputs.')
else:
    p[0] = p0
    for t in index_set[1:]:
        p[t] = (alpha - gamma)/beta -(delta/beta)*p[t-1]


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


# To see available styles: print(plt.style.available)
with plt.style.context('bmh'):
    if alpha > 0 and beta > 0 and delta > 0:    
        pp = plt.figure()
        plt.plot(index_set,p)
        plt.title('Price', fontdict=font)
        plt.xlabel('$t$', fontdict=font)
        plt.ylabel('$p_{t}$', fontdict=font)
        
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()
            
        pp.savefig('fig.pdf')
        
        #print('The monthly payment due is %s.' % round(a,2))



             
