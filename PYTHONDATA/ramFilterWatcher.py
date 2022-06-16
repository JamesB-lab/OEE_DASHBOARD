import time
import os
from watchdog.observers import Observer
from  watchdog.events import FileSystemEventHandler

class RamFileHandler(FileSystemEventHandler):

    def __init__(self, targetDir):
        self.targetDir = targetDir
        self.valid_ram_lengths = [29,30,57,58,59,85,86,87,88,113,114,115,116,117]



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
            return

        # Finally we write (copy) the original lines in the target file

        copiedFile = os.path.join(self.targetDir, os.path.basename(path))
        with open(copiedFile,'w') as f:
            f.writelines(lines)
        print(f'Copied file{path}')



def start_ram_watch_and_copy(srcDir, targetDir):
    # Just in case, create the target parent directory if it doesn't exist already
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)

# Define our custom handler and start it

    handler = RamFileHandler(targetDir)
    observer = Observer()
    observer.schedule(handler, srcDir, recursive=True)
    observer.start()
    # This is just so the file watcher (observer) keeps looping with a small wait in between
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()



# Important that we initialised here what paths we want to work with

# the script will watch srcDir and copy valid .ram files into targetDir

start_ram_watch_and_copy(srcDir='P:\\! Evo Stats\\DA5', targetDir='P:\\OEE_Dashboard\\Raw_Data_Input')