import pandas as pd

audio_features_df = pd.read_csv('audio_features.csv')
output2_df = pd.read_csv('output2.csv')

merged_df = pd.merge(audio_features_df, output2_df, left_on='Title', right_on='Track ID', how='left')

merged_df.drop('Track ID', axis=1, inplace=True)

merged_df.rename(columns={'Genre': 'genre'}, inplace=True)
merged_df.to_csv('output_audio_features.csv', index=False)
