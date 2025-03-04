# Bollywood Music Jamming App

A **Generative AI-powered** music jamming application that arranges Bollywood songs dynamically based on mood, theme, and user preferences. This app separates music and lyrics, displaying **bold lyrics** while playing **instrumental tracks** for an immersive karaoke-like jamming experience.

## Features
- **Dynamic Song Arrangement**: AI arranges songs to create a seamless jamming experience.
- **Lyric-based Song Transitions**: Songs switch when similar words appear in two tracks.
- **Background Transitions**: UI dynamically changes as songs switch.
- **Auto Mode**: AI automatically selects and arranges songs.
- **Save & Replay**: Save jam sessions and replay them later.
- **Manual Transitions**: Users can adjust song transitions.
- **Collaborative Mode**: Share and jam with friends.
- **Favorites**: Mark songs for jamming.
- **User Profiles**: Save history, preferences, and jam sessions.
- **Upload Custom Songs**: Integrate personal songs into jam sessions.

## Tech Stack
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **AI Module**: NLP, Vectorization, LangChain
- **APIs**:
  - **Spotify API** (Song metadata & streaming)
  - **Last.fm API** (Moods, themes, and metadata)
  - **JioSaavn Web Scraping** (Song search & details)

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/bollywood-music-jamming.git
cd bollywood-music-jamming
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Backend
```bash
python backend.py
```

### 4. Run the Frontend
```bash
cd frontend
npm install
npm start
```

## API Usage
### **1. Get Songs**
Endpoint: `/get_songs` (POST)
```json
{
  "mood": "happy",
  "theme": "love",
  "release_year_range": [2000, 2023],
  "artists": ["Arijit Singh", "Shreya Ghoshal"]
}
```
Response:
```json
[
  {"title": "Tum Hi Ho", "artist": "Arijit Singh"},
  {"title": "Channa Mereya", "artist": "Arijit Singh"}
]
```

## Future Enhancements
- **Real-time Beat Detection**: Improved transitions based on beat matching.
- **Live Jamming Mode**: Synchronize multiple users in real-time.
- **AI Voice Separation**: More accurate instrumental extraction.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes.
4. Open a Pull Request.

## License
MIT License

