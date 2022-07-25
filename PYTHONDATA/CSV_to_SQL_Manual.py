###ERROR PROGRAM DOESNT WORK###


import pandas as pd
from sqlalchemy import create_engine

rawData = pd.read_csv('P:\\OEE_Dashboard\\Data\\dl_datetime.csv')
# print(rawData)

df = pd.DataFrame(rawData)
print(df)


#SQL Connection Windows Authentication#

Server = 'UKC-VM-SQL01'
Database = 'Scorecard'
Driver = 'ODBC Driver 17 for SQL Server'
Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

engine = create_engine(Database_con)
con = engine.connect()

df.to_sql('OEELog', con, if_exists='append', index = False)

#Fin#
print('Program Complete')

###ERROR PROGRAM DOESNT WORK###
