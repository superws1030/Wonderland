# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:17:20 2021

This code is for calculating mean annual groundater head

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
n = 17 #calculation period
#data_all[i,:,:,:] = dfs_f.get_data(0,1)

data_all = np.empty ((9832,175,150))


for i in range(0,9832):  #extract all data
    data_all[i,:,:] = dfs_f.get_data(i,1)[35] #there is only 1 items and select layer 35


#print(data_all[8030,32,28])

#extract mean annual value of groundwater head
datatime_series = pd.Series(pd.date_range('2000',periods = n, freq = 'Y'))
data_year1 = pd.dataframe(index = datetime_series, columns = ['mean value'])
for i in range(0,16):
    data_year1.iloc[i:i+1,:] = np.mean(data_all[365*(10+i):365*(10+i+1),:])



######################################################################################

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1_riv_irr.she - Result Files/S1_riv_irr_3DSZ.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
n = 17 #calculation period
#data_all[i,:,:,:] = dfs_f.get_data(0,1)

data_all = np.empty ((9832,175,150))


for i in range(0,9832):  #extract all data
    data_all[i,:,:] = dfs_f.get_data(i,1)[35] #there is only 1 items and select layer 35


#print(data_all[8030,32,28])

#extract mean annual value of groundwater head
datatime_series = pd.Series(pd.date_range('2000',periods = n, freq = 'Y'))
data_year2 = pd.dataframe(index = datetime_series, columns = ['mean value'])
for i in range(0,16):
    data_year2.iloc[i:i+1,:] = np.mean(data_all[365*(10+i):365*(10+i+1),:])