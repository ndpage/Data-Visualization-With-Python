import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

def read_data(data):
    #excel_data = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    if len(data) == 0: return 0
    excel_data = data
    data_frm = pd.read_excel(
        excel_data,
        sheet_name='Canada by Citizenship',
        skiprows=range(20),
        skipfooter=2
        )

    # in pandas axis=0 represents rows (default) and axis=1 represents columns.
    data_frm.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)   # remove unwanted columns
   
    data_frm.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)   # rename columns
   
    data_frm['Total'] = data_frm.sum(axis=1)    # add totals column that is a sum of all 
   
    data_frm.set_index('Country', inplace=True)  # set the 'Country' column to be the index of the dataframe
    # tip: The opposite of set is reset. So to reset the index, we can use data_frm.reset_index()

    data_frm.columns = list(map(str, data_frm.columns)) # Must convert years columns to strings from integers to use the ['index'] style index

    return data_frm
    