import datetime
import pandas as pd

dateTime = str(datetime.datetime.today())
print(dateTime)

dateDict = {'Data': dateTime}

df = pd.DataFrame(dateDict, index=[0])
print(df)

# df.to_csv(index=False)

#Fix this'

df.to_csv(r'C:\\vs_code\\OEE_DASHBOARD\\DATABASE\\testy.csv', index=False, mode='a', header=False)


