# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:02:17 2016

@author: Kaloyan Ganev, Sofia University

Illustrates compound interest and PDVs with constant rates:

w[t+1] = (1+r[t+1])*w[t] + y[t+1] - c[t+1]

"""


import numpy as np
import matplotlib.pyplot as plt

w0 = 100 # Initial wealth
# r = 0.08 # Interest rate, as fraction of 1
T = 30 # Number of periods
index_set = range(T+1)
w = np.zeros(len(index_set))
r = np.random.uniform(0,0.1,T+1)
y = np.random.uniform(9,10,T+1)
c = 0.5 + 0.8 * y + np.random.normal(0,1,T+1)

w[0] = w0
for t in index_set[1:]:
    w[t] = (1+r[t])*w[t-1] + y[t] - c[t] # r[t] should be r if r is fixed


#Present Discount Value
pdv = w[T]/(np.prod(1+r))**(1/T)


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


# To see available styles: print(plt.style.available)
with plt.style.context('bmh'):
    #if r >= 0:    
        pp = plt.figure()
        plt.plot(index_set,w)
        plt.title('Compounded Amount over Time', fontdict=font)
        plt.xlabel('$t$', fontdict=font)
        plt.ylabel('$w_{t}$', fontdict=font)
        
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()
            
        pp.savefig('fig.pdf')
        
print('The PDV of the amount received at the end of the last period is %s.' % round(pdv,2))



             
