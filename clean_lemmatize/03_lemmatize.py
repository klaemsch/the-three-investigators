import pandas as pd
from HanTa import HanoverTagger as ht
import os

# Initialize tagger
tagger = ht.HanoverTagger('morphmodel_ger.pgz')

# Ensure the lemmatized_csv directory exists
os.makedirs('clean_lemmatize/lemmatized_csv', exist_ok=True)

# Process all CSV files in the 'stopwords_csv' folder
for filename in os.listdir('clean_lemmatize/stopwords_csv'):
    if filename.endswith('.csv'):
        filepath = os.path.join('clean_lemmatize/stopwords_csv', filename)
        df = pd.read_csv(filepath)

        # Function to lemmatize text
        def lemmatize_text(text):
            if pd.isna(text):
                return text
            try:
                lemma = [lemma for (word, lemma, pos) in tagger.tag_sent(text.split())]
                return ' '.join(lemma)
            except:
                return text

        # Apply lemmatization to Text column
        df['Text'] = df['Text'].apply(lemmatize_text)

        # Save the lemmatized CSV
        output_filename = os.path.join('clean_lemmatize/lemmatized_csv', 'lemmatized_' + filename)
        df.to_csv(output_filename, index=False)
        print(f"Lemmatisierung abgeschlossen. Datei gespeichert: {output_filename}")