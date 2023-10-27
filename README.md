# Lyric Pulse: Evaluating Emotion Recognition Models on Song Lyrics
Testing sentiment analysis models using lyrics

# Summary
Music emotion recognition and recommendations today are changing the way people find and listen to their preferred musical tracks. In this work, we compare four existing text-based emotion recognition models. Our study assesses their adaptability to song lyrics, offering insights into their potential impact on music recommendation systems. This research represents a significant step in enhancing personalized and emotionally resonant music recommendations through emotion-aware technology. 

# Motivation and research value
Personally speaking, we both like music, especially Taylor Swift's emotional expressions in songwriting and we want to do something highly related to our interests. Secondly, doing sentimental analysis for lyrics on the one hand could help the audience understand songs better. On the other hand, it will contribute to the music recommendation system. Last but not least, considering accessibility, it's always good to have labels for visually impaired people before they want to listen to a song.

# Data
Our input data is song lyrics paired with emotion label/labels. We have following data sets:

| Data set | Content | URL |
| ------------- | ------------- | ------------- |
| SingleLabel | Lyrics paired with a single label | [SingleLabel.csv](https://github.com/glazar01/UZH-essentials-project/blob/310d0532aebf24bc25d1994f599cf1cea6286d8b/data/SingleLabel.csv)|
| MultiLabel  | Lyrics paired with multiple labels  | [MultiLabel.csv](https://github.com/glazar01/UZH-essentials-project/blob/310d0532aebf24bc25d1994f599cf1cea6286d8b/data/MultiLabel.csv)|

Emotion Labels: 'amazement', 'calmness', 'joyful activation', 'nostalgia', 'power', 'sadness', 'solemnity', 'tenderness', and 'tension'.

# Testing Models

We test four different sentiment analysis models that can be found on [Hugging Face](https://huggingface.co/). 

- Model1: [roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions?text=I+love+you)

- Model2: [emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?text=This+movie+always+makes+me+cry..)

- Model3: [distilbert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion?text=I+like+you.+I+love+you)

- Model4: [t-5 base-finetuned-emotion](https://huggingface.co/mrm8488/t5-base-finetuned-emotion?text=I+wish+you+were+here+but+it+is+impossible)
