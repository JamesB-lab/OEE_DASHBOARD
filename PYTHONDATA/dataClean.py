from ast import If
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
from datetime import date


file = '22_03.ram'

# rawData = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\BMCDROPTEST\\{file}', colspecs=[(1,23), (25,33)], names=['Col_1', 'Col_2'])
#print(rawData)

rawData = pd.read_fwf(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\DA5_Copy\\BMCDROPTEST\\{file}', colspecs=[(1,23), (25,33)], names=['Col_1', 'Col_2'])


df = pd.DataFrame(rawData)
# print(df)
# print(df.shape)


# print(df.index)

# for label in df.index:
#     print(f'\'{label}\'')

ignore = ['bmc']
#df = df[df.Col_1.isin(ignore) == False]


df = df[df.Col_1.isin(ignore) == False]


# for i in range(len(df)) :
# #   print(df.iloc[i, 0])
#   if df.iloc[i, 0] == 'bmc':
#      print('True')
#      #df = df[df.Col_1.isin(ignore) == False]
#       #df = df.drop(df.loc['bmc', 0], axis=0, index=0)
#       #df = df.drop(df.loc[df['Col_1']=='bmc'].index, inplace=True)
#       #df = df.drop('bmc')
    


print(f'df new = {df}')

#df.to_csv(r'c:\data\pandas.txt', header=None, index=None, sep=' ', mode='a')
df.to_csv(r'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\cleaning.txt', index=False, mode='a', header=False)