import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import data_ingest.excel_data as excel_data

df_can = excel_data.read_data('../Canada.xlsx')

print(df_can.head())

years = list(map(str, range(1980,2014)))

df_can.sort_values(['Total'], ascending = False, axis = 0, inplace=True)  # sort the data frame from highest to lowest number of immigrants

df_top5 = df_can.head()

df_top5 = df_top5[years].transpose() # transpose swaps the rows and columns

### Area Plot ###

# df_top5.plot(kind='area')

# plt.title("Tope 5 Countries")
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')

# #plt.show()

# ### Histogram ### 
# year = '1995'
# count, bin_edges = np.histogram(df_can[year])
# df_can[year].plot(kind='hist',xticks=bin_edges)

# plt.title(f"Histogram of immigrants from 195 countries in {year}")

# #plt.show()

### Bar chart ### 
country = 'United States of America'
df_can.loc[country,years].plot(kind='bar')

plt.title(F"Bar chart of {country}")
plt.ylabel("Number of Immigrants")
plt.xlabel("Years")
plt.show()