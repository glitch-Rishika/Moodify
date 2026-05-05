🎧 Moodify 

Moodify is an intelligent music recommendation web app that detects your mood from text input and suggests songs accordingly — complete with embedded YouTube playback, aesthetic UI, and emotion-based themes.

---

✨ Features

- 🧠 AI Mood Detection (VADER Sentiment Analysis)
- 🎵 Emotion-Based Song Recommendations
- 🎧 Genre Suggestions Based on Mood
- ▶️ Embedded YouTube Music Player
- 🎨 Dynamic UI Themes (changes with mood)
- 😍 Modern UI with animations, emojis & gradients
- 🌍 Multi-language Songs (Hindi, English, Korean)

---

🧠 How It Works

1. User enters how they feel (text input)
2. Backend analyzes sentiment using VADER
3. Emotion is detected (happy, sad, romantic, etc.)
4. Songs are filtered based on emotion tags
5. UI updates dynamically and plays songs

---

🛠️ Tech Stack

- Frontend: HTML, Tailwind CSS, JavaScript
- Backend: Python (Flask)
- AI/NLP: VADER Sentiment Analysis
- Data: CSV dataset of songs
- Media: YouTube Embedded Player

---

📁 Project Structure

Moodify/
│
├── app.py
├── data/
│   └── songs.csv
├── templates/
│   └── index.html
└── static/
    └── style.css

---

🚀 Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/moodify-ai.git
cd moodify-ai

2️⃣ Install dependencies

pip install flask pandas vaderSentiment

3️⃣ Run the app

python app.py

4️⃣ Open in browser

http://127.0.0.1:5000/

---

🎯 Example Input

«"I feel lonely and tired"»

👉 Output:

- Emotion: Sad 😢
- Genre: Lo-fi / Acoustic 🎧
- Songs: Embedded YouTube recommendations

---

💡 Future Improvements

- 🔐 User login & personalization
- 📊 Mood history tracking
- 🤖 AI chatbot companion
- 🎶 Spotify API integration
- 📱 Mobile responsive improvements

---

🙌 Acknowledgements

- VADER Sentiment Analysis
- YouTube for music embedding
- Open-source community

---

📌 Author

Rishika Mishra
B.Tech CSE Student | AI & Web Development Enthusiast

---

⭐ If you like this project

Give it a star ⭐ on GitHub and share it!
