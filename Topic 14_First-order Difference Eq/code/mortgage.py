# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:02:17 2016

@author: Kaloyan Ganev, Sofia University

Illustrates mortgage repayment

"""


import numpy as np
import matplotlib.pyplot as plt

K = 180000 # Initial amount borrowed
r = 0.035 # Interest rate, as fraction of 1
T = 360 # Number of months
index_set = range((T+1))
b = np.zeros(len(index_set))
#r = np.random.uniform(0,0.1,T+1)

if r < 0:
    print('Negative interest rate, banks cannot be that generous :)')
else:
    # Monthly payment
    a = r/12*K*(1+r/12)**(T)/((1+r/12)**(T) - 1)
    # Principal
    b[0] = K
    for t in index_set[1:]:
        b[t] = (1+r/12)*b[t-1] - a


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


# To see available styles: print(plt.style.available)
with plt.style.context('bmh'):
    if r >= 0:    
        pp = plt.figure()
        plt.stackplot(index_set,b)
        plt.title('Principal', fontdict=font)
        plt.xlabel('$t$', fontdict=font)
        plt.ylabel('$b_{t}$', fontdict=font)
        
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()
            
        pp.savefig('fig.pdf')
        
        print('The monthly payment due is %s.' % round(a,2))



             
