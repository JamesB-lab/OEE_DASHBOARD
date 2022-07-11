import pandas as pd
import sqlite3



data = {'Datetime': ['02/03/2022','03/03/2022','04/03/2022','05/03/2022'],
        'RamDate': ['02_03','03_03','04_03','05_03'], 'Availability': [40.7542, 24.83845, 17.9525, 0], 'Performance': [2.17546, 1.747504, 5.734655, 0.014265], 'Quality': [99.2292, 100, 100, 0], 'OEE': [0.879777, 0.434053, 1.0, 0], 'Machine': ['SQLTEST','SQLTEST','SQLTEST','SQLTEST']
        }

df = pd.DataFrame(data, columns=['Datetime', 'RamDate', 'Availability', 'Performance', 'Quality', 'OEE', 'Machine'])
print(df)


conn = sqlite3.connect('P:\\OEE_Dashboard\\SQL\\testDB')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS oeeTest ('Datetime', 'RamDate', 'Availability', 'Performance', 'Quality', 'OEE', 'Machine')")
conn.commit()
df.to_sql('oeeTest', conn, if_exists='replace', index = False)