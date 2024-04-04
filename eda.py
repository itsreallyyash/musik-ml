import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('final_with_sentiment.csv')

sentiment_columns = ['Sentiment_Positivity', 'Sentiment_Negativity', 'Sentiment_Neutrality', 'Sentiment_Compound']
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[sentiment_columns])
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Scores')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='genre', y='Sentiment_Compound', data=df)
plt.title('Distribution of Sentiment Scores by Genre')
plt.xlabel('Genre')
plt.ylabel('Sentiment Compound Score')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sentiment_Compound', y='Danceability', data=df)
plt.title('Sentiment Compound Score vs. Danceability')
plt.xlabel('Sentiment Compound Score')
plt.ylabel('Danceability')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sentiment_Compound', y='Energy', data=df)
plt.title('Sentiment Compound Score vs. Energy')
plt.xlabel('Sentiment Compound Score')
plt.ylabel('Energy')
plt.show()
