import os

path = 'P:\\OEE_Dashboard\\DA5\\Raw_Data_Input'
print(f'Testing Path {path}')

pathExists = os.path.exists(path)
print(f'Does the path exist? {pathExists}')