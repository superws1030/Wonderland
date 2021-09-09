# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:16:22 2021

Time resolution:month
@author: Wensi
"""

import hydroinform.DFS as DFS
import pandas as pd
from shutil import copyfile
import numpy as np


# extract data from dfs2 file
dfs_f = DFS.DFS0.from_file('ORIGIN_Irrigation_well_abstraction_All_YR1.dfs0')
data = pd.DataFrame(index=dfs_f.time_steps, columns=[it.name for it in dfs_f.items])
i=1  #### can only be 1!
for it in dfs_f.items:
    data[it.name] = dfs_f.get_timeseries(i)
    i=i+1
Array = data.values #this step can't be skipped!



#write new data to new dfs0 file
copyfile('ORIGIN_Irrigation_well_abstraction_All_YR1.dfs0', 'file_with_new_data.dfs0')
dfs_f = DFS.DFS0.from_file('file_with_new_data.dfs0')

# from 2007-2016 the irrigation data reduce 20%, including 2007
for i in range (0,205):  # 12*17 = 204; 1 (1990) + 16 (1991-2016) = 17
    for j in range (0,30922):
        dfs_f.set_data(i,j,Array[i,j])
        j+=1
    i+=1

for i in range (205,324):
    for j in range (0,30922):
        dfs_f.set_data(i,j,0.8*Array[i,j]) #reduction ratio 0.8
        j+=1
    i+=1

# extract data from new created file and check if the values reduced
dfs_f = DFS.DFS0.from_file('file_with_new_data.dfs0')
data1 = pd.DataFrame(index=dfs_f.time_steps, columns=[it.name for it in dfs_f.items])
i=1
for it in dfs_f.items:
    data1[it.name] = dfs_f.get_timeseries(i)
    i=i+1
    
check = data-data1


#illustrate irrigration pattern
irr_diff = np.empty ((120,30922))
Array_irr = data1.values
for i in range (205,324):
    for j in range (0,30922):
        irr_diff[i-205,j] = Array_irr[i,j]
        j+=1
    i+=1
irr_diff_mean = irr_diff_mean()

#for i in range(0,30922):
#    for j in range(0,324):
#        if j <  205:
#           dfs_f.set_data(i,j,Array[i,j])
#        else:
#           dfs_f.set_data(i,j,0.8*Array[i,j])
#        j+=1
#    i+=1

    













#temp_fp = 'Irrigation_well_abstraction_All_YR1.dfs0'
#create new empty DFS0 file 'output_file.dfs0', based on the template file's properties
#out_f = DFS.DFS0.from_template_file('output_file.dfs0', temp_fp)
# change time axis (if necessary)
#out_f.start_time = ts[0].astype('M8[D]').astype('O')
#out_f.time_step_size = DFS.timedelta(days=1) #never change time_step_unit - that has to be left as seconds!
# loop over all timesteps (need to be sorted chronologically!) and write the file timestep by timestep
