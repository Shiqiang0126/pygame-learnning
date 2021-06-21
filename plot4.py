# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:04:52 2019

@author: sq
"""

import matplotlib.pyplot as plt
import pandas as pd

d = pd.Series(range(5),index=[chr(ord('A')+i) for i in range(5)])
dc = d.cumsum()


labels = dc.index
sizes = dc.values


plt.pie(sizes, labels=labels, shadow=False)

#plt.axis('equal')
plt.show()
