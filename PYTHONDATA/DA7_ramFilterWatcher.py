#Developed by James Booth M68153 for Microchip Technology 2022 #
#Github repo: https://github.com/jboothMCHP/OEE_DASHBOARD.git #
#The purpose of this architecture is to provide a complete solution for data extraction, wrangling and archiving data into MCHP SQL Servers via an ETL pipeline #
#ETL order is given at the top of the code beinging with 'PL' and increasing sequentially #
#Information is displayed via the 'OEE Dashboard' a Django based web app which pulls data from a csv file which generates up to date graphs via the plotly chart studio API #
#OEE Dashboard can be viewed at http://http://10.205.40.60/ #
#Historic information can be viewed in SSRS report at http://reporting.ax2012.microchip.com/reports/ #
#For scalability purposes code is duplicated for new machines (e.g., 'DA5','DA6' etc)#
#Program launch via cmd terminal: cd C:\vs_code\OEE_DASHBOARD\PYTHONDATA | python DA5_watcherWrapper.py #
#Server launch using port 80 (must be enabled on host PC): cd C:\vs_code\OEE_DASHBOARD\PYTHONDATA | python manage.py runserver 0.0.0.0:80 #
#Data is generated by the BESI Datacon Evos daily. Machine statistics export mode = Daily, Hour = 8, Delete machine statistics after export = On#
#The above means that data is recorded a the machine level daily and restarts its log on the 8th hour of everyday i.e. 8AM. #
#Therefore the data gathered on day 2 represents the OEE performance of day 1# 

##############################################################################################################################################################################

#PL01 for OEE Dashboard #
#ramFilterWatcher program is the first stage in the ETL pipeline. The program utilised the python packages 'watchdog' and 'os' #
#The program is event driven, it's purpose is to monitor the dedicated source folder and act upon the new data added into the folder #
#Within the RamFileHandler class valid ram lengths are set. Meaning that only .ram files that are 'genuine' are loaded. #
#The length of the .ram file increases each time a program is changed, therefore if the number of program changes per day is >4 the system will not act #
#The on_created function uses a try except to elicit from the FileSystemEventHandler class if the new file is not a directory #
#If True the program passes the file to the filterRamLengths function which filters from os.path.basename if the file extension is .ram, it also filters through our valid ram lengths #
#If invalid the file is passed to the 'unhandled' directory'. If valid the file is passed to the target directory#
#The start_ram_watch_and_copy function is the 'main' part of the program and works similar to a while loop. #
#The observer method within the function calls the handler when it detects a new file is added into the source folder #
#The handler class then copies the files from the source directory to the target direcotry if valid and to the bad directory if invalid #


import os
from watchdog.observers import Observer
from  watchdog.events import FileSystemEventHandler

def run_ramFilterWatcher():

    print('Running ramFilterWatcher.py')

    class RamFileHandler(FileSystemEventHandler):

        def __init__(self, targetDir, badDir):
            self.targetDir = targetDir
            self.badDir = badDir
            self.valid_ram_lengths = [28,29,30,55,56,57,58,59,85,86,87,88,113,114,115,116,117]



        def on_created(self, event):
        # We use try-except to avoid the service crashing if it can't do the work on the file

            try:
                print(event)
                if not event.is_directory:
                # If it is a file, then we do some work with it
                    self.filterRamFiles(event.src_path)

            except BaseException as err:
                print(err)


        def filterRamFiles(self, path):
        # If this is NOT a '*.ram' file, return early, nothing to do
            if not os.path.basename(path).endswith('.ram'):
                print(f'Skipping file {path} which is not a RAM file')
                return

            # First we read the source file lines and make a count
            with open(path,'r') as f:
                lines = f.readlines()
                count =len(lines)
            # If the count of lines is not allowed, we return early

            if not count in self.valid_ram_lengths:
                print(f'Skipping file {path} which has length {count}')
                copyFile(path, os.path.join(self.badDir, os.path.basename(path)))
                return

            # Finally we write (copy) the original lines in the target file
            copyFile(path, os.path.join(self.targetDir, os.path.basename(path)))
    
    def copyFile(source, destination):
        with open(source, 'r') as s:
            lines = s.readlines()
        with open(destination, 'w') as d:
            d.writelines(lines)
        print(f'Copied file {source} to {destination}')






    def start_ram_watch_and_copy(srcDir, targetDir, badDir):
        # Just in case, create the target parent directory if it doesn't exist already
        if not os.path.exists(targetDir):
            os.mkdir(targetDir)
        if not os.path.exists(badDir):
            os.mkdir(badDir)

    # Define our custom handler and start it

        handler = RamFileHandler(targetDir, badDir)
        observer = Observer()
        observer.schedule(handler, srcDir, recursive=True)
        observer.start()
        # This is just so the file watcher (observer) keeps looping with a small wait in between
        return observer



    # Important that we initialised here what paths we want to work with

    # the script will watch srcDir and copy valid .ram files into targetDir

    start_ram_watch_and_copy(srcDir='P:\\! Evo Stats\\DA7', targetDir='P:\\OEE_Dashboard\\DA7\\Raw_Data_Input', badDir= 'P:\\OEE_Dashboard\\DA7\\Unhandled')