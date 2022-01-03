

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

print(df_can.head()) # show first 5 rows of dataframe

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)   # remove unwanted columns

print(df_can.head(2))

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)   # rename columns

df_can['Total'] = df_can.sum(axis=1)    # add totals column that is a sum of all 


df_can.set_index('Country', inplace=True)  # set the 'Country' column to be the index of the dataframe
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

print(df_can.describe())
#print(df_can.head(2))

df_can.sort_values(['Total'], ascending = False, axis = 0, inplace=True)

print(df_can.head(3))