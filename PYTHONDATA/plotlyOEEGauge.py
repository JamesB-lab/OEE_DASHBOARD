from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import plotly.graph_objects as go 
import datetime
from datetime import date


df = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv', header=0, parse_dates=True, squeeze=True, dayfirst=False)
df = pd.DataFrame(df)

df = df.drop_duplicates(subset=['Datetime', 'RamDate','Availability','Performance','Quality','OEE'], keep="first")

#Sort remaining values by datetime#
df = df.sort_values(by='Datetime', ascending=True)


###Create variable for dateYesterday##
dateYesterday = date.today() - datetime.timedelta(days = 19) #19
deltaDate = dateYesterday - datetime.timedelta(days = 1)
dateYesterday = str(dateYesterday)
deltaDate = str(deltaDate)
print(dateYesterday)

DateTestBool = df.Datetime == dateYesterday ##Error here must be string
print(DateTestBool)


print(f'Delta Date = {deltaDate}')

yesterdayPlot = df.loc[df.Datetime == dateYesterday]
print(yesterdayPlot)
deltaPlot = df.loc[df.Datetime == deltaDate]
print(f'deltaplot = {deltaPlot}')

OEE = yesterdayPlot['OEE']
OEE = float(OEE)
print(f'TYPE {type(OEE)}')

OEE_Delta = deltaPlot['OEE']
OEE_Delta = OEE_Delta.astype('float')
#OEE_Delta = {'reference': OEE_Delta}
print(f'TYPE Delta = {type(OEE_Delta)}')




###Plot###

import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = OEE,
    mode = "gauge+number+delta",
    title = {'text': "OEE"},
    delta = {'reference': 100},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))

fig.show()
