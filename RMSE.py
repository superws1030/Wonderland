# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:50:03 2021

@author: Wensi
"""
import os, csv
import sys
import getopt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  
from datetime import datetime
from pandas.tseries.offsets import DateOffset
from scipy import stats
import statistics
#Round1

obs_fp = '1.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
df = pd.read_table(obs_fp, sep='\t', engine='python', header=0)
print(df)
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me1 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae1 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse1 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs1 = np.nanmean(well_nan_obs,axis=1)
array_sim1 = np.nanmean(well_nan_sim,axis=1)


#Round2

obs_fp2 = '2.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
df = pd.read_table(obs_fp2, sep='\t', engine='python', header=0)
print(df)
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me2 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae2 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse2 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs2 = np.nanmean(well_nan_obs,axis=1)
array_sim2 = np.nanmean(well_nan_sim,axis=1)



#Round3
obs_fp3 = '3.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
df = pd.read_table(obs_fp3, sep='\t', engine='python', header=0)
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me3 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae3 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse3 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs3 = np.nanmean(well_nan_obs,axis=1)
array_sim3 = np.nanmean(well_nan_sim,axis=1)

#Round 4

obs_fp = '4.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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

well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me4 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae4 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse4 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs4 = np.nanmean(well_nan_obs,axis=1)
array_sim4 = np.nanmean(well_nan_sim,axis=1)


#Round 5

obs_fp = '5.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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

well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me5 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae5 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse5 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs5 = np.nanmean(well_nan_obs,axis=1)
array_sim5 = np.nanmean(well_nan_sim,axis=1)

#Round 6

obs_fp = '6.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me6 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae6 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse6 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs6 = np.nanmean(well_nan_obs,axis=1)
array_sim6 = np.nanmean(well_nan_sim,axis=1)

#Round 7

obs_fp = '7.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me7 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae7 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse7 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs7 = np.nanmean(well_nan_obs,axis=1)
array_sim7 = np.nanmean(well_nan_sim,axis=1)

#Round 8

obs_fp = '8.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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

well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me8 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae8 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse8 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs8 = np.nanmean(well_nan_obs,axis=1)
array_sim8 = np.nanmean(well_nan_sim,axis=1)

#Round 9

obs_fp = '9.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me9 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae9 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse9 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs9 = np.nanmean(well_nan_obs,axis=1)
array_sim9 = np.nanmean(well_nan_sim,axis=1)

#Round 10

obs_fp = '10.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me10 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae10 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse10 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells

array_obs10 = np.nanmean(well_nan_obs,axis=1)
array_sim10 = np.nanmean(well_nan_sim,axis=1)

array_obs_all = np.array([array_obs1,array_obs2,array_obs3,array_obs4,array_obs5,array_obs6,array_obs7,array_obs8,array_obs9,array_obs10])
array_sim_all = np.array([array_sim1,array_sim2,array_sim3,array_sim4,array_sim5,array_sim6,array_sim7,array_sim8,array_sim9,array_sim10])

#Round 11

obs_fp = '11.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me11 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae11 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse11 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs11 = np.nanmean(well_nan_obs,axis=1)
array_sim11 = np.nanmean(well_nan_sim,axis=1)

#Round 12

obs_fp = '12.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me12 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae12 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse12 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs12 = np.nanmean(well_nan_obs,axis=1)
array_sim12 = np.nanmean(well_nan_sim,axis=1)

#Round 13

obs_fp = '13.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me13 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae13 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse13 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs13 = np.nanmean(well_nan_obs,axis=1)
array_sim13 = np.nanmean(well_nan_sim,axis=1)

#Round 14

obs_fp = '14.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me14 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae14 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse14 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs14 = np.nanmean(well_nan_obs,axis=1)
array_sim14 = np.nanmean(well_nan_sim,axis=1)


#Round 15

obs_fp = '15.txt'


    
### Import sim and obs groundwater heads from LayerStatistics
    
# Header information
# OBS_ID, X, Y, Depth, LAYER, OBS_VALUE, DATO, SIM_VALUE_INTP, SIM_VALUE_CELL, ME, ME^2, #DRY_CELLS, #BOUNDARY_CELLS, COLUMN, ROW, COMMENT, #OBSInWell
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
well_nan_err = well_nan_obs-well_nan_sim # errors 
well_nan_me15 = np.nanmean(well_nan_err,axis=1) # ME for each well
#    print(well_nan_me.shape)
well_nan_mae15 = np.nanmean(abs(well_nan_err),axis=1) # MAE for each well
#    well_nan_me_2 = np.nanmean(well_nan_err,axis=1)**2
well_nan_me_2 = np.nanmean(well_nan_err**2,axis=1) # squared ME for each well
#    print(well_nan_me_2.shape)
well_nan_rmse15 = np.sqrt(np.nanmean(well_nan_me_2)) # rmse for all wells


array_obs15 = np.nanmean(well_nan_obs,axis=1)
array_sim15 = np.nanmean(well_nan_sim,axis=1)


array_obs_all = np.array([array_obs1,array_obs2,array_obs3,array_obs4,array_obs5,array_obs6,array_obs7,array_obs8,array_obs9,array_obs10,array_obs11,array_obs12,array_obs13,array_obs14,array_obs15])
array_sim_all = np.array([array_sim1,array_sim2,array_sim3,array_sim4,array_sim5,array_sim6,array_sim7,array_sim8,array_sim9,array_sim10,array_sim11,array_sim12,array_sim13,array_sim14,array_sim15])


plt.scatter(np.nanmean(array_obs_all,axis=0),np.nanmean(array_sim_all,axis=0))

#plt.scatter(np.nanmean(well_nan_obs,axis=1),np.nanmean(well_nan_sim,axis=1))
#text_str = '\n'.join((
#'ME=%.2f' % (np.nanmean(np.nanmean(well_nan_me1,well_nan_me2,well_nan_me3,well_nan_me4,well_nan_me5,well_nan_me6,well_nan_me7,well_nan_me8,well_nan_me9,well_nan_me10,well_nan_me11)) ,),
#'MAE=%.2f' % (np.nanmean(np.nanmean(well_nan_mae1,well_nan_mae2,well_nan_mae3,well_nan_mae4,well_nan_mae5,well_nan_mae6,well_nan_mae7,well_nan_mae8,well_nan_mae9,well_nan_mae10,well_nan_mae11)) ,),
#'RMSE=%.2f' % np.nanmean(well_nan_rmse1,well_nan_rmse2,well_nan_rmse3,well_nan_rmse4,well_nan_rmse5,well_nan_rmse6,well_nan_rmse7,well_nan_rmse8,well_nan_rmse9,well_nan_rmse10,well_nan_rmse11), ))
#plt.text(-55,55, text_str, fontsize=8, verticalalignment='top')

plt.plot([-65,65],[-65,65], color='red')
plt.xlim([-65,65])
plt.ylim([-65,65])
plt.xlabel('Mean observed head (m)')
plt.ylabel('Mean simulated head (m)')
plt.savefig('mean_sim_obs_plt.png',format='png')






