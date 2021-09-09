# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:17:20 2021

This codes are for calculating mean annual SZ exchange flow with river individually 

time resolution: day

@author: Wensi
"""

import hydroinform.DFS as DFS
import numpy as np
from matplotlib import pyplot as plt, cm
import matplotlib
import pandas as pd
import matplotlib as mpl

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1.she - Result Files/S1_3DSZflow.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all = np.empty ((9832,175,150))


for i in range(365*17,9832):  #2007-2016
    data_all[i,:,:] = dfs_f.get_data(i,5)[38] #The 5th item and layer 38

#print(data_all[8030,30,96])

sum_data = np.sum(data_all*10516*1000*1000/1000000000,axis=0) #converse unit from mm to km^3
mean_data = sum_data/10  #calculate mean annual value
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

res1 = pd.DataFrame(new_new_data) #transform array to dataframe
res1 = res1.replace(-3.814153268664188e-32,np.NaN) #replace background value with NaN
cmap_reversed = matplotlib.cm.get_cmap('viridis_r') #reverse color bar
im = plt.imshow(res1, cmap=cmap_reversed) 
plt.colorbar()
plt.show()

######################################################################################

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1_riv_irr.she - Result Files/S1_riv_irr_3DSZflow.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all = np.empty ((9832,175,150))


for i in range(365*17,9832):
    data_all[i,:,:] = dfs_f.get_data(i,5)[38] #(0,4) or (i,4)? seems the same results

#print(data_all[8030,30,96])

sum_data = np.sum(data_all*10516*1000*1000/1000000000,axis=0) #converse unit from mm to km^3
mean_data = sum_data/10  #calculate mean annual value

# transpose the layout way of data

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
res2 = res2.replace(-3.814153268664188e-32,np.NaN) #replace background value with NaN

var = res2 - res1
max = np.nanmax(var)
min = np.nanmin(var)
mean = np.nanmean(var)
#max_value = var.to_numpy().max()
#min_value = var.to_numpy().min()
#mean_value = var.mean()
mpl.rc('font',family='Times New Roman')
csfont = {'fontname':'Times New Roman'}
cmap_reversed = matplotlib.cm.get_cmap('viridis_r') #reverse color bar
im = plt.imshow(var, cmap=cmap_reversed) 
plt.title('Saturated zone exchange with river (km^3/year)',fontsize = 15,**csfont)
plt.colorbar()
plt.show()