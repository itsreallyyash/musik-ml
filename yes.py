import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to extract features from audio files
def extract_features(audio_file_path):
    y, sr = librosa.load(audio_file_path)

    # Extract features (e.g., Mel-frequency cepstral coefficients (MFCCs))
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

    # Concatenate features
    features = np.concatenate((mfccs, [spectral_centroid], spectral_contrast), axis=0)

    return features.T  # Transpose for shape consistency

# Function to load audio files and extract features with labels
def load_data(data_dir):
    features = []
    labels = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".mp3"):
                file_path = os.path.join(root, file)
                instrument = os.path.basename(root)
                features.append(extract_features(file_path))
                labels.append(instrument)

    return np.vstack(features), np.array(labels)

# Load and preprocess data
data_dir = 'path_to_your_dataset_directory'  # Directory containing audio files categorized by instrument
X, y = load_data(data_dir)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier (e.g., Random Forest)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Evaluate the classifier
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
