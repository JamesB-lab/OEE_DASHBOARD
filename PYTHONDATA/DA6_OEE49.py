###OEE Calculation Tool for use in OEE Dashboard. Beta Version 1.2###
###Updated to create datetime object when logging each dataframe for easier plotting##
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 57 only###
###Last updated 25/04/2022###


from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pprint
import datetime
from datetime import date
from DA5_updatePlots import run_update_plots



def run_OEE_49(path):

    print('Running OEE49')


    basename = os.path.basename(path) #ok

    basename = basename.replace('.ram', '') #ok
    #print(f'basename: {basename}') #ok

    ##Import raw data as fixed width file (fwf)### #not ok, need to fix import drops and merge two dataframes#
    data_a = pd.read_fwf(path, skiprows=3, skipfooter=27, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    #print(f'OEE49 Data{data_a}')

    data_b = pd.read_fwf(path, skiprows=27, skipfooter=3, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    #print(f'OEE49 Data{data_b}')

    ###CONVERT data_a and data_b to dataframe. Agregate into single datafram###

    data_a = pd.DataFrame(data_a)
    data_b = pd.DataFrame(data_b)

    # print(f'OEE49: {data_a}')
    # print(f'OEE49: {data_b}')




    # ###AVAILABILITY DATA_A Convert raw data to dataFrame, subset for timedelata###
    dftd_a = pd.DataFrame(data_a)
    dftd_a = dftd_a.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    # print(f'dftd_a data: {dftd_a}')

    # ###AVAILABILITY DATA_B###
    dftd_b = pd.DataFrame(data_b)
    dftd_b = dftd_b.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    # print(f'dftd_b data: {dftd_b}')

    # ###AVAILABILITY Cast Types convert from Object to string/timedelta###
    dftd_a['Category'] = dftd_a['Category'].astype('string') #Error#
    dftd_a['System 1'] = pd.to_timedelta(dftd_a['System 1'])
    dftd_a['System 2'] = pd.to_timedelta(dftd_a['System 2'])
    #print(f'dftd_a data post cast: {dftd_a}')

    dftd_b['Category'] = dftd_b['Category'].astype('string') #Error#
    dftd_b['System 1'] = pd.to_timedelta(dftd_b['System 1'])
    dftd_b['System 2'] = pd.to_timedelta(dftd_b['System 2'])
    #print(f'dftd_b data post cast: {dftd_b}')

    # ###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
    dftd_a['System 1'] = dftd_a['System 1'] / pd.Timedelta(hours =1)
    dftd_a['System 2'] = dftd_a['System 2'] / pd.Timedelta(hours =1)

    # print(f'dftd_a {dftd_a}')
    # print(f'dftf_a type {dftd_a.dtypes}')

    dftd_b['System 1'] = dftd_b['System 1'] / pd.Timedelta(hours =1)
    dftd_b['System 2'] = dftd_b['System 2'] / pd.Timedelta(hours =1)

    # print(f'dftd_b {dftd_b}')
    # print(f'dftf_b type {dftd_b.dtypes}')

    ###AVAILABILITY OEE Availability Calcs###
    ###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

    possibleProd_a = dftd_a.loc[dftd_a.index[2], 'System 2']

    actualProd_a = dftd_a.loc[dftd_a.index[5], 'System 2']
    # print(f'possibleProd_a: {possibleProd_a}')
    # print(f'actualProd_a: {actualProd_a}')


    availability_a = actualProd_a / possibleProd_a
    #print(f'availability_a: {availability_a}')


    possibleProd_b = dftd_b.loc[dftd_b.index[2], 'System 2']

    actualProd_b = dftd_b.loc[dftd_b.index[5], 'System 2']
    # print(f'possibleProd_b: {possibleProd_b}')
    # print(f'actualProd_b: {actualProd_b}')

    availability_b = actualProd_b / possibleProd_b
    #print(f'availability_b: {availability_b}')



    ###QUALITY Subset for Quality Statistics ###

    dfq_a = pd.DataFrame(data_a)
    dfq_a = dfq_a.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(f'OEE57 dfq_a quality dataset: {dfq_a}')

    dfq_b = pd.DataFrame(data_b)
    dfq_b = dfq_b.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(f'OEE57 dfq_b quality dataset: {dfq_b}')


    ###QUALITY Cast Types convert from Object to string/int64###
    dfq_a['Category'] = dfq_a['Category'].astype('string')
    dfq_a['System 2'] = dfq_a['System 2'].astype('int')

    # print(f'dfq_a {dfq_a}')
    # print(f'dfq_a type {dfq_a.dtypes}')

    dfq_b['Category'] = dfq_b['Category'].astype('string')
    dfq_b['System 2'] = dfq_b['System 2'].astype('int')

    # print(f'dfq_b {dfq_b}')
    # print(f'dfq_b type {dfq_b.dtypes}')


    ###QUALITY OEE Quality Calcs###
    ###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

    pickup_a = dfq_a.loc[dfq_a.index[0], 'System 2']
    place_a = dfq_a.loc[dfq_a.index[1], 'System 2']
    quality_a = place_a / pickup_a

    # print(f'pickup_a {pickup_a}')
    # print(f'place_a {place_a}')
    # print(f'quality_a {quality_a}')

    pickup_b = dfq_b.loc[dfq_b.index[0], 'System 2']
    place_b = dfq_b.loc[dfq_b.index[1], 'System 2']
    quality_b = place_b / pickup_b

    # print(f'pickup_b {pickup_b}')
    # print(f'place_b {place_b}')
    # print(f'quality_b {quality_b}')

    ###PERFORMANCE Subset for Performance Statistics ###

    data2_a = pd.read_fwf(path, skiprows=23, skipfooter=24,   colspecs=[(0,13), (14,24), (25, 37), (38, 49), (50, 60), (61, 71), (72, 83), (83, 90), (91, 100), (101, 112), (112, 124), (125,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp_a = pd.DataFrame(data2_a)
    #print(f'OEE49 data2_a = {dfp_a}')
    #print(f">>>{dfp_a.loc[dfp_a.index[0], 'AM-Err1']}<<<")

    data2_b = pd.read_fwf(path, skiprows=47, skipfooter=0,   colspecs=[(0,13), (14,24), (25, 37), (38, 49), (50, 60), (61, 71), (72, 83), (83, 90), (91, 100), (101, 112), (112, 124), (125,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp_b = pd.DataFrame(data2_b)
    # print(f'OEE49 data2_b = {dfp_b}')
    # print(f">>>{dfp_b.loc[dfp_b.index[0], 'InspErr']}<<<")

    ###PERFORMANCE OEE Quality Calcs###


    actualOut_a = dfp_a.loc[dfp_a.index[0], 'Total']
    actualOut_a = int(actualOut_a)
    PossibleOut = 7010
    #print(f'Actual Out: {actualOut_a}')
    #print(type(actualOut_a))



    performance_a = actualOut_a / PossibleOut #error
    #print(f'Performance_a: {performance_a}')

    actualOut_b = dfp_b.loc[dfp_a.index[0], 'Total']
    actualOut_b = int(actualOut_b)
    #print(f'Actual Out: {actualOut_b}')
    #print(type(actualOut_b))

    performance_b = actualOut_b / PossibleOut #error
    #print(f'Performance_b: {performance_b}')


    ###MERGE Dataframe_a & Dataframe_b###
    ###FIX THIS MATHS ERROR###

    availability = (actualProd_a + actualProd_b) / (possibleProd_a + possibleProd_b)
    #print(f'overall availability {availability}')

    quality = (place_a + place_b) / (pickup_a + pickup_b)
    #print(f'overall quality {quality}')

    performance = (actualOut_a + actualOut_b) / (PossibleOut + PossibleOut)
    #print(f'overall performance {performance}')





    ###FINAL OEE CACLULATION###

    OEE = availability * performance * quality * 100

    print(f'Availbability = {availability}')
    print(f'Performance = {performance}')
    print(f'Quality = {quality}')
    print(f'OEE = {OEE} %')



    ###Save Results to csv###

    ###Create DataFrame of the results: availability, performance, quality, OEE###
    ramYear = str(datetime.datetime.now().year)
    date_text = basename.replace('_','/')
    date_text = date_text.replace('.RAM','') + '/' + ramYear
    date_time = pd.to_datetime(date_text, format='%d/%m/%Y').date()
    # print(f' Date_Text = {date_text}')
    # print(f' Date_Time = {date_time}')

    dict = {'Datetime': date_time, 'RamDate': basename, 'Availability': availability*100, 'Performance': performance*100, 'Quality': quality*100, 'OEE': OEE, 'Machine': 'DA5'}


    resultsDF = pd.DataFrame.from_dict(dict, orient='index')
    resultsTransp = resultsDF.transpose()


    ###Write to csv###

    resultsTransp.to_csv(r'P:\\OEE_Dashboard\\Data\\datalog.csv', index=False, mode='a', header=False)



    print('OEE49 program complete')
    print('Updating plots')
    run_update_plots()