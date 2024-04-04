
from flask import Flask, request, jsonify
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
import numpy as np

app = Flask(__name__)
CORS(app) 

client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load the trained model
with open("gradient_boosting_classifier_best.pkl", "rb") as f:
    model = pickle.load(f)

def get_features_from_spotify_url(spotify_url):
    track_id = spotify_url.split('/')[-1].split('?')[0]
    audio_features = sp.audio_features([track_id])[0]
    return audio_features

@app.route('/predict_genre', methods=['POST'])
def predict_genre():
    print("Received request to predict genre")
    data = request.json
    print("Received data:", data)
    # Receive data from the front-end
    data = request.json

    if 'spotifyUrl' in data:
        # Extract features from Spotify URL
        spotify_url = data['spotifyUrl']
        features = get_features_from_spotify_url(spotify_url)
    else:
        # Extract features from manual input fields
        danceability = data['danceability']
        energy = data['energy']
        acousticness = data['acousticness']
        instrumentalness = data['instrumentalness']
        tempo = data['tempo']
        features = {
            'danceability': danceability,
            'energy': energy,
            'acousticness': acousticness,
            'instrumentalness': instrumentalness,
            'tempo': tempo
        }

    # Prepare features for prediction
    features_array = np.array([[features['danceability'], features['energy'], features['acousticness'],
                                 features['instrumentalness'], features['tempo']]])

    # Make prediction
    prediction = model.predict(features_array)

    # Return predicted genre to the front-end
    return jsonify({'predicted_genre': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
