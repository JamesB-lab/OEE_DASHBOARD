import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from lineCounter import run_line_counter

def run_cleanedDataWatcher():

    print('Running cleanedDataWatcher.py')

    def run_line_counter_Trigger(path):
        print(f'Running lineCounter on {path}')
        run_line_counter(path)



    class JamesEventHandler(FileSystemEventHandler):
    # We're only interested in created events, so we only need to implement this method
        def on_created(self, event):
    # In general, there's no guarantee that the file will be good since it's user input
    # Hence, we protect ourselves with a try-except block
            try:
                if event.is_directory == False:
                    run_line_counter_Trigger(event.src_path)
                    # print('True')
                    # print(event)
            except BaseException as err:
                print(err)


    
    path = 'P:\\OEE_Dashboard\\Cleaned_Data_Output'
    # We create a new instance of our custom handler
    event_handler = JamesEventHandler()
    # We create a new watchdog observer
    observer = Observer()
    # We tell the observer to watch a 'path' recursively and use the 'event_handler'
    observer.schedule(event_handler, path, recursive=True)
    # We start the observer
    observer.start()
    return observer