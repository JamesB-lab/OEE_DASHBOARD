import pandas as pd
import sqlite3



data = {
        'Production Order':['PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135', 'PDWO80023135'],
        'Item Number':['ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL', 'ZL70675BAL'], 
        'Batch':[39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240, 39240], 
        'Operation Number':[10,60,70,100,125,128,130,135,140,160,180,190,240,290,300,320,325,330,340,350,360], 
        'Operation ID and Data Collection':['ISSUE001', 'BAKE001', 'SMT_FT_Kit', 'SMT_FT_Reflow', 'SMT_BK_Kitting', 'SMT_BK_Reflow', 'WASH001_2', 'WASH001', 'INSP001', 'BAKE001_2', 'UFIL003_Canary Underfill Front', 'UFIL004_Canary Underfill Back', 'Underfill Inspection Canary', 'Routing', 'TEST001', 'Canary Burn In', 'INST001_2', 'TEST001_2', 'Final Insp_003', 'INST001_3', 'PACK001'], 
        'Date Time Started':['31 May 2022 at 21:29', '31 May 2022 at 21:30', '01 Jun 2022 at 13:31', '01 Jun 2022 at 13:31', '01 Jun 2022 at 16:26', '01 Jun 2022 at 16:27', '01 Jun 2022 at 17:07', '01 Jun 2022 at 21:34', '06 Jun 2022 at 12:30', '06 Jun 2022 at 12:38', '07 Jun 2022 at 10:09', '07 Jun 2022 at 12:43', '08 Jun 2022 at 08:21', '08 Jun 2022 at 18:05', '09 Jun 2022 at 08:24', '10 Jun 2022 at 11:22', '13 Jun 2022 at 11:26', '14 Jun 2022 at 12:32', '14 Jun 2022 at 19:06', '15 Jun 2022 at 08:39', '15 Jun 2022 at 08:39'], 
        'Date Time Finished':['31 May 2022 at 21:30', '31 May 2022 at 22:36', '01 Jun 2022 at 13:31', '01 Jun 2022 at 13:53', '01 Jun 2022 at 16:27', '01 Jun 2022 at 17:07', '01 Jun 2022 at 21:34', '01 Jun 2022 at 22:01', '06 Jun 2022 at 12:37', '06 Jun 2022 at 13:08', '07 Jun 2022 at 11:18', '07 Jun 2022 at 13:12', '08 Jun 2022 at 08:58', '08 Jun 2022 at 19:00', '09 Jun 2022 at 14:08', '13 Jun 2022 at 11:26', '13 Jun 2022 at 11:27', '14 Jun 2022 at 17:05', '14 Jun 2022 at 19:18', '15 Jun 2022 at 08:39', '15 Jun 2022 at 08:45' ], 
        'Time Taken (mins)':[1,66,0,22,1,40,267,27,7,30,69,29,37,55,344,4324,1,273,12,0,6], 
        'Qty Scheduled':[53,53,53,53,53,53,53,53,53,53,53,53,53,53,47,47,47,46,46,46,46], 
        'Qty Started':[53,53,53,53,53,53,53,53,53,53,53,53,53,53,47,47,47,46,46,46,46], 
        'Qty Good':[53,53,53,53,53,53,53,53,53,53,53,53,53,47,47,47,47,46,46,46,46], 
        'Qty Error':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,1,0,0,0], 
        'Yield %':[100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,88.6,100.0,100.0,97.87,100.0,100.0,100.0], 
        'Operator':['Martin Greenlaugh', 'Martin Greenlaugh', 'Ceriann Williams', 'Ceriann Williams', 'Paul Jones', 'Paul Jones', 'Paul Jones', 'Paul Jones', 'Sue Jefferies', 'Sue Jefferies', 'Mark Bisset', 'Mark Bisset', 'Joanne Parsley', 'Ian Maclauclan', 'Gina Beacham', 'Danielle Morgan', 'Danielle Morgan', 'Jason Weed', 'Alison Baker', 'Saul Taylor', 'Saul Taylor'], 
        'Scanner ID':['LM01','OV20','SMT_K01','SP1','PP1','IR4','SMT_K02','SP1','PP1','IR4','C2','C2','INS_01','OV20','UFF_01','UFF_02','UFB_01','UFB_02','UF_INSP','INS_02','NaN'], 
        'Station':['LM01','OV20','SMT_K01','SP1','PP1','IR4','SMT_K02','SP1','PP1','IR4','C2','C2','INS_01','OV20','UFF_01','UFF_02','UFB_01','UFB_02','UF_INSP','INS_02','NaN'], 
        'Time Between Stations':[1,66,0,22,1,40,267,27,7,30,69,29,37,55,344,4324,1,273,12,0,6],
        'Cum Cycle Time':[1,67,67,89,90,130,397,404,411,441,510,539,576,631,975,5299,5300,5573,5585,5585,5591],
        }

# print(len(data['Station']))

# for key, value in data:
#         print(key, value)


df = pd.DataFrame(data, columns=['Production Order', 'Item Number', 'Batch', 'Operation Number', 'Operation ID and Data Collection', 'Data Time Started', 'Date Time Finished', 'Time Taken (mins)', 'Qty Scheduled', 'Qty Started', 'Qty Good', 'Qty Error', 'Yield %', 'Operator', 'Scanner ID', 'Station', 'Time Between Stations', 'Cum Cycle Time'])
print(df)


conn = sqlite3.connect('P:\\OEE_Dashboard\\SQL\\WIPLite')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS wipLIGHT ('Production Order', 'Item Number', 'Batch', 'Operation Number', 'Operation ID and Data Collection', 'Data Time Started', 'Date Time Finished', 'Time Taken (mins)', 'Qty Scheduled', 'Qty Started', 'Qty Good', 'Qty Error', 'Yield %', 'Operator', 'Scanner ID', 'Station', 'Time Between Stations', 'Cum Cycle Time')")
conn.commit()
df.to_sql('wipLIGHT', conn, if_exists='replace', index = False)

print('Database Created')