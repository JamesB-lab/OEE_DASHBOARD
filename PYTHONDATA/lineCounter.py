import pandas as pd
import numpy as np
import os
from OEE29 import run_OEE_29
from OEE57 import run_OEE_57
from OEE85 import run_OEE_85


def main():

    #file = '04_03.ram' #29 lines
    file = '02_03.ram' #57 lines
    #file = '07_03.ram' #85 lines

    os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    file_exists = os.path.exists(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}')
    print(f'File Exists? {file_exists}')

    basename = os.path.basename(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}')

    basename = basename.replace('.ram', '')
    print(f'basename: {basename}')


    ###Count number of lines in the file###

    count = len(open(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\EDITS\\{file}').readlines(  ))
    count = count +1
    print(count)
    ##Import raw data as fixed width file (fwf)###
    #data = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}', skiprows=3, skipfooter=7, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])

    if count == 29:
        print('File is 29 lines long')
        run_OEE_29(file)
    elif count == 57:
        print('File is 57 lines long')
        run_OEE_57(file)
    elif count == 85:
        print('File is 85 lines long')
        run_OEE_85(file)
    else:
        print('Syntax Error file length')

main()