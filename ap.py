import streamlit as st
import pandas as pd
import requests

# Load your song lyrics dataset
@st.cache_data
def load_data():
    return pd.read_csv('ex.csv')

# Function to get lyrics for a song
def get_lyrics(song_name, df):
    match = df[df['song_name'].str.lower() == song_name.lower()]
    if not match.empty:
        return match.iloc[0]['lyrics']
    return None

# Send lyrics to Ollama
def query_ollama(lyrics, model="llama3"):
    prompt = f"Analyze the lyrics of the song and provide a summary:\n\n{lyrics}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt},
        stream=False
    )
    if response.status_code == 200:
        return response.json().get("response")
    else:
        return "Error querying Ollama."

# Streamlit UI
def main():
    st.title("🎵 Song Lyrics Analyzer with Ollama")
    df = load_data()
    
    song_input = st.text_input("Enter song name:")
    
    if st.button("Analyze"):
        if not song_input:
            st.warning("Please enter a song name.")
        else:
            lyrics = get_lyrics(song_input, df)
            if lyrics:
                st.subheader("🎤 Lyrics Found:")
                st.text_area("Lyrics", lyrics, height=200)
                
                with st.spinner("Analyzing lyrics with Ollama..."):
                    response = query_ollama(lyrics)
                    st.subheader("🧠 Ollama's Interpretation:")
                    st.write(response)
            else:
                st.error("Song not found in the dataset.")

if __name__ == "__main__":
    main()
