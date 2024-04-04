import librosa

audio_file = 'zz.wav'
y, sr = librosa.load(audio_file)

mfccs = librosa.feature.mfcc(y=y, sr=sr)
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)

# Display 
print("Mel-Frequency Cepstral Coefficients (MFCCs):")
print(mfccs)
print("\nSpectral Centroid:")
print(spectral_centroid)
print("\nSpectral Contrast:")
print(spectral_contrast)
print("\nChroma Features:")
print(chroma)
print("\nTempo (BPM):", tempo)
print("\nZero-Crossing Rate:")
print(zero_crossing_rate)
