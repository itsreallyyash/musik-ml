import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('final_with_sentiment.csv')

# Define the mapping of genres to simplified categories
genre_mapping = {
    'Alternative': 'Alternative',
    'Hip-Hop/Rap': 'Hip-Hop',
    'Soundtrack': 'Alternative',
    'Pop': 'Pop',
    'Hip-Hop': 'Hip-Hop',
    'Electronic': 'Electronic',
    'Downtempo': 'Electronic',
    'R&B/Soul': 'R&B/Soul',
    'Old School Rap': 'Hip-Hop',
    'Dance': 'R&B/Soul',
    'Jazz': 'Alternative',
    'Rock': 'Alternative',
    'Soul': 'R&B/Soul',
    'Rap': 'Hip-Hop',
    'Indian Pop': 'Pop',
    'Indie Pop': 'Pop',
    'Easy Listening': 'Alternative',
    'Punjabi Pop': 'Pop',
    'Bluegrass': 'Alternative',
    'Hard Rock': 'Alternative',
    'Singer/Songwriter': None,
    'Christian': 'R&B/Soul',
    'Alternative Rap': 'Hip-Hop',
    'Holiday': None,
    'North African': None,
    'Country': 'Alternative',
    'Comedy': None,
    'Afro-fusion': 'Electronic',
    'Vocal': 'R&B/Soul',
    'Christian Rap': 'Hip-Hop',
    'Swing': None,
    'Pop Latino': 'Pop',
    'Reggae': 'Alternative',
    'Instrumental': 'Electronic',
    'Bollywood': None,
    'Blues': 'R&B/Soul',
}

# Apply the mapping to the 'genre' column
df['genre'] = df['genre'].map(genre_mapping)

# Remove rows where 'genre' is None
df = df.dropna(subset=['genre'])

# Save the updated DataFrame to a new CSV file
df.to_csv('penultimate.csv', index=False)
