from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import chart_studio.tools as tls
import os
from pathlib import Path



os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
file_exists = os.path.exists('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\11_03.ram')
print(f'File Exists? {file_exists}')



##Import raw data as fixed width file (fwf)###
data = pd.read_fwf('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\11_03.ram', skiprows=3, skipfooter=7, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
print(f'data 11_02.ram: {data}')


###AVAILABILITY Convert raw data to dataFrame, subset for timedelata###
dftd = pd.DataFrame(data)
dftd = dftd.drop(axis=0, index =[9,10,11, 12, 13, 14, 15, 16, 17])
# print(dftd)
# print(dftd.dtypes)

###AVAILABILITY Cast Types convert from Object to string/timedelta###
dftd['Category'] = dftd['Category'].astype('string')
dftd['System 1'] = pd.to_timedelta(dftd['System 1'])
dftd['System 2'] = pd.to_timedelta(dftd['System 2'])

###AVAILABILITY Add extra column for plotting, convert timedelata to float64###
dftd['System 1'] = dftd['System 1'] / pd.Timedelta(hours =1)
dftd['System 2'] = dftd['System 2'] / pd.Timedelta(hours =1)

# print(dftd)
# print(dftd.dtypes)

###AVAILABILITY OEE Availability Calcs###
###AVAILABILITY Availability = Actual Production Time / Possible Production Time * 100###

possibleProd = dftd.loc[dftd.index[2], 'System 2']

actualProd = dftd.loc[dftd.index[5], 'System 2']


availability = actualProd / possibleProd




###QUALITY Subset for Quality Statistics ###

dfq = pd.DataFrame(data)
dfq = dfq.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])



###QUALITY Cast Types convert from Object to string/int64###
dfq['Category'] = dfq['Category'].astype('string')
dfq['System 2'] = dfq['System 2'].astype('int')



###QUALITY OEE Quality Calcs###
###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

pickup = dfq.loc[dfq.index[0], 'System 2']
place = dfq.loc[dfq.index[1], 'System 2']


quality = place / pickup


###PERFORMANCE Subset for Performance Statistics ###

data2 = pd.read_fwf('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\11_03.ram', skiprows=25, skipfooter=0,   colspecs=[(1,23), (25,33), (36, 45), (47, 56), (57, 65), (65, 76), (76, 87), (87, 98), (98, 109), (109, 120), (120, 131), (131,-1)], names=['ComponentStatistics', 'Total', 'Useable', 'Reject', 'Inked', 'Pos-Error', 'Vac-Error', 'AM-Err1', 'AM-Err2', 'AM-Err3', 'AM-Err4', 'InspErr' ])
dfp = pd.DataFrame(data2)



###PERFORMANCE OEE Quality Calcs###


actualOut = dfp.loc[dfp.index[1], 'Total']
PossibleOut = 840


performance = actualOut / PossibleOut


###FINAL OEE CACLULATION###

OEE = availability * performance * quality * 100
availability1 = availability * 100
performance1 = performance * 100
quality1 = quality * 100

print(f'Availbability = {availability}')
print(f'Performance = {performance}')
print(f'Quality = {quality}')
print(f'OEE = {OEE} %')





####################################################

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "indicator"}, {"type": "indicator"}],
           [{"type": "indicator"}, {"type": "indicator"}]],
)

fig.add_trace(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = OEE,
    mode = "gauge+number+delta",
    title = {'text': "Datacon Evo Overall Equipment Effectiveness"},
    delta = {'reference': 40},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 33], 'color': "gray"},
                 {'range': [33, 65], 'color': "darkgray"},
                 {'range': [65, 100], 'color': "lightgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}),
             row=1, col=1)

fig.add_trace(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = availability1,
    mode = "gauge+number+delta",
    title = {'text': "Datacon Evo Availability"},
    delta = {'reference': 65},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 33], 'color': "gray"},
                 {'range': [33, 65], 'color': "darkgray"},
                 {'range': [65, 100], 'color': "lightgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}),
             row=1, col=2)

fig.add_trace(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = performance1,
    mode = "gauge+number+delta",
    title = {'text': "Datacon Evo Performance"},
    delta = {'reference': 65},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 33], 'color': "gray"},
                 {'range': [33, 65], 'color': "darkgray"},
                 {'range': [65, 100], 'color': "lightgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}),
             row=2, col=1)

fig.add_trace(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = quality1,
    mode = "gauge+number+delta",
    title = {'text': "Datacon Evo Quality"},
    delta = {'reference': 95},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 33], 'color': "gray"},
                 {'range': [33, 65], 'color': "darkgray"},
                 {'range': [65, 100], 'color': "lightgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}),
             row=2, col=2)

fig.update_layout(height=700, showlegend=False)

fig.write_html('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\OEE_DASHBOARD\\PLOTLYEXPORTS\\test.html')
 
fig.show()










