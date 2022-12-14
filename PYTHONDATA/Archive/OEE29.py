###OEE Calculation Tool for use in OEE Dashboard. Beta Version 1.2###
###Updated to create datetime object when logging each dataframe for easier plotting##
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 29 only###
###Last updated 26/04/2022###


from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pprint
import datetime
from datetime import date

print('OEE29')

def run_OEE_29(path):

    #path = 'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\PRECLEAN\\20_05.ram'
    # file = '11_03.ram'

    # os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    # file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')
    # print(f'File Exists? {file_exists}')

    basename = os.path.basename(path)

    basename = basename.replace('.ram', '')
    print(f'basename: {basename}')

    ##Import raw data as fixed width file (fwf)###
    data = pd.read_fwf(path, skiprows=3, skipfooter=6, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
    print(f'OEE29 Data{data}')

    ###AVAILABILITY Convert raw data to dataFrame, subset for timedelata###
    dftd = pd.DataFrame(data)
    dftd = dftd.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
    print(f'OEE29 dftd data: {dftd}')

    ###AVAILABILITY Cast Types convert from Object to string/timedelta###
    dftd['Category'] = dftd['Category'].astype('string') #Error#
    dftd['System 1'] = pd.to_timedelta(dftd['System 1'])
    dftd['System 2'] = pd.to_timedelta(dftd['System 2'])
    print(f'OEE29 dftd data post cast: {dftd}')

    ###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
    dftd['System 1'] = dftd['System 1'] / pd.Timedelta(hours =1)
    dftd['System 2'] = dftd['System 2'] / pd.Timedelta(hours =1)

    print(f'OEE29 dftd: {dftd}')
    print(f'OEE29 dftd dtypes: {dftd.dtypes}')

    ###AVAILABILITY OEE Availability Calcs###
    ###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

    possibleProd = dftd.loc[dftd.index[2], 'System 2']


    actualProd = dftd.loc[dftd.index[5], 'System 2']


    availability = actualProd / possibleProd
    print(f'OEE29 possibleProd = {possibleProd}')
    print(f'OEE29 actualProd = {actualProd}')
    print(f'OEE29 availability = {availability}')



    ###QUALITY Subset for Quality Statistics ###

    dfq = pd.DataFrame(data)
    print(f'OEE29 rawdataframe: {dfq}')
    dfq = dfq.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print(f'OEE29 dfq dataset: {dfq}')


    ###QUALITY Cast Types convert from Object to string/int64###
    dfq['Category'] = dfq['Category'].astype('string')
    dfq['System 2'] = dfq['System 2'].astype('int')



    ###QUALITY OEE Quality Calcs###
    ###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

    pickup = dfq.loc[dfq.index[0], 'System 2']
    place = dfq.loc[dfq.index[1], 'System 2']

    quality = place / pickup
    print(f'OEE29 pickup = {pickup}')
    print(f'OEE29 place = {place}')
    print(f'OEE29 quality = {quality}')

    ###PERFORMANCE Subset for Performance Statistics ###

    data2 = pd.read_fwf(path, skiprows=24, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
    dfp = pd.DataFrame(data2)
    print(f'OEE29 data2 = {data2}')



    ###PERFORMANCE OEE Quality Calcs###


    actualOut = dfp.loc[dfp.index[1], 'Total']
    actualOut = int(actualOut)
    PossibleOut = 7010
    # print(f'Actual Out: {actualOut}')
    # print(type(actualOut))



    performance = actualOut / PossibleOut #error



    ###FINAL OEE CACLULATION###

    OEE = availability * performance * quality * 100

    # print(f'Availbability = {availability}')
    # print(f'Performance = {performance}')
    # print(f'Quality = {quality}')
    # print(f'OEE = {OEE} %')



    ###Save Results to csv###

    ###Create DataFrame of the results: availability, performance, quality, OEE###
    ramYear = str(datetime.datetime.now().year)
    date_text = basename.replace('_','/')
    date_text = date_text.replace('.RAM','') + '/' + ramYear
    date_time = pd.to_datetime(date_text, format='%d/%m/%Y').date()
    # print(f' Date_Text = {date_text}')
    # print(f' Date_Time = {date_time}')

    dict = {'Datetime': date_time, 'RamDate': basename, 'Availability': availability*100, 'Performance': performance*100, 'Quality': quality*100, 'OEE': OEE}


    resultsDF = pd.DataFrame.from_dict(dict, orient='index')
    resultsTransp = resultsDF.transpose()


    ###Write to csv###

    resultsTransp.to_csv(r'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv', index=False, mode='a', header=False)





