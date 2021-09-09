# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:17:20 2021

This code is for calculating annual average groundater head for comparison

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

data_all1 = np.empty ((9832,175,150))


for i in range(0,9832):  #extract all data
    data_all1[i,:,:] = dfs_f.get_data(i,1)[35] #there is only 1 items and select layer 35


#print(data_all[8030,32,28])

#extract mean annual value of groundwater head
datetime_series = pd.Series(pd.date_range('2000',periods = n, freq = 'Y'))
data_year1 = pd.DataFrame(index = datetime_series, columns = ['mean value'])
for i in range(0,17):
    data_year1.iloc[i:i+1,:] = np.mean(data_all1[365*(10+i):365*(10+i+1),:])



######################################################################################

dfs_f = DFS.DFS3.from_file('K:/Non_dom_runs/S1/S1_riv_irr.she - Result Files/S1_riv_irr_3DSZ.dfs3')
nol = dfs_f.number_of_layers
items = [item.name for item in dfs_f.items]
n = 17 #calculation period
#data_all[i,:,:,:] = dfs_f.get_data(0,1)

data_all2 = np.empty ((9832,175,150))


for i in range(0,9832):  #extract all data
    data_all2[i,:,:] = dfs_f.get_data(i,1)[35] #there is only 1 items and select layer 35


#print(data_all[8030,32,28])

#extract mean annual value of groundwater head
datetime_series = pd.Series(pd.date_range('2000',periods = n, freq = 'Y'))
data_year2 = pd.DataFrame(index = datetime_series, columns = ['mean value'])
for i in range(0,17):
    data_year2.iloc[i:i+1,:] = np.mean(data_all2[365*(10+i):365*(10+i+1),:])

#################################################################################################    
##extract monthly average groundwater head data:
datatime_series = pd.Series(pd.date_range(('2000-01-01'),periods = 17*12, freq = 'M'))
data_month1 = pd.DataFrame(index = datetime_series, columns = ['mean value'])
data_m1 = np.mean (data_all1,axis = 2)
data_m1 = np.mean (data_m1,axis = 1)
for i in range(0,17*12):
    data_month1.iloc[i:i+1,:] = np.mean(data_m1[3650+30*i:3650+30*(i+1)])

data_month2 = pd.DataFrame(index = datetime_series, columns = ['mean value'])
data_m2 = np.mean (data_all2,axis = 2)
data_m2 = np.mean (data_m2,axis = 1)
for i in range(0,17*12):
    data_month2.iloc[i:i+1,:] = np.mean(data_m2[3650+30*i:3650+30*(i+1)])
    
comb = np.array([data_m1,data_m2])
np.savetxt('montly_gw.csv', comb_, delimiter=',')