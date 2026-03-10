import pandas as pd
import os
import re

# Ensure the clean_lemmatize/cleaned_csv directory exists
os.makedirs('clean_lemmatize/cleaned_csv', exist_ok=True)

# Process CSV files 001 to 010
for i in range(1, 11):
    filename = f'{i:03d}.csv'
    filepath = os.path.join('csv', filename)
    
    # Check if file exists
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)

        # Print out the first rows of df (only for the first file to avoid clutter)
        if i == 1:
            print(df.head())

        # Remove punctuation (everything except word characters and whitespace)
        df['Text'] = df['Text'].map(
            lambda x: re.sub(r"[^\w\s]", "", x) if pd.notna(x) else x
        )

        # Convert to lowercase
        df['Text'] = df['Text'].map(lambda x: x.lower() if pd.notna(x) else x)

        # Print out the first rows of processed text (only for the first file)
        if i == 1:
            print(df['Text'].head())

        # Save the processed CSV
        output_filename = os.path.join('clean_lemmatize/cleaned_csv', 'cleaned_' + filename)
        df.to_csv(output_filename, index=False)
        print(f"Bereinigung abgeschlossen. Datei gespeichert: {output_filename}")