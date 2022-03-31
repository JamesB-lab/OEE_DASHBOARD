from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import plotly.graph_objects as go 


#os.path.join( "C:", "meshes", "as" ) #Add to future versions for correct method
file_exists = os.path.exists('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\11_02.ram')
print(file_exists)


###Import raw data as fixed width file (fwf)###
data = pd.read_fwf('C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\Coding\\evo_log_data\\11_02.ram', skiprows=3, skipfooter=8, colspecs=[(0,23), (23,37), (37,-1)], names=['Category', 'System 1', 'System 2'])
# print(data)

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
print(possibleProd)

actualProd = dftd.loc[dftd.index[5], 'System 2']
print(actualProd)

availability = actualProd / possibleProd
print(f'Availability = {availability}')



###QUALITY Subset for Quality Statistics ###

dfq = pd.DataFrame(data)
dfq = dfq.drop(axis=0, index =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dfq)


###QUALITY Cast Types convert from Object to string/int64###
dfq['Category'] = dfq['Category'].astype('string')
dfq['System 2'] = dfq['System 2'].astype('int')
print(dfq.dtypes)


###QUALITY OEE Quality Calcs###
###QUALITY Quality = Good Count/Total Count * 100 == Placed/Picked#

pickup = dfq.loc[dfq.index[0], 'System 2']
place = dfq.loc[dfq.index[1], 'System 2']
print(pickup,place)

quality = place / pickup
print(f'Quality = {quality}')

###PERFORMANCE Subset for Performance Statistics ###

dfp = pd.DataFrame(data)
dfp = dfp = dfp.drop(axis=0, index =[0,1,2,3,4,5,6,7,8, 12, 13, 14, 15, 16, 17])
print(dfp)

###PERFORMANCE Cast Types convert from Object to string###
dfp['Category'] = dfp['Category'].astype('string')
dfp['System 2'] = dfp['System 2'].astype('string')
print(dfp)
print(dfp.dtypes)

###PERFORMANCE Remove % & Convert string to float###
s = dfp.loc[dfp.index[2], 'System 2']
print(s)
f = float(s.replace("%",""))
print(f)


###PERFORMANCE OEE Quality Calcs###
###PERFORMANCE Performance = Actual Output/Possible Output * 100 == Total Utilisation/100#

actualOut = f
PossibleOut = 100

performance = actualOut / PossibleOut
print( f'Performance = {performance}')


###FINAL OEE CACLULATION###

#OEE = availability * performance * quality * 100

OEE =  0.14 * 100

print(f'Availbability = {availability} %')
print(f'Performance = {performance} %')
print(f'Quality = {quality} %')
print(f'OEE = {OEE} %')




fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = OEE,
    mode = "gauge+number+delta",
    # title = {'text': "Datacon Evo Overall Equipment Effectiveness"},
    delta = {'reference': 41},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 40], 'color': "lightgray"},
                 {'range': [40, 60], 'color': "gray"},],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))


fig.update_layout(
    title={
        # 'text': "<b>Datacon Evo Overall Equipment Effectiveness</b>",
        'y':0.9,
        'x':0.15,
        'xanchor': 'center',
        'yanchor': 'top'},
    gauge={
        'color':"size", 
        'color_continuous_scale': 'Inferno'}    
    )



fig.show()











# productive = df.loc[df.index[5], 'System 2']
# print(productive)

# performance = productive / availability * 100
# print(f'Performance {performance}')


###Plot data###
# ax = df.plot.barh(x = 'Category', y = ['System 1', 'System 2'], title = 'Hours per operation on Datacon Evo DA 5 in past 3 months Oct-Jan', color = ['coral', 'lightsteelblue'])
# ax.set_xlabel("Machine Operation")
# ax.set_ylabel("Hours")
# plt.show()



# print(df.loc[5]['System 2'])

###OEE###
###OEE = Availability x Performance x Quality ### and/or RunTime/TotalTime x Actual Speed/Possible Speed x Ideal Output/Actual Output ###
### 8 hours per shift - 1 for breaks. 2 shifts. Total Possible Productive hours per day = 14 || 840 hrs per 3 month###

# availability = /840

# performance = 

# quality = 

# oee = availability*performance*quality


###Test code for reading column headings###
# for col in df.columns:
#       print(f'col_test: {col}')



