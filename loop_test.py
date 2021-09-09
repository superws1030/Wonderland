# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:03:31 2021

@author: Wensi
"""
import numpy as np
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import DateOffset

filenames = ['1.txt', '2.txt', '3.txt']
array_obs = np.empty((15,62))
array_sim = np.empty((15,62))
x = 0 
for obs_fp in filenames: '1.txt', '2.txt', '3.txt'
df = pd.read_table(obs_fp, sep='\t', engine='python', header=0)
LS_data = df.values[:,:]
    
# Convert dates to ordinal numbers
#LS_dates = LS_data[:,6]
LS_dates = pd.to_datetime(df.values[:,6],dayfirst=True).strftime("%Y-%m-%d").tolist()
LS_dates_min = min(pd.to_datetime(df.values[:,6]))
LS_dates_max = max(pd.to_datetime(df.values[:,6]))
dates_lst = pd.date_range(LS_dates_min,LS_dates_max + DateOffset(months=11),freq='MS').strftime("%Y-%m-%d").tolist()
    
    
obs_id = np.unique(LS_data[:,0]) # NOT sorted
    
    
# Assumptions
#assert() # Check assumption of monthly time steps in LS_input_observations.txt
    
# Data extraction for each well
well_ts = [] # Head data in each well
well_nan_sim = np.full((len(obs_id),len(dates_lst)),np.nan) # Sim head ts in each well
well_nan_obs = np.full((len(obs_id),len(dates_lst)),np.nan) # Obs head ts in each well
#lyr_id = np.empty(len(obs_id)) # Layer of well
#geo_id = np.empty((len(obs_id),2)) # Geounit of well [lyr1,lyr2]
#    ts_uniq = np.empty((len(obs_id)))
for i in range(0,len(obs_id)):
    obs_indx_tmp = np.asarray(np.where(LS_data[:,0]==obs_id[i])).squeeze()
#    lyr_id[i] = 1
#    bool_tmp = (id_strip==obs_id[i].strip('obs'))
#        print(bool_tmp)
#    geo_id[i,:] = [id_all.loc[bool_tmp.index[bool_tmp].tolist(),'lay1_GeoCo'].values[0], id_all.loc[bool_tmp.index[bool_tmp].tolist(),'lay2_GeoCo'].values[0]]
#        sim_data_tmp = np.array(LS_data[obs_indx_tmp,7])
#        ts_uniq[i] = len(np.unique(sim_data_tmp[~np.isnan(sim_data_tmp)]))
    if len(obs_indx_tmp) == LS_data[obs_indx_tmp[0],-1]:
            pass        
    else:
            print('Well no. ' + str(i) + ' #Obs and time series observations do not match')
        # Extract time series of obs and sim
    well_ts.append([LS_data[obs_indx_tmp,5].tolist(), LS_data[obs_indx_tmp,7].tolist()])
    well_tmp = np.full([2,len(dates_lst)], np.nan) # NaN values array for sim and obs for the full time series
# Obs and sim ts with data gaps as NaN values
    date_indx_tmp = [dates_lst.index(i) for i in [LS_dates[i] for i in obs_indx_tmp]]
    well_nan_obs[i,date_indx_tmp] = LS_data[obs_indx_tmp,5]
    well_nan_sim[i,date_indx_tmp] = LS_data[obs_indx_tmp,7]
        
#        indx_cut = np.where(well_nan_sim[2,:-1] != well_nan_sim[2,1:])[0]

#well_nan_err = well_nan_obs-well_nan_sim # errors 
#well_nan_me = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
#well_nan_mae = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
#well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
#well_nan_rmse = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells
array_obs[x] = np.nanmean(well_nan_obs,axis=1)
array_sim[x] = np.nanmean(well_nan_sim,axis=1)
x += 1