import data_ingest.excel_data as excel_data
import matplotlib as mpl
import matplotlib.pyplot as plt

# Read data from excel sheet (see excel_data.py)
df_can = excel_data.read_data('../Canada.xlsx')

years = list(map(str, range(1980,2014)))
df_can.sort_values(['Total'], ascending = False, axis = 0, inplace=True)  # sort the data frame from highest to lowest number of immigrants

# get top 5 by total immigrants
df_top5 = df_can.head()
df_top5 = df_top5[years].transpose() # transpose swaps the rows and columns

# let's change the index values of df_top5 to type integer for plotting
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='line',
            stacked=False,
            figsize=(15, 8))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()