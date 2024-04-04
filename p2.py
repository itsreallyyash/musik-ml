import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_audio_features(track_id):
    audio_features = sp.audio_features([track_id])[0]
    return audio_features

def print_song_features(features):
    print("Danceability:", features['danceability'])
    print("Energy:", features['energy'])
    print("Acousticness:", features['acousticness'])
    print("Instrumentalness:", features['instrumentalness'])
    print("Tempo:", features['tempo'])

spotify_url = "https://open.spotify.com/track/3DK6m7It6Pw857FcQftMds?si=7b5304dd7b224234"
track_id = spotify_url.split('/')[-1].split('?')[0]
features = get_audio_features(track_id)
print_song_features(features)
