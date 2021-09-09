# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 14:40:50 2021

This codes create BDP mask for NCP irrigation file

@author: Wensi
"""

import hydroinform.DFS as DFS
import pandas as pd
import numpy as np
from numpy import loadtxt

dfs_f = DFS.DFS0.from_file('Irrigation_well_abstraction_All_YR1.dfs0')
well = loadtxt('irr_ID_wells.txt')    
well = well.astype(int)
# initialize data frame to hold the entire dfs0 file
data = pd.DataFrame(index=dfs_f.time_steps, columns=[it.name for it in dfs_f.items])
#data1 = dfs_f.get_timeseries(1) #get timeseries of first item
i=1
for it in dfs_f.items:
    data[it.name] = dfs_f.get_timeseries(i)
    i=i+1
    
#extract data dates from 2007-2016
dataextr=data.iloc[205:324,:]

#BDP_col = pd.DataFrame(index=dataextr.index,columns=well)
BDP_col = pd.DataFrame(index=dataextr.index)
j = 0
for i in well:
    BDP_col[j] = dataextr.iloc[:,i-1:i]
    j+=1

##write data with coordinates
df = pd.read_csv('I:/Scenarios/Pumping/NCP2BDP/BDP.txt',sep = ',')
# calculate mean temporal data in BDP
mean_data = np.mean(BDP_col,axis=0) #axis=0, remain x-axis
# add mean_data in df
df['Field4'] = pd.Series(mean_data, index=df.index)
#drop NAN values row
df = df.dropna()
#plot irrigation data, kriging may be needed for smoothing the image
ax = df.plot.scatter(x= 'Field2',
                      y= 'Field3',
                      c= 'Field4',
                      colormap='viridis')
#f = interp2d(x_list,y_list,z_list,kind="linear")
#x_coords = np.arange(np.min(x_list),np.max(x_list),2000) ##min()can't work
#y_coords = np.arange(np.min(y_list),np.max(y_list),2000)
#Z = f(x_coords,y_coords)

#fig = plt.imshow(Z,extent=[np.min(x_list),np.max(x_list),np.min(y_list),np.max(y_list)],origin="lower")
plt.colorbar()


# write dataframe to csv file BDP_col.to_csv("BDP_col.csv")
    
mask1 = BDP_col.index.year == 2012

mask2 = BDP_col.index.year == 2013

mask3 = BDP_col.index.year == 2014

mask4 = BDP_col.index.year == 2015

mask5 = BDP_col.index.year == 2016

BDP2012 = BDP_col[mask1]
total2012 = (BDP2012.sum()).sum()

BDP2013 = BDP_col[mask2]
total2013 = (BDP2013.sum()).sum()

BDP2014 = BDP_col[mask3]
total2014 = (BDP2014.sum()).sum()

BDP2015 = BDP_col[mask4]
total2015 = (BDP2015.sum()).sum()

BDP2016 = BDP_col[mask5]
total2016 = (BDP2016.sum()).sum()


#write new data to new dfs0 file

copyfile('Irrigation_well_abstraction_All_YR1.dfs0', 'file_with_new_data.dfs0')
dfs_f = DFS.DFS0.from_file('file_with_new_data.dfs0')
data_new = 0.8*data
new_array = data_new.values
for i in range (0,324):
    for j in range (0,30922):
        dfs_f.set_data(i,j,new_array[i,j])
        j+=1
    i+=1
##data.index;data.columns
#calculate the sum value of individual year
# BDP2012 = BDP_col[BDP_col.index.year == 2012]
# (BDP2012.sum()).sum()
#for it in dfs_f.items:
#  data[it.name] = it.data  # error shows DFSItem has no attribute 'data'


# plot 3D figures 
#columns = BDP_col.columns

#index = BDP_col.index

#x, y = np.meshgrid(np.arange(len(columns)), np.arange(len(index)))

#z = np.array([[BDP_col[c][i] for c in columns] for i in index])

#dataframe to csv file
#BDP2012.to_csv('BDP_2012.csv')