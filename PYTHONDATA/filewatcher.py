import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


'''
To customise how to handle file system events, we just need to defined this tiny class that
inherits from FileSystemEventHandler and overrides the method 'on_created'
In this case I also redefine the '__init__' method so that we can store a custom value
'completedDir'
so that we can use it inside the method
'''


class MyEventHandler (FileSystemEventHandler):
    def __init__(self, completedDir):
        self.completedDir = completedDir

    # In this case we only care about 'created' events
    def on_created(self, event):
        # We use try-except to avoid the service crashing if it can't do the work on the file
        try:
            print(event)
            if not event.is_directory:
                # If it is a file, then we do some work with it
                doSomeWorkWithCreatedFile(event.src_path, self.completedDir)
        except BaseException as err:
            print(err)


def doSomeWorkWithCreatedFile(path, completedDir):
    # This would be some more interesting work, like read an OEE file and store the logs
    with open(path, 'r') as f:
        contents = f.read()
        print(contents)
    # Move it to the completed directory once done
    os.rename(path, os.path.join(completedDir, os.path.basename(path)))


def main(srcDir, completedDir):
    # Just in case, create the completed directory if it doesn't exist already
    if not os.path.exists(completedDir):
        os.mkdir(completedDir)
    # Define our custom handler and start it
    my_handler = MyEventHandler(completedDir)
    observer = Observer()
    observer.schedule(my_handler, srcDir, recursive=True)
    observer.start()
    # This is just so the file watcher (observer) keeps looping with a small wait in between
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    # Important that we initialised here what paths we want to work with
    main(srcDir='./data', completedDir='./completed')