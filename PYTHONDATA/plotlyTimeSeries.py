import plotly.express as px
import pandas as pd
from datetime import date
import datetime
pd.options.display.max_rows = 3000

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
lower_date = now - datetime.timedelta(days = 15)
upper_date = now + datetime.timedelta(days = 15)
# print(now)
# print(lower_date)
# print(upper_date)

rollingDate = pd.bdate_range(start=lower_date, end=upper_date)
#Convert rollingDate into a dataframe with a single column#
rollingDate = pd.DataFrame(rollingDate, columns =['RollingDate'])


#merge for rolling date
mergedRolling = pd.merge(left=rollingDate, right = merged, how='outer', left_on='RollingDate', right_on='DateBrange')
print(mergedRolling)




# #df = px.data.stocks(indexed=True)-1
# fig = px.bar(df, x=df.index, y=["Availability", "Performance", "Quality", "OEE"], barmode='group')
# fig.update_traces(xperiod0=now, selector=dict(type='bar')) #Adds a marker for the current date to the graph could be x or y
# fig.show() 