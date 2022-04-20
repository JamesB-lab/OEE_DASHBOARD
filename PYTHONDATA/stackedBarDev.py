import plotly.express as px
import pandas as pd
import datetime
#from datetime import datetime

#To do: create a function that will read the basename from datalog.csv and convert to date-time
#To do: join dataframes on the date-time column

datalog = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv')
# print(datalog)

df = pd.DataFrame(datalog)

df = df.drop_duplicates(subset=['Date','Availability','Performance','Quality','OEE'], keep=False)
# print(df)
# print(df.shape)

bDate = pd.bdate_range(start='3/1/2022', end='3/31/2022') #business date range March 2022#
bDate.columns = ['bDate']
bDate = pd.DataFrame(bDate)
# print(bDate)



ramYear = str(datetime.datetime.now().year)

date_text = df['Date'].replace('_','/', regex=True) + '/' + ramYear
df['Datetime'] = pd.to_datetime(date_text, format='%d/%m/%Y')
df['Date_brange'] = df['Datetime'].dt.strftime('%Y-%m-%d').astype('string') #string type
#print(df)
# print(df.dtypes)

##Sort Dataframe by Date##
df = df.sort_values(by='Datetime', ascending=True)
#print(df)


####Concatinate Dataframes###

# result = pd.concat([df, bDate], axis=1)
# print(result)


# result = pd.concat([df, bDate], axis=1, join="inner")
# print(result)

# result = pd.concat([df, bDate], axis=1, ignore_index=True, sort=False)
# print(result)

result = pd.merge(df, bDate, how="left", on=["bDate"])
print(result)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df)

#fmt = '%d %b %Y at %H:%M'



#fig = px.bar(df, x="Date", y= "OEE", title="OEE Historical")
#fig = px.bar(df, x="Date", y= "OEE", color="Availability", title="OEE Historical")
#fig.show()
