import pandas as pd
import re
import os

# Load stopwords from TXT file
with open('clean_lemmatize/ext_stopwords-de.txt', 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# Create a set of lowercase stopwords for case-insensitive matching
stopwords_lower = set(stop.lower() for stop in stopwords)

# Ensure the stopwords_csv directory exists
os.makedirs('clean_lemmatize/stopwords_csv', exist_ok=True)

# Process all CSV files in the 'clean_lemmatize/cleaned_csv' folder
for filename in os.listdir('clean_lemmatize/cleaned_csv'):
    if filename.endswith('.csv'):
        filepath = os.path.join('clean_lemmatize/cleaned_csv', filename)
        df = pd.read_csv(filepath)

        # Function to remove stopwords from text
        def remove_stopwords(text):
            if pd.isna(text):
                return text
            words = text.split()
            filtered_words = [word for word in words if word.lower() not in stopwords_lower]
            return ' '.join(filtered_words)

        # Apply the function to the text column
        df['Text'] = df['Text'].apply(remove_stopwords)

        # Save the updated CSV
        output_filename = os.path.join('clean_lemmatize/stopwords_csv', 'stopwords_' + filename)
        df.to_csv(output_filename, index=False)