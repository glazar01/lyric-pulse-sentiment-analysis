import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER sentiment analysis lexicon if you haven't already
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "I love this product! It's amazing."

# Get sentiment scores for the text
sentiment_scores = analyzer.polarity_scores(text)

# Interpret the sentiment scores
compound_score = sentiment_scores['compound']

if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment and sentiment scores
print("Sentiment:", sentiment)
print("Sentiment Scores:", sentiment_scores)
