import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from DA7_dataClean import run_Data_Clean

def run_inputWatcher():

    print('Running inputWatcher.py')

    def run_Data_Clean_Trigger(path):
        print(f'Running dataClean on {path}')
        run_Data_Clean(path)



    class JamesEventHandler(FileSystemEventHandler):
    # We're only interested in created events, so we only need to implement this method
        def on_created(self, event):
    # In general, there's no guarantee that the file will be good since it's user input
    # Hence, we protect ourselves with a try-except block
            try:
                if event.is_directory == False:
                    print(f'Running DataCean Trigger on {path}')
                    run_Data_Clean_Trigger(event.src_path)
                    # print('True')
                    # print(event)
            except BaseException as err:
                print(err)


    
    path = 'P:\\OEE_Dashboard\\DA7\\Raw_Data_Input'
    # We create a new instance of our custom handler
    event_handler = JamesEventHandler()
    # We create a new watchdog observer
    observer = Observer()
    # We tell the observer to watch a 'path' recursively and use the 'event_handler'
    observer.schedule(event_handler, path, recursive=True)
    # We start the observer
    observer.start()
    return observer