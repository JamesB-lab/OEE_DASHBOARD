###Test Environment for bmc/0 value drop for performance stats###


from ast import If
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path

from datetime import date


file = '11_03.ram'

os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')
print(f'File Exists? {file_exists}')

basename = os.path.basename(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}')

basename = basename.replace('.ram', '')
print(f'basename: {basename}')


###PERFORMANCE Subset for Performance Statistics ###

data2 = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}', skiprows=25, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
dfp = pd.DataFrame(data2)
print(f'DFP: {dfp}')

bmcValue = dfp.loc[dfp.index[0], 'ComponentStatistics']
print(f' BMC Value = {bmcValue}')

if bmcValue == 'bmc':
    print(True)
    dfp = dfp.drop(axis=0, index =[0])

print(f'DFP: {dfp}')

