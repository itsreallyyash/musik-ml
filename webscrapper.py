import pandas as pd
import requests
df = pd.read_csv('yes2.csv')

def get_lyrics(artist, title):
    url = f'https://api.lyrics.ovh/v1/{artist}/{title}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'lyrics' in data:
            return data['lyrics']
        else:
            return "Lyrics not found"
    else:
        return "Error: Failed to fetch lyrics"
for index, row in df.iterrows():
    lyrics = get_lyrics(row['Artist'], row['Title'])
    df.at[index, 'Lyrics'] = lyrics
df.to_csv('modified_csv_file18.csv', index=False)