
# 🎶 Bollywood Music Jamming App

An AI-powered jamming platform that curates and blends Bollywood songs into a seamless musical session based on user inputs like mood, theme, year, and favorite artists. Lyrics are separated from the music, and instrumental parts are played while bold lyrics appear dynamically with a visually adaptive UI.

---

## 🚀 Features

- 🎧 **Jamming Flow Generator**: Intro → Interludes → Chorus → Outro.
- 🧠 **GenAI + NLP**: Understands mood/theme and arranges songs accordingly.
- 🎵 **Lyrics & Instrument Separation**: Shows bold lyrics while playing only instrumental versions.
- 🎨 **Dynamic UI**: Backgrounds adapt to song transitions.
- 🤖 **Auto Mode**: Let AI auto-select and arrange songs.
- ✨ **Manual Mode**: Manually control transitions and parts.
- 🎶 **Multi-API Support**: Spotify, Saavn, Last.fm, Musixmatch, (optionally Qroq).
- ❤️ **Favorite Songs**: Mark and save preferred tracks.
- 🔗 **Collab + Share**: Share jam sessions with friends.

---

## 🧠 Tech Stack

| Layer         | Tools/Frameworks |
|---------------|------------------|
| 🧠 AI Layer    | GenAI, NLP, LangChain |
| 🎼 Music APIs  | Spotify API, Saavn API (saavn.dev), Last.fm, Musixmatch |
| 🎛️ Audio Ops  | Librosa, Pydub, Transformers (for BERT) |
| 💻 Backend     | FastAPI / Flask (optional), Python |
| 🌐 Frontend    | Streamlit / React |
| 📦 Deployment  | Vercel / Streamlit Cloud / Localhost |
| 🔑 API Key Used | Qroq (optional, replace with working endpoints) |

---

## 📥 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Bollywood-Music-Jamming-App.git
cd Bollywood-Music-Jamming-App
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Keys

Create a `.env` file:

```
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
LASTFM_API_KEY=your_key
SAAVN_API_KEY=your_key
MUSIXMATCH_API_KEY=your_key
QROQ_API_KEY=your_key   # Optional
```

Or directly assign them in the script if testing locally.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Or if you're using `app2.py` (LangGraph):

```bash
python app2.py
```

---

## 🧪 Sample Input

- 🎵 Number of Songs: 5  
- 🎭 Mood: Chill  
- 🎨 Theme: Friendship  
- 📅 Year Range: 2010–2020  
- 🧑‍🎤 Artists: Arijit Singh, Pritam, Amit Trivedi

---

## 📦 Folder Structure

```
Bollywood-Music-Jamming-App/
│
├── app.py              # Main Streamlit app
├── app2.py             # LangGraph AI pipeline
├── utils/
│   ├── api_wrappers.py
│   └── audio_utils.py
├── assets/
│   └── visuals/        # Dynamic UI backgrounds
├── README.md
└── requirements.txt
```

---

## 🛠️ Troubleshooting

- ❌ **Qroq URL Not Working**:
  - Replace with OpenAI/HuggingFace LLM alternatives.
  - Or contact Qroq support for updated endpoints.

- 🎧 **Audio Not Playing?**
  - Ensure `ffmpeg` is installed for Pydub:
    ```bash
    brew install ffmpeg  # macOS
    sudo apt install ffmpeg  # Ubuntu
    ```

---

## 💡 Future Enhancements

- 🎛️ Drag-and-drop song parts to rearrange manually.
- 🗣️ Voice input for mood/theme detection.
- 📱 Mobile-friendly UI.
- 🧩 Plugin mode for DJ apps.

---

## 🤝 Contributing

Feel free to open issues or PRs for new features or bug fixes. All contributions are welcome.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ by [Your Name].
