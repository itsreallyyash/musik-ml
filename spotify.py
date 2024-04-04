import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

client_id = ''
client_secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
songs_df = pd.read_csv('output.csv')

audio_features_list = []

for index, row in songs_df.iterrows():
    artist = row['Artist']
    title = row['Track ID']
    
    results = sp.search(q=f'track:{title} artist:{artist}', type='track', limit=1)
    
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        
        retries = 3
        while retries > 0:
            try:
                audio_features = sp.audio_features([track_id])
                break
            except spotipy.SpotifyException as e:
                if e.http_status == 429:
                    print("Rate limit exceeded. Waiting for 10 seconds...")
                    time.sleep(10)
                    retries -= 1
                else:
                    raise
        else:
            print("Max retries reached. Skipping song.")
            continue
        
        features_dict = {
            'Artist': artist,
            'Title': title,
            'Danceability': audio_features[0]['danceability'],
            'Energy': audio_features[0]['energy'],
            'Acousticness': audio_features[0]['acousticness'],
            'Instrumentalness': audio_features[0]['instrumentalness'],
            'Tempo': audio_features[0]['tempo']
        }
        audio_features_list.append(features_dict)
    else:
        print(f"Song '{title}' by '{artist}' not found.")

audio_features_df = pd.DataFrame(audio_features_list)

audio_features_df.to_csv('audio_features2.csv', index=False)
