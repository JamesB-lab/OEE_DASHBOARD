#Plotly Dial/Gauge for Quality for OEE Dashboard#


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


###Code is good up to here###

###Create variable for dateYesterday##
dateYesterday = date.today() - datetime.timedelta(days = 20) #20 - Needs to be adjusted every day to reach 2022-04-14 for test purposes 
print(f'Date Yesterday = {dateYesterday}')
deltaDate = dateYesterday - datetime.timedelta(days = 1)
print(f'Delta Date = {deltaDate}')

###Code is good up to here, remeber to adjust 'days' value to get real data###

###Cast Datetime as string for bool Test###
dateYesterday = str(dateYesterday)
deltaDate = str(deltaDate)
# print(dateYesterday)


###Bool test is optional to check if the data is being correctly parsed###
DateTestBool = df.Datetime == dateYesterday ##Error here must be string
#print(DateTestBool)
DeltaTestBool = df.Datetime == deltaDate ##Error here must be string
#print(DeltaTestBool)



yesterdayPlot = df.loc[df.Datetime == dateYesterday]
#print(f'yesterdayPlot = {yesterdayPlot}')
deltaPlot = df.loc[df.Datetime == deltaDate]
print(f'deltaplot = {deltaPlot}')

Qua = yesterdayPlot['Quality']
Qua = float(Qua)
# print(f'TEST: {OEE}')

Qua_Delta = deltaPlot['Quality']
Qua_Delta = float(Qua_Delta)
# # OEE_Delta = {'reference': OEE_Delta}
print(f'TEST: {Qua_Delta}')





##Plot###

import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = Qua,
    mode = "gauge+number+delta",
    title = {'text': "Quality"},
    delta = {'reference': Qua_Delta},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))

fig.show()
