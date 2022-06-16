from ramFilterWatcher import run_ramFilterWatcher
from InputWatcher import run_inputWatcher
from cleanedDataWatcher import run_cleanedDataWatcher

def __main__():

    print("Running watcher program")
    run_ramFilterWatcher()
    run_inputWatcher()
    run_cleanedDataWatcher()
    

__main__()