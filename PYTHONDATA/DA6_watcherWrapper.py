from DA5_ramFilterWatcher import run_ramFilterWatcher
from DA5_InputWatcher import run_inputWatcher
from DA5_cleanedDataWatcher import run_cleanedDataWatcher
import time

def __main__():

    print("Running watcher programs")

    ramFileObserver = run_ramFilterWatcher()
    inputObserver = run_inputWatcher()
    cleanedDataObserver = run_cleanedDataWatcher()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ramFileObserver.stop()
        inputObserver.stop()
        cleanedDataObserver.stop()
    ramFileObserver.join()
    inputObserver.join()
    cleanedDataObserver.join()
 
__main__()