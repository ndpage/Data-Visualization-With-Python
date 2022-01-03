
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import excel

stopwords = set(STOPWORDS)

df_can = excel.read_data('Canada.xlsx')

total_immigration = df_can['Total'].sum()

max_words = 90
word_string = ''
for country in df_can.index.values:
    # check if country's name is a single-word name
    if country.count(" ") == 0:
        repeat_num_times = int(df_can.loc[country, 'Total'] / total_immigration * max_words)
        word_string = word_string + ((country + ' ') * repeat_num_times)

# display the generated text
wordcloud = WordCloud(background_color='white').generate(word_string)

# display the cloud
plt.figure(figsize=(14, 12))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()