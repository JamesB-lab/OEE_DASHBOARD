import plotly.express as px
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
#from datetime import datetime

#To do: create a function that will read the basename from datalog.csv and convert to date-time
#To do: join dataframes on the date-time column

datalog = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalog.csv')
# print(datalog)

df = pd.DataFrame(datalog)
print(f'df shape: {df.shape}')

df = df.drop_duplicates(subset=['Date','Availability','Performance','Quality','OEE'], keep="first")
print(df)
print(f'df shape: {df.shape}')

ramYear = str(datetime.datetime.now().year)
# Create Business Date Ranges #
start_date = datetime.datetime(day=25, month=2, year=2022)
end_date = datetime.datetime(day=5, month=4, year=2022)
brange = pd.bdate_range(start=start_date, end=end_date)
brange = pd.DataFrame(brange, columns =['DateBrange'])
print(f'brange shape: {brange.shape}')


date_text = df['Date'].replace('_','/', regex=True) + '/' + ramYear
df['Datetime'] = pd.to_datetime(date_text, format='%d/%m/%Y')
#df['Date_brange'] = df['Datetime'].dt.strftime('%Y-%m-%d').astype('string') #string type
#print(df)
# print(df.dtypes)

##Sort Dataframe by Date##
df = df.sort_values(by='Datetime', ascending=True)
#print(df)

#print(brange.dtypes)
#print(df.dtypes)


result = pd.merge(left=brange, right = df, how='outer', left_on='DateBrange', right_on='Datetime')
#print(result)
#print(result.to_markdown())
#print(result.to_string())

print(result)
print(result.shape)

###Write to csv###

#result.to_csv(r'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalogDF.csv', index=False, mode='a', header=True)



###Plot Sandbox###
# Availability = [0.1, 17.5, 40, 48, 52, 69, 88]
# Performance = [2, 8, 70, 1.5, 25, 12, 28]
# Quality = [90, 89, 88, 89, 91, 99, 95]
# index = ['04/04/22', '05/04/22', '06/04/22',
#          '07/04/22', '08/04/22', '11/04/22', '12/04/22']
# df = pd.DataFrame({'Availability': Availability,
#                    'Performance': Performance,
#                    'Quality': Quality}, index=index)
# ax = df.plot.bar(rot=0)
# ax = df.plot.bar(stacked=True)

# plt.show()


series = pd.read_csv(f'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\datalogDF.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
series.plot.bar(rot=90, stacked =True)

###A failed experiment###
# N = len(result['Datetime'])
# print(f' N = {N}')
# Availability = result['Availability']
# Performance = result['Performance']
# Quality = result['Quality']
# index = result['Datetime']
# ind = np.arange(N)
# dfp = pd.DataFrame({'Availability': Availability,
#                    'Performance': Performance,
#                    'Quality': Quality}, index=index)
# #ax = dfp.plot.bar(rot=0)
# ax = dfp.plot.bar(Availability, rot=30, stacked=False)

#plt.xticks(index)




###Subplots, kinda cool but not what I'm looking for##
# axes = df.plot.bar(rot=0, subplots=True)
# axes[1].legend(loc=2)


plt.show()







# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#                 print(result)

                       






####Concatinate Dataframes###

# result = pd.concat([df, bDate], axis=1)
# print(result)


# result = pd.concat([df, bDate], axis=1, join="inner")
# print(result)

# result = pd.concat([df, bDate], axis=1, ignore_index=True, sort=False)
# print(result)


# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df)

#fmt = '%d %b %Y at %H:%M'



#fig = px.bar(df, x="Date", y= "OEE", title="OEE Historical")
#fig = px.bar(df, x="Date", y= "OEE", color="Availability", title="OEE Historical")
#fig.show()
