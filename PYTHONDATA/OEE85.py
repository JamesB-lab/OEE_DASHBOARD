###OEE Calculation Tool for use in OEE Dashboard. Alpha Version 0.2###
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 85 only###
###Last updated 16/03/202###


from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pprint
from datetime import date

print('opened function file')

def run_OEE_85(file):


    # file = '11_03.ram'

    # os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    # file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')
    # print(f'File Exists? {file_exists}')

    basename = os.path.basename(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}') #ok

    basename = basename.replace('.ram', '') #ok
    print(f'basename: {basename}') #ok

    ##Import raw data as fixed width file (fwf)### #not ok, need to fix import drops and merge two dataframes#
    data_a = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=3, skipfooter=61, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    # print(f'OEE85 Data{data_a}')

    data_b = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=31, skipfooter=33, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    # print(f'OEE85 Data{data_b}')

    data_c = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=59, skipfooter=6, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    #print(f'OEE85 Data{data_c}')
    
    ###CONVERT data_a and data_b to dataframe. Agregate into single datafram###

    data_a = pd.DataFrame(data_a)
    data_b = pd.DataFrame(data_b)
    data_c = pd.DataFrame(data_c)

    # print(data_a)
    # print(data_b)
    # print(data_c)

    


    ###AVAILABILITY DATA_A Convert raw data to dataFrame, subset for timedelata###
    dftd_a = pd.DataFrame(data_a)
    dftd_a = dftd_a.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    #print(f'dftd_a data: {dftd_a}')

    # ###AVAILABILITY DATA_B###
    dftd_b = pd.DataFrame(data_b)
    dftd_b = dftd_b.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    #print(f'dftd_b data: {dftd_b}')

    # ###AVAILABILITY DATA_C###
    dftd_c = pd.DataFrame(data_c)
    dftd_c = dftd_c.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    #print(f'dftd_c data: {dftd_c}')

    ###AVAILABILITY Cast Types convert from Object to string/timedelta###
    dftd_a['Category'] = dftd_a['Category'].astype('string') #Error#
    dftd_a['System 1'] = pd.to_timedelta(dftd_a['System 1'])
    dftd_a['System 2'] = pd.to_timedelta(dftd_a['System 2'])
    #print(f'dftd_a data post cast: {dftd_a}')

    dftd_b['Category'] = dftd_b['Category'].astype('string') #Error#
    dftd_b['System 1'] = pd.to_timedelta(dftd_b['System 1'])
    dftd_b['System 2'] = pd.to_timedelta(dftd_b['System 2'])
    #print(f'dftd_b data post cast: {dftd_b}')

    dftd_c['Category'] = dftd_c['Category'].astype('string') #Error#
    dftd_c['System 1'] = pd.to_timedelta(dftd_c['System 1'])
    dftd_c['System 2'] = pd.to_timedelta(dftd_c['System 2'])
    #print(f'dftd_c data post cast: {dftd_c}')

    ###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
    dftd_a['System 1'] = dftd_a['System 1'] / pd.Timedelta(hours =1)
    dftd_a['System 2'] = dftd_a['System 2'] / pd.Timedelta(hours =1)

    # print(f'dftd_a {dftd_a}')
    # print(f'dftf_a type {dftd_a.dtypes}')

    dftd_b['System 1'] = dftd_b['System 1'] / pd.Timedelta(hours =1)
    dftd_b['System 2'] = dftd_b['System 2'] / pd.Timedelta(hours =1)

    # print(f'dftd_b {dftd_b}')
    # print(f'dftf_b type {dftd_b.dtypes}')

    dftd_c['System 1'] = dftd_c['System 1'] / pd.Timedelta(hours =1)
    dftd_c['System 2'] = dftd_c['System 2'] / pd.Timedelta(hours =1)

    # print(f'dftd_c {dftd_c}')
    # print(f'dftf_c type {dftd_c.dtypes}')

    ###AVAILABILITY OEE Availability Calcs###
    ###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

    possibleProd_a = dftd_a.loc[dftd_a.index[2], 'System 2']

    actualProd_a = dftd_a.loc[dftd_a.index[5], 'System 2']
    #print(f'possibleProd_a: {possibleProd_a}')
    #print(f'actualProd_a: {actualProd_a}')


    availability_a = actualProd_a / possibleProd_a
    #print(f'availability_a: {availability_a}')


    possibleProd_b = dftd_b.loc[dftd_b.index[2], 'System 2']

    actualProd_b = dftd_b.loc[dftd_b.index[5], 'System 2']
    #print(f'possibleProd_b: {possibleProd_b}')
    #print(f'actualProd_b: {actualProd_b}')

    availability_b = actualProd_b / possibleProd_b
    #print(f'availability_b: {availability_b}')

    possibleProd_c = dftd_c.loc[dftd_c.index[2], 'System 2']

    actualProd_c = dftd_c.loc[dftd_c.index[5], 'System 2']
    #print(f'possibleProd_c: {possibleProd_c}')
    #print(f'actualProd_c: {actualProd_c}')

    availability_c = actualProd_c / possibleProd_c
    #print(f'availability_c: {availability_c}')



    ###QUALITY Subset for Quality Statistics ###

    dfq_a = pd.DataFrame(data_a)
    dfq_a = dfq_a.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(f'OEE85 dfq_a quality dataset: {dfq_a}')

    dfq_b = pd.DataFrame(data_b)
    dfq_b = dfq_b.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(f'OEE85 dfq_b quality dataset: {dfq_b}')

    dfq_c = pd.DataFrame(data_c)
    dfq_c = dfq_c.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(f'OEE85 dfq_c quality dataset: {dfq_c}')


    ###QUALITY Cast Types convert from Object to string/int64###
    dfq_a['Category'] = dfq_a['Category'].astype('string')
    dfq_a['System 2'] = dfq_a['System 2'].astype('int')

    #print(f'dfq_a {dfq_a}')
    #print(f'dfq_a type {dfq_a.dtypes}')

    dfq_b['Category'] = dfq_b['Category'].astype('string')
    dfq_b['System 2'] = dfq_b['System 2'].astype('int')

    #print(f'dfq_b {dfq_b}')
    #print(f'dfq_b type {dfq_b.dtypes}')


    dfq_c['Category'] = dfq_c['Category'].astype('string')
    dfq_c['System 2'] = dfq_c['System 2'].astype('int')

    #print(f'dfq_c {dfq_c}')
    #print(f'dfq_c type {dfq_c.dtypes}')

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
    quality_b = place_b / pickup_b #potential issue if div/0

    # print(f'pickup_b {pickup_b}')
    # print(f'place_b {place_b}')
    # print(f'quality_b {quality_b}')

    pickup_c = dfq_c.loc[dfq_c.index[0], 'System 2']
    place_c = dfq_c.loc[dfq_c.index[1], 'System 2']
    quality_c = place_c / pickup_c #potential issue if div/0

    # print(f'pickup_c {pickup_c}')
    # print(f'place_c {place_c}')
    # print(f'quality_c {quality_c}')

    ###PERFORMANCE Subset for Performance Statistics ###

    data2_a = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=25, skipfooter=56,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp_a = pd.DataFrame(data2_a)
    # print(f'{dfp_a}')

    data2_b = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=53, skipfooter=28,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp_b = pd.DataFrame(data2_b)
    # print(f'{dfp_b}')

    data2_c = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=81, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp_c = pd.DataFrame(data2_c)
    # print(f'{dfp_c}')

    ###PERFORMANCE OEE Quality Calcs###


    actualOut_a = dfp_a.loc[dfp_a.index[0], 'Total']
    actualOut_a = int(actualOut_a)
    PossibleOut = 840
    # print(f'Actual Out: {actualOut_a}')
    # print(type(actualOut_a))

    performance_a = actualOut_a / PossibleOut #error
    #print(f'Performance_a: {performance_a}')

    actualOut_b = dfp_b.loc[dfp_a.index[0], 'Total']
    actualOut_b = int(actualOut_b)
    # print(f'Actual Out: {actualOut_b}')
    # print(type(actualOut_b))

    performance_b = actualOut_b / PossibleOut #error
    # print(f'Performance_b: {performance_b}')

    actualOut_c = dfp_c.loc[dfp_c.index[0], 'Total']
    actualOut_c = int(actualOut_c)
    #print(f'Actual Out: {actualOut_c}')
    #print(type(actualOut_c))

    performance_c = actualOut_c / PossibleOut #error
    #print(f'Performance_c: {performance_c}')


    ###MERGE Dataframe_a & Dataframe_b###
    
    availability = (actualProd_a + actualProd_b + actualProd_c) / (possibleProd_a + possibleProd_b + possibleProd_c)
    #print(f'overall availability {availability}')

    quality = (place_a + place_b + place_c) / (pickup_a + pickup_b + pickup_c)
    #print(f'overall quality {quality}')

    performance = (actualOut_a + actualOut_b + actualOut_c) / (PossibleOut + PossibleOut + PossibleOut)
    #print(f'overall performance {performance}')





    ###FINAL OEE CACLULATION###

    OEE = availability * performance * quality * 100

    print(f'Availbability = {availability}')
    print(f'Performance = {performance}')
    print(f'Quality = {quality}')
    print(f'OEE = {OEE} %')



    # ###Save Results to csv###

    # ###Create DataFrame of the results: availability, performance, quality, OEE###

    # today = date.today()

    # # dd/mm/YY
    # dateCurrent = today.strftime("%d/%m/%Y")


    # dict = {'Date': basename, 'Availability': availability*100, 'Performance': performance*100, 'Quality': quality*100, 'OEE': OEE}


    # resultsDF = pd.DataFrame.from_dict(dict, orient='index')



    # resultsTransp = resultsDF.transpose()


    # ###Write to csv###

    # resultsTransp.to_csv(r'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv', index=False, mode='a', header=False)





