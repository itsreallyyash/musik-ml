import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

final_df = pd.read_csv('final_output .csv')

final_df['Lyrics'] = final_df['Lyrics'].fillna('')  

def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

final_df['Sentiment_Scores'] = final_df['Lyrics'].apply(calculate_sentiment_scores)

final_df[['Sentiment_Positivity', 'Sentiment_Negativity', 'Sentiment_Neutrality', 'Sentiment_Compound']] = final_df['Sentiment_Scores'].apply(pd.Series)
final_df.drop('Sentiment_Scores', axis=1, inplace=True)

final_df.to_csv('final_with_sentiment.csv', index=False)
