
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import excel    # Imports custom function for reading Canada.xlsx file and processing the data into a Pandas Dataframe


df_can = excel.read_data('C:/Users/pag1fni/Documents/Learning/Data Visualization with Python/Canada.xlsx')

years = list(map(str, range(1980,2014)))

### type your answer here
df_dsn = df_can.loc[['Denmark','Sweden','Norway'],years]

df_tot = pd.DataFrame(df_dsn[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)


# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
print(df_tot.head())

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('whitegrid')

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()
