# Lyric Pylse: Mapping Sentiments in Music Lyrics
A Sentiment Analysis for song lyrics

# Summary
Music emotion recognition and recommendations today are changing the way people find and listen to their preferred musical tracks. Our task is to do a sentimental analysis (focusing on emotion detection) of different songs. 

# Motivation and research value
Personally speaking, we both like music, especially Taylor Swift's emotional expressions in songwriting and we want to do something highly related to our interests. Secondly, doing sentimental analysis for lyrics on the one hand could help the audience understand songs better. On the other hand, it will contribute to the music recommendation system. Last but not least, considering accessibility, it's always good to have labels for visually impaired people before they want to listen to a song.

# Project Plan
## Data Preparation
Our input data will be text (lyrics of songs) paired with emotion labels. We have two data sets (SingleLabel and MultiLabel) with the following possible labels: 'activation', 'amazement', 'calmness', 'joyful', 'nostalgia', 'power', 'sadness', 'solemnity', 'tenderness', and 'tension'.

The idea is to label more manually or by counting some keywords. 

## Model and Goal
Overall, this is a classification problem. We want to train and test different models and compare them. We can also try to use some existing models (e.g. the \href{https://www.nltk.org/_modules/nltk/sentiment/vader.html}{NLKT's Vader Sentiment analyzer}) on our input data sets. Something extra is to provide some visualizations using word cloud showing to the users the preferences of a singer.
