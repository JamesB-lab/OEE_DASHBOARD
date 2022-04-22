import plotly.express as px
import pandas as pd
from datetime import date


df = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalogDF.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
df = pd.DataFrame(df)

now = date.today()
print(now)

#df = px.data.stocks(indexed=True)-1
fig = px.bar(df, x=df.index, y=["Availability", "Performance", "Quality", "OEE"], barmode='group')
fig.update_traces(xperiod0=now, selector=dict(type='bar')) #Adds a marker for the current date to the graph could be x or y
fig.show() 