#Plotly Dial/Gauge for OEE for OEE Dashboard#

from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import plotly.graph_objects as go 
import datetime
from datetime import date
import chart_studio.plotly as py
import chart_studio



def run_plotly_OEE():

    print('Running Plotly OEE')

    username = 'james.booth' # your username
    api_key = 'cCmuSWNFC4GOKnshMCr2' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


    df = pd.read_csv(f'P:\\OEE_Dashboard\\Data\\datalog.csv', header=0, parse_dates=True, squeeze=True, dayfirst=False)
    df = pd.DataFrame(df)


    df = df.drop_duplicates(subset=['Datetime', 'RamDate','Availability','Performance','Quality','OEE'], keep="first")

    ###Filter by machine type###
    df = df[(df['Machine'] == 'DA6')]



    #Sort remaining values by datetime#
    df = df.sort_values(by='Datetime', ascending=True)


    ###Code is good up to here###

    ###Create Offset for Business Date###
    offset = pd.tseries.offsets.BusinessDay(n=1)

    ###Create variable for dateYesterday##
    dateYesterday = date.today() - datetime.timedelta(days =0) # Should be 1!!! #20 - Needs to be adjusted every day to reach 2022-04-14 for test purposes 
    print(f'Date Yesterday = {dateYesterday}')
    deltaDate = dateYesterday - offset
    print(f'Delta Date = {deltaDate}')

    ###Code is good up to here, remeber to adjust 'days' value to get real data###

    ###Cast Datetime as string for bool Test###
    dateYesterday = str(dateYesterday)
    deltaDate = str(deltaDate.date())
    # print(dateYesterday)


    ###Bool test is optional to check if the data is being correctly parsed###
    DateTestBool = df.Datetime == dateYesterday ##Error here must be string
    #print(DateTestBool)
    DeltaTestBool = df.Datetime == deltaDate ##Error here must be string
    #print(DeltaTestBool)



    yesterdayPlot = df.loc[df.Datetime == dateYesterday]
    print(f'YesterdayPlot =\n{yesterdayPlot}')
    #print(f'yesterdayPlot = {yesterdayPlot}')
    deltaPlot = df.loc[df.Datetime == deltaDate]
    #print(f'deltaplot = {deltaPlot}')
    print(f'deltaPlot =\n{deltaPlot}')

    ###Error check here for 0 values###

    if len(yesterdayPlot) == 0:
        OEE =0
    else:
        OEE = yesterdayPlot['OEE']
        OEE = float(OEE)
        # print(f'TEST: {OEE}')

    if len(deltaPlot) == 0:
        OEE_Delta = 0
    else:
        OEE_Delta = deltaPlot['OEE']
        OEE_Delta = float(OEE_Delta)

    # # OEE_Delta = {'reference': OEE_Delta}
    print(f'TEST: {OEE_Delta}')



    ##Plot###

    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = OEE,
        mode = "gauge+number+delta",
        title = {'text': "OEE"},
        delta = {'reference': OEE_Delta},
        gauge = {'axis': {'range': [None, 100]},
                'steps' : [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 100], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))

    #fig.write_html("PLOTLYEXPORTS\\OEEGauge.html")
    py.plot(fig, filename = 'plotlyOEEGauge', auto_open=False)

    fig.show()
