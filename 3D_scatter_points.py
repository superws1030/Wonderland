# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:06:24 2021

@author: Wensi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

df = pd.read_excel('non_dominant_solutions.xlsx')  
x = df['SSR_bias']
y = df['SSR_trend']
z = df['SSR_amp']

x1 = x[9]
y1 = y[9]
z1 = z[9]

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x1,y1,z1,c='r', s=80, marker="o")
ax.scatter(x, y, z,c='b', marker="o")


ax.set_zlabel('SSR_amp', fontdict={'size': 10, 'color': 'black'})
ax.set_ylabel('SSR_trend', fontdict={'size': 10, 'color': 'black'})
ax.set_xlabel('SSR_bias', fontdict={'size': 10, 'color': 'black'})
plt.show()
print(x1)
print(y1)
print(z1)
