###OEE Calculation Tool for use in OEE Dashboard. Alpha Version 0.2###
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 57 only###
###Last updated 16/03/202###


from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pprint
from datetime import date

print('opened function file')

def run_OEE_57(file):


    # file = '11_03.ram'

    # os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    # file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')
    # print(f'File Exists? {file_exists}')

    basename = os.path.basename(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}') #ok

    basename = basename.replace('.ram', '') #ok
    print(f'basename: {basename}') #ok

    ##Import raw data as fixed width file (fwf)### #not ok, need to fix import drops and merge two dataframes#
    data_a = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=3, skipfooter=34, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    #print(f'OEE57 Data{data_a}')

    data_b = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=31, skipfooter=6, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    # print(f'OEE57 Data{data_b}')

    ###CONVERT data_a and data_b to dataframe. Agregate into single datafram###

    data_a = pd.DataFrame(data_a)
    data_b = pd.DataFrame(data_b)

    print(data_a)
    print(data_b)

    # data_a = data_a.add(data_b, fill_value=0)
    # print(f'summed datframe {data_a}')


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
    print(f'dftd_a data post cast: {dftd_a}')

    dftd_b['Category'] = dftd_b['Category'].astype('string') #Error#
    dftd_b['System 1'] = pd.to_timedelta(dftd_b['System 1'])
    dftd_b['System 2'] = pd.to_timedelta(dftd_b['System 2'])
    print(f'dftd_b data post cast: {dftd_b}')

    # ###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
    dftd_a['System 1'] = dftd_a['System 1'] / pd.Timedelta(hours =1)
    dftd_a['System 2'] = dftd_a['System 2'] / pd.Timedelta(hours =1)

    print(f'dftd_a {dftd_a}')
    print(f'dftf_a type {dftd_a.dtypes}')

    dftd_b['System 1'] = dftd_b['System 1'] / pd.Timedelta(hours =1)
    dftd_b['System 2'] = dftd_b['System 2'] / pd.Timedelta(hours =1)

    print(f'dftd_b {dftd_b}')
    print(f'dftf_b type {dftd_b.dtypes}')

    ###AVAILABILITY OEE Availability Calcs###
    ###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

    possibleProd_a = dftd_a.loc[dftd_a.index[2], 'System 2']

    actualProd_a = dftd_a.loc[dftd_a.index[5], 'System 2']
    print(f'possibleProd_a: {possibleProd_a}')
    print(f'actualProd_a: {actualProd_a}')


    availability_a = actualProd_a / possibleProd_a
    print(f'availability_a: {availability_a}')


    possibleProd_b = dftd_b.loc[dftd_b.index[2], 'System 2']

    actualProd_b = dftd_b.loc[dftd_b.index[5], 'System 2']
    print(f'possibleProd_b: {possibleProd_b}')
    print(f'actualProd_b: {actualProd_b}')


    availability_b = actualProd_b / possibleProd_b
    print(f'availability_b: {availability_b}')



    # ###QUALITY Subset for Quality Statistics ###

    # dfq = pd.DataFrame(data)
    # # print(f'OEE29 rawdataframe: {dfq}')
    # dfq = dfq.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    # # print(f'OEE29 dfq dataset: {dfq}')


    # ###QUALITY Cast Types convert from Object to string/int64###
    # dfq['Category'] = dfq['Category'].astype('string')
    # dfq['System 2'] = dfq['System 2'].astype('int')



    # ###QUALITY OEE Quality Calcs###
    # ###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

    # pickup = dfq.loc[dfq.index[0], 'System 2']
    # place = dfq.loc[dfq.index[1], 'System 2']


    # quality = place / pickup


    # ###PERFORMANCE Subset for Performance Statistics ###

    # data2 = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}', skiprows=24, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    # dfp = pd.DataFrame(data2)



    # ###PERFORMANCE OEE Quality Calcs###


    # actualOut = dfp.loc[dfp.index[1], 'Total']
    # actualOut = int(actualOut)
    # PossibleOut = 840
    # print(f'Actual Out: {actualOut}')
    # print(type(actualOut))



    # performance = actualOut / PossibleOut #error



    # ###FINAL OEE CACLULATION###

    # OEE = availability * performance * quality * 100

    # print(f'Availbability = {availability}')
    # print(f'Performance = {performance}')
    # print(f'Quality = {quality}')
    # print(f'OEE = {OEE} %')



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





