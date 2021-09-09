# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:31:30 2021

@author: Wensi
"""
import numpy as np
p = np.loadtxt('111.txt')

data=np.empty(shape=[204,30922],dtype=float)


xyi = 0;
for y in range(0,30922):
  for x in range(0,204):
    data[xyi] = 0.7*p[xyi]
    xyi = xyi+1
    print(xyi)
np.savetxt('reduced.txt',data)
#l = np.empty[p.shape[0],p.shape[1]]