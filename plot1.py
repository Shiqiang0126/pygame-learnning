# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:13:02 2019

@author: sq
"""

import matplotlib.pyplot as plt

plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('Grade')
plt.xlabel('foo')
plt.axis([-1,20,-1,10])
plt.show()