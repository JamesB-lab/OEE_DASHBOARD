###OEE Datalogger Tool for use in OEE Dashboard. Beta Version 1.3###
###Updated to include file parsing for RAM files of length 113##
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 113 only###
###Last updated 07/06/2022###

import pandas as pd
import numpy as np
import os
from OEE29 import run_OEE_29
from OEE57 import run_OEE_57
from OEE85 import run_OEE_85
from OEE113 import run_OEE_113


def run_line_counter(file):

    #file = '04_03.ram' #29 lines
    #file = '02_03.ram' #57 lines
    #file = '07_03.ram' #85 lines
    #file = file

    os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    file_exists = os.path.exists(file)
    print(f'File Exists? {file}')

    basename = os.path.basename(file)

    basename = basename.replace('.ram', '')
    print(f'basename: {basename}')


    ###Count number of lines in the file###

    count = len(open(file).readlines(  ))
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
    elif count == 113:
        print('File is 113 lines long')
        run_OEE_113(file)
    else:
        print('Syntax Error file length')

if __name__ == '__main__':
    run_line_counter('07_03.ram')

#run_line_counter()