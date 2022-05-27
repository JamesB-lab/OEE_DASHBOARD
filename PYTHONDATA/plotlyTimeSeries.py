import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import date
import datetime
pd.options.display.max_rows = 3000
import chart_studio.plotly as py
import chart_studio


def run_plotly_TimeSeries():


    username = 'james.booth' # your username
    api_key = 'cCmuSWNFC4GOKnshMCr2' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


    #pd.set_option("display.max_rows", None, "display.max_columns", None)


    #Read raw data from csv, parse dates and make datetime begin with day first, finally convert to dataframe#
    df = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv', header=0, parse_dates=True, squeeze=True, dayfirst=True)
    df = pd.DataFrame(df)
    # print(df)
    # print(df.shape)
    #Drop duplicates from the csv file leaving the original input data#
    df = df.drop_duplicates(subset=['Datetime', 'RamDate','Availability','Performance','Quality','OEE'], keep="first")
    # print(f'df shape: {df.shape}')
    # print(f'pre sorted dates: {df}')
    #Sort remaining values by datetime#
    df = df.sort_values(by='Datetime', ascending=True)
    # print(f'post sorted dates: {df}')
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    #Creat business date range (brange)#
    currentYear = str(datetime.datetime.now().year)
    start_date = datetime.datetime(day=3, month=1, year=2022)
    end_date = datetime.datetime(day=27, month=12, year=2030) #may need to be adjusted currently arbitray high value#
    brange = pd.bdate_range(start=start_date, end=end_date)
    #Convert brange into a dataframe with a single column#
    brange = pd.DataFrame(brange, columns =['DateBrange'])
    # print(f'brange shape: {brange.shape}')

    # print(f"df[Datetime] = {df['Datetime'].dtypes}")
    # print(f"brannge[DateBrange] = {brange['DateBrange'].dtypes}")


    #Merge df with brange on outer pandas join#
    merged = pd.merge(left=brange, right = df, how='outer', left_on='DateBrange', right_on='Datetime')
    print(f'merged shape = {merged.shape}')
    #print(merged)


    #Subset for rolling date range#

    now = date.today()
    lower_date = now - datetime.timedelta(days = 30)
    upper_date = now + datetime.timedelta(days = 15)
    # print(now)
    # print(lower_date)
    # print(upper_date)

    rollingDate = pd.bdate_range(start=lower_date, end=upper_date)
    #Convert rollingDate into a dataframe with a single column#
    rollingDate = pd.DataFrame(rollingDate, columns =['RollingDate'])


    #merge for rolling date, use inner join to only plot within the rolling date range#
    mergedRolling = pd.merge(left=rollingDate, right = merged, how='inner', left_on='RollingDate', right_on='DateBrange')


    ##Apply fillna() to OEE column##7

    mergedRolling['OEE'] = mergedRolling['OEE'].fillna(0)
    print(mergedRolling)


    #df = px.data.stocks(indexed=True)-1
    fig = px.bar(mergedRolling, x=mergedRolling['RollingDate'], y=["Availability", "Performance", "Quality"], barmode='group')
    fig.update_layout(xaxis_tickformat = '%d/%m/%Y')
    #xaxis=dict(tickvals=mergedRolling['RollingDate'], title='Deliveries by Vehicle', titlefont=dict(family='Courier New, monospace', size=18, color='#7f7f7f'),type='category')
    fig.update_xaxes(tickangle= -90, nticks = 50, tickfont_size=10)

    fig.update_traces(xperiod0=now, selector=dict(type='bar')) #Adds a marker for the current date to the graph could be x or y


    fig.add_trace(
        go.Scatter(
            x=mergedRolling['RollingDate'],
            y=mergedRolling['OEE'],
            name='OEE',
            line_shape='hvh'
        ))

    fig.update_layout(
        #title=f"Datacon Evo [DA5] 2200+ OEE Trend {lower_date} to {upper_date}",
        xaxis_title="Date",
        yaxis_title="%",
        legend_title="Legend |",
        font=dict(
            family="Helvetica",
            size=18,
            color="Black"
        )
    )

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ))

    fig.add_vline(x=now, line_width=3, line_dash="dash", line_color="green")

    py.plot(fig, filename = 'plotlyTimeSeries', auto_open=True)


    fig.show() 