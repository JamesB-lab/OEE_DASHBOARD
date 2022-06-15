###OEE Datalogger Tool for use in OEE Dashboard. Beta Version 1.3###
###Updated to include file parsing for RAM files of length 113##
###Developed by James Booth###
###For parsing Datacon Evo FWF files of line length 113 only###
###Last updated 07/06/2022###

import imp
import pandas as pd
import numpy as np
import os
from OEE25 import run_OEE_25
from OEE29 import run_OEE_29
from OEE57 import run_OEE_57
from OEE85 import run_OEE_85
from OEE113 import run_OEE_113
from OEE49 import run_OEE_49
from OEE73 import run_OEE_73
from OEE97 import run_OEE_97


def run_line_counter(path):

    #file = '04_03.ram' #29 lines
    #file = '02_03.ram' #57 lines
    #file = '07_03.ram' #85 lines
    #file = file

    os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
    file_exists = os.path.exists(path)
    print(f'File Exists? {path}')

    basename = os.path.basename(path)

    basename = basename.replace('.ram', '')
    print(f'basename: {basename}')


    ###Count number of lines in the file###

    count = len(open(path).readlines(  ))
    count = count +1
    print(count)
    ##Import raw data as fixed width file (fwf)###
    #data = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\RAMFILES\\keeps\\{file}', skiprows=3, skipfooter=7, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])

    if count == 25:
        print('File is 25 lines long')
        run_OEE_25(path)
    elif count == 49:
        print('File is 49 lines long')
        run_OEE_49(path)
    elif count == 73:
        print('File is 73 lines long')
        run_OEE_73(path)
    elif count == 97:
        print('File is 97 lines long')
        run_OEE_97(path)
    else:
        print('Syntax Error file length')

# if __name__ == '__main__':
#     run_line_counter('07_03.ram')

#run_line_counter()