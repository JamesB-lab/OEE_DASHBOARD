import pandas as pd
import os.path


file = '09_05.ram'

basename = os.path.basename(file) #ok
print(f'basename: {basename}') #ok

rawData = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\BMCDROPTEST\\{file}', colspecs=[(0,142)], names=['Col_1'],)

df = pd.DataFrame(rawData)


ignore = ['bmc', 'bmc       0          0          0          0          0          0          0          0          0          0          0']
df = df[df.Col_1.isin(ignore) == False]

print(f'df new = {df}')


df.to_csv(f'P:\\OEE_Dashboard\\Cleaned_Data_Output\\{basename}', index=False, mode='a', header=False)
#df.to_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\{basename}', index=False, mode='a', header=False)
