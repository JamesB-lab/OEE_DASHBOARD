import plotly.express as px
import pandas as pd

#To do: create a function that will read the basename from datalog.csv and convert to date-time
#To do: join dataframes on the date-time column

datalog = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv')
# print(datalog)

df = pd.DataFrame(datalog)

df = df.drop_duplicates(subset=['Date','Availability','Performance','Quality','OEE'], keep=False)
print(df)
print(df.shape)

bDate = pd.bdate_range(start='3/1/2022', end='3/31/2022') #business date range March 2022#
print(bDate)


#fig = px.bar(df, x="Date", y= "OEE", title="OEE Historical")
#fig = px.bar(df, x="Date", y= "OEE", color="Availability", title="OEE Historical")
#fig.show()