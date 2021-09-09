# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:17:20 2021

This code is for calculation groundwater head variations between two _3DSZ.dfs files

time resolution: day


@author: Wensi
"""

import hydroinform.DFS as DFS
import numpy as np
from matplotlib import pyplot as plt, cm
import matplotlib as mpl
import pandas as pd

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1.she - Result Files/S1_3DSZ.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all = np.empty ((9832,175,150))


for i in range(365*17,9832):  #extract year from 2007-2016 : 1 (1990) + 16 (1991-2016) = 17
    data_all[i,:,:] = dfs_f.get_data(i,1)[35] #there is only 1 items and select layer 35

#print(data_all[8030,32,28])

#extract mean annual value of groundwater head


mean_data = np.mean(data_all,axis=0)  #calculate mean data in a daily level

new_data = np.empty ((175,150))
new_new_data1 = np.empty ((175,150))

# put the data in right layout
for i in range (0,175):
    for j in range (0,150):
        new_data[i,j] = mean_data[174-i,149-j]
        j+=1
    i+=1

for i in range (0,150):
    new_new_data1[:,i] = new_data[:,149-i]
    i+=1

res1 = pd.DataFrame(new_new_data1) #transform array to dataframe
res1 = res1.replace(-3.6889748426516494e-36,np.NaN) #replace background value with NaN

######################################################################################

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1_riv_irr.she - Result Files/S1_riv_irr_3DSZ.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
#data_all[i,:,:,:] = dfs_f.get_data(0,1)


data_all = np.empty ((9832,175,150))


for i in range(365*17,9832):  #extract year from 2007-2016
    data_all[i,:,:] = dfs_f.get_data(i,1)[35] #(0,4) or (i,4)? seems the same results

#print(data_all[8030,32,28])

mean_data = np.mean(data_all,axis=0)

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
res2 = res2.replace(-3.6889748426516494e-36,np.NaN) #replace background value with NaN

#show the variation distribution

mpl.rc('font',family='Times New Roman') #change default font for all drawings
im = plt.imshow(res2-res1, cmap='viridis')
csfont = {'fontname':'Times New Roman'}
plt.title('Groundwater head (m)',fontsize = 15,**csfont)
plt.xticks(fontsize = 10, **csfont)
plt.yticks(fontsize = 10, **csfont)
plt.colorbar()
plt.show()
plt.savefig('Groundwater head' + '.png',format='png')
#calculate statistics
var = res2 -res1
max = np.nanmax(var)
min = np.nanmin(var)
mean = np.nanmean(var)
#me1 = var.mean()
#mean = me1.mean()