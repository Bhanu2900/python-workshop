# Importing Libraries and Loading Data
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


song_data_url = "https://github.com/mahkaila/songnames/raw/refs/heads/master/SongCSV.csv" # dataset taken form github 
song_data = pd.read_csv(song_data_url)

# Print the first few rows of the dataset for checking if its working or not
print("First few rows of the dataset:")
print(song_data.head())



# Initialize the VADER Sentiment Intensity Analyzer
xyz = SentimentIntensityAnalyzer()


# Define a function to map moods
def map_direct_mood(input_text):
    mood_map = {
        "happy": "Happy",
        "excited": "Excited",
        "calm": "Calm",
        "neutral": "Neutral",
        "sad": "Sad",
        "angry": "Angry",
        "anxious": "Anxious",
        "confident": "Confident",
    }


    input_text_lower = input_text.lower()


    return mood_map.get(input_text_lower, None)


# Define a function to analyze the moods of a song using sentiment analysis
def analyze_mood(text):
    sentiment_score = xyz.polarity_scores(text)
    compound_score = sentiment_score['compound']

    if compound_score >= 0.8:
        return 'Excited'
    elif 0.5 <= compound_score < 0.8:
        return 'Happy'
    elif 0.05 <= compound_score < 0.5:
        return 'Calm'
    elif -0.05 < compound_score < 0.05:
        return 'Neutral'
    elif -0.8 < compound_score <= -0.05:
        return 'Sad'
    elif compound_score <= -0.8:
        return 'Angry'
    return 'Neutral'


# Apply the analyze_mood function to the 'Track Name' column to create a 'Mood' column
if 'Track Name' in song_data.columns:
    song_data['Mood'] = song_data['Track Name'].apply(analyze_mood)
elif 'Title' in song_data.columns:  # Adjust if the column is named 'Title'
    song_data['Mood'] = song_data['Title'].apply(analyze_mood)
else:
    print("No appropriate column for song names found.")
    exit()

# Define a function to recommend songs based on the user's mood
def music_recommender(mood):

    if 'Mood' in song_data.columns:
        recommender_songs = song_data[song_data['Mood'] == mood]
        if recommender_songs.empty:
            return "There are no songs available for your current mood."
        else:
            return recommender_songs
    else:
        return "The 'Mood' column does not exist in the dataset."


# Define a function to get the user's mood input and recommend songs
def get_user_mood():
    user_input = input("What is your current mood? ")

    # First, check if the mood can be directly mapped
    direct_mood = map_direct_mood(user_input)

    if direct_mood:
        mood = direct_mood
    else:
        # If it is  not a direct mood word, go back to sentiment analysis
        mood = analyze_mood(user_input)

    print(f"Mood detected: {mood}")

    recommendation = music_recommender(mood)
    if isinstance(recommendation, str):
        print(recommendation)
    else:
        print("\nRecommended songs for you:")
        print(recommendation[['AlbumName', 'ArtistName', 'Title', 'Year']])


# Run the song recommender
get_user_mood()
