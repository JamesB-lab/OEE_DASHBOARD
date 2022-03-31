import plotly.express as px
import pandas as pd



datalog = pd.read_csv(f'C:\\Users\\M68153\\OneDrive - Microchip Technology Inc\\Desktop\\OEE_DASHBOARD\\DATABASE\\datalog.csv')
print(datalog)


fig = px.bar(datalog, x="Date", y= "OEE", color="Availability", title="OEE Historical")
fig.show()