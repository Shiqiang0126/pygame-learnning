# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:25:41 2019

@author: sq
"""

import numpy as np
import matplotlib.pyplot as plt
def f(t):
     return np.exp(-t) * np.cos(2*np.pi*t)
 
a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(212)
plt.plot(a,np.cos(2*np.pi*a),'r--')

plt.show()