import pandas as pd
import os.path


def run_Data_Clean(path):
    print(f'Running Data_Clean on {path}')

    basename = os.path.basename(path) #ok
    print(f'basename: {basename}') #ok

    rawData = pd.read_fwf(path, colspecs=[(0,142)], names=['Col_1'],)

    df = pd.DataFrame(rawData)


    ignore = ['bmc', 'bmc       0          0          0          0']
    df = df[df.Col_1.isin(ignore) == False]

    print(f'df new = {df}')


    df.to_csv(f'P:\\OEE_Dashboard\\DA7\\Cleaned_Data_Output\\{basename}', index=False, mode='a', header=False)
    #df.to_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\{basename}', index=False, mode='a', header=False)