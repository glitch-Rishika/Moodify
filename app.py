from flask import Flask, render_template, request, jsonify
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

songs = pd.read_csv('data/songs.csv')


def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["sad", "cry", "lonely", "hurt", "depressed"]):
        return "sad"
    if any(word in text for word in ["happy", "joy", "excited", "fun"]):
        return "happy"
    if any(word in text for word in ["love", "miss", "crush"]):
        return "romantic"
    if any(word in text for word in ["angry", "mad", "frustrated"]):
        return "angry"
    if any(word in text for word in ["motivated", "focus", "study"]):
        return "motivational"
    if any(word in text for word in ["calm", "relaxed", "peaceful"]):
        return "calm"
    if any(word in text for word in ["bored", "nothing", "blank"]):
        return "bored"

    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.5:
        return "happy"
    elif score <= -0.5:
        return "sad"
    else:
        return "neutral"


def get_genre(emotion):
    genres = {
        "happy": "Pop / Dance",
        "sad": "Lo-fi / Acoustic",
        "romantic": "Romantic / Soft",
        "angry": "Rock / Rap",
        "motivational": "Workout / EDM",
        "calm": "Ambient / Chill",
        "bored": "Indie / Random",
        "neutral": "Mixed"
    }
    return genres.get(emotion, "Mixed")


def recommend(emotion):
    def match(tags):
        tag_list = [t.strip().lower() for t in tags.split(";")]
        return emotion in tag_list

    matched = songs[songs['emotion_tags'].apply(match)]

    if not matched.empty:
        shuffled = matched.sample(frac=1)
        return shuffled.head(3)[
            ['title', 'artist', 'language', 'youtube_link']
        ].to_dict(orient='records')

    return songs.sample(3)[
        ['title', 'artist', 'language', 'youtube_link']
    ].to_dict(orient='records')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/recommend', methods=['POST'])
def rec():
    text = request.form.get("text")
    emotion = detect_emotion(text)
    recs = recommend(emotion)
    genre = get_genre(emotion)

    return jsonify({
        "emotion": emotion,
        "genre": genre,
        "songs": recs
    })


if __name__ == "__main__":
    app.run(debug=True)
