# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:41:30 2021

@author: Wensi
"""
import numpy as np
f = np.loadtxt('tsimtsim_extra.asc')
#for n in range(0,50):
l = np.empty(21939)
for i in range(0,21939):
   l[i] = f[i]
#with open("layer.txt",'w') as f:
# f.write(l)
np.savetxt("ly1.txt",l) 