###OEE Calculation Tool for use in OEE Dashboard. Alpha Version 0.1###
###Developed by James Booth###
###Current limit on file types, must be: .RAM, length 30, include bmc step & name of program must not exceed 21 characters###
###Last updated 16/03/202###


from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pprint
from datetime import date


file = '11_03.ram'

os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')
print(f'File Exists? {file_exists}')

basename = os.path.basename(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')

basename = basename.replace('.ram', '')
print(f'basename: {basename}')

##Import raw data as fixed width file (fwf)###
data = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}', skiprows=3, skipfooter=7, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])


###AVAILABILITY Convert raw data to dataFrame, subset for timedelata###
dftd = pd.DataFrame(data)
dftd = dftd.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])


###AVAILABILITY Cast Types convert from Object to string/timedelta###
dftd['Category'] = dftd['Category'].astype('string')
dftd['System 1'] = pd.to_timedelta(dftd['System 1'])
dftd['System 2'] = pd.to_timedelta(dftd['System 2'])

###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
dftd['System 1'] = dftd['System 1'] / pd.Timedelta(hours =1)
dftd['System 2'] = dftd['System 2'] / pd.Timedelta(hours =1)

# print(dftd)
# print(dftd.dtypes)

###AVAILABILITY OEE Availability Calcs###
###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

possibleProd = dftd.loc[dftd.index[2], 'System 2']


actualProd = dftd.loc[dftd.index[5], 'System 2']


availability = actualProd / possibleProd




###QUALITY Subset for Quality Statistics ###

dfq = pd.DataFrame(data)
dfq = dfq.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])



###QUALITY Cast Types convert from Object to string/int64###
dfq['Category'] = dfq['Category'].astype('string')
dfq['System 2'] = dfq['System 2'].astype('int')



###QUALITY OEE Quality Calcs###
###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

pickup = dfq.loc[dfq.index[0], 'System 2']
place = dfq.loc[dfq.index[1], 'System 2']


quality = place / pickup


###PERFORMANCE Subset for Performance Statistics ###

data2 = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}', skiprows=25, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
dfp = pd.DataFrame(data2)
print(f'DFP: {dfp}')



###PERFORMANCE OEE Quality Calcs###


actualOut = dfp.loc[dfp.index[1], 'Total']
PossibleOut = 840
print(f'Actual Out: {actualOut}')



performance = actualOut / PossibleOut



###FINAL OEE CACLULATION###

OEE = availability * performance * quality * 100

print(f'Availbability = {availability}')
print(f'Performance = {performance}')
print(f'Quality = {quality}')
print(f'OEE = {OEE} %')



###Save Results to csv###

###Create DataFrame of the results: availability, performance, quality, OEE###

today = date.today()

# dd/mm/YY
dateCurrent = today.strftime("%d/%m/%Y")


dict = {'Date': basename, 'Availability': availability*100, 'Performance': performance*100, 'Quality': quality*100, 'OEE': OEE}


resultsDF = pd.DataFrame.from_dict(dict, orient='index')



resultsTransp = resultsDF.transpose()


###Write to csv###

resultsTransp.to_csv(r'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\OEE_DASHBOARD\\DATABASE\\datalog.csv', index=False, mode='a', header=False)





