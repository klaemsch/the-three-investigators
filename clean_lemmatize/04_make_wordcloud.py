import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from collections import Counter

# Combine text from all cleaned CSV files in clean_lemmatize/lemmatized_csv
long_string = ''
for filename in os.listdir('clean_lemmatize/lemmatized_csv'):
    if filename.endswith('.csv'):
        filepath = os.path.join('clean_lemmatize/lemmatized_csv', filename)
        papers = pd.read_csv(filepath)
        long_string += ' '.join(papers['Text'].dropna().astype(str).values) + ' '

# Calculate word frequencies
words = long_string.split()
word_counts = Counter(words)
top_words = word_counts.most_common(50)

print("Top 50 Wörter:")
for word, count in top_words:
    print(f"{word}: {count}")

# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')

# Generate a word cloud
wordcloud.generate(long_string)

# Save the word cloud as image
wordcloud.to_file('clean_lemmatize/wordcloud_all.png')


