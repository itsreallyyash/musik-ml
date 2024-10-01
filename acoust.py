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


# MFCCs (Mel-Frequency Cepstral Coefficients):

# What it is: Captures the texture and tone of music.
# Example: Happy songs might have higher MFCC values. If you listen to a joyful track, MFCCs will help your project identify it as "happy."

# Spectral Centroid:

# What it is: Measures the brightness of the sound.
# Example: A bright, cheerful song will have a high spectral centroid, while a deep, slow song will have a low value.

# Spectral Contrast:

# What it is: Compares different frequency levels in a song.
# Example: Songs with sharp transitions (like pop or electronic) will have higher contrast, showing excitement.

# Chroma Features:

# What it is: Tracks the harmonic notes in music.
# Example: A song in a major key (happy) has different chroma than one in a minor key (sad).

# Tempo (BPM):

# What it is: Speed of the song.
# Example: Fast songs (150 BPM) feel energetic, slow songs (70 BPM) are calming.

# Zero-Crossing Rate:

# What it is: Measures how often the music waveform changes direction.
# Example: A noisy, energetic song will have a high rate, while a smooth, calm song will have a low rate.
