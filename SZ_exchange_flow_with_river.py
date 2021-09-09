# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:17:20 2021

@author: Wensi
"""

import hydroinform.DFS as DFS
import numpy as np
from matplotlib import pyplot as plt, cm
import matplotlib
import pandas as pd

dfs_f = DFS.DFS3.from_file('I:/test13/scenario2/scenario2.she - Result Files/scenario2_3DSZflow.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all1 = np.empty ((9832,175,150))


for i in range(8030,9832):  #2012-2016
    data_all1[i,:,:] = dfs_f.get_data(i,5)[38] #(0,4) or (i,4)? seems the same results

#print(data_all[8030,30,96])

#mean_data = np.mean(data_all,axis=0)

#new_data = np.empty ((175,150))
#new_new_data = np.empty ((175,150))

#for i in range (0,175):
#    for j in range (0,150):
#        new_data[i,j] = mean_data[174-i,149-j]
#        j+=1
#    i+=1

#for i in range (0,150):
#    new_new_data[:,i] = new_data[:,149-i]
#    i+=1

#res1 = pd.DataFrame(new_new_data) #transform array to dataframe
#res1 = res1.replace(-1.832790919894754e-36,np.NaN) #replace background value with NaN
#im = plt.imshow(res1, cmap='viridis') 

######################################################################################

dfs_f = DFS.DFS3.from_file('I:/test13/Geounits_sub2_test13.she - Result Files/Geounits_sub2_test13_3DSZflow.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all2 = np.empty ((9832,175,150))


for i in range(8030,9832):
    data_all2[i,:,:] = dfs_f.get_data(i,5)[38] #(0,4) or (i,4)? seems the same results

#print(data_all[8030,30,96])

mean_data = np.mean(data_all2-data_all1,axis=0)

new_data = np.empty ((175,150))
new_new_data = np.empty ((175,150))

for i in range (0,175):
    for j in range (0,150):
        new_data[i,j] = mean_data[174-i,149-j]
        j+=1
    i+=1

for i in range (0,150):
    new_new_data[:,i] = new_data[:,149-i]
    i+=1

res2 = pd.DataFrame(new_new_data) #transform array to dataframe
res2 = res2.replace(-1.832790919894754e-36,np.NaN) #replace background value with NaN
cmap_reversed = matplotlib.cm.get_cmap('viridis_r')
im = plt.imshow(res2, cmap=cmap_reversed,vmin=0.004, vmax=0.006) 
plt.colorbar()
plt.show()