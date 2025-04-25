import streamlit as st
from langgraph.graph import StateGraph
from typing import List, Dict, Any, TypedDict
import requests
import json

# Your Qroq API Key
API_KEY = "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"

# Headers with the API key
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
# === Define state schema ===
class JamState(TypedDict):
    mood: str
    theme: str
    song_range: tuple
    release_years: tuple
    stars: List[str]
    songs: List[Dict[str, Any]]
    jam_session: List[Dict[str, Any]]

# === LangGraph Setup ===
graph = StateGraph(state_schema=JamState)

# === LangGraph Nodes ===
# Define functions
def fetch_songs_and_lyrics(inputs: Dict[str, Any]) -> Dict[str, Any]:
    mood = inputs["mood"]
    theme = inputs["theme"]
    song_range = inputs["song_range"]
    release_years = inputs["release_years"]
    stars = inputs["stars"]

    payload = {
        "mood": mood,
        "theme": theme,
        "song_range": song_range,
        "release_years": release_years,
        "stars": stars
    }

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "ollama_model_name",
        "prompt": json.dumps(payload)
    })
    songs = response.json().get("songs", [])
    return {"songs": songs}


def generate_jam_session(inputs: Dict[str, Any]) -> Dict[str, Any]:
    songs = inputs["songs"]
    response = requests.post(
        "https://api.qroq.io/jamgen", 
        json={"songs": songs},
        headers=headers 
    )
    session = response.json().get("session", [])
    return {"jam_session": session}


# Add them to graph
graph.add_node("fetch_songs_and_lyrics", fetch_songs_and_lyrics)
graph.add_node("generate_jam_session", generate_jam_session)

# Set up the graph flow
# === LangGraph Assembly ===
graph.set_entry_point("fetch_songs_and_lyrics")
graph.add_edge("fetch_songs_and_lyrics", "generate_jam_session")
graph.set_finish_point("generate_jam_session")


app = graph.compile()

# === Streamlit UI ===
st.title("🎶 Bollywood Music Jamming App")
st.markdown("Create a custom jamming session based on your mood and theme.")

# Required inputs
mood = st.text_input("Mood (Required)", placeholder="e.g., romantic, energetic")
theme = st.text_input("Theme (Required)", placeholder="e.g., rain, heartbreak")

# Sliders
use_time = st.checkbox("Use time limit instead of number of songs")
if use_time:
    time_limit = st.slider("Time Limit (in minutes)", 5, 60, 15)
    song_range = (1, time_limit // 3)
else:
    song_range = st.slider("Number of Songs (Range)", 1, 10, (3, 5))

# Optional inputs
release_years = st.slider("Release Year Range (Optional)", 1980, 2025, (2000, 2020))
star1 = st.text_input("Favorite Star 1 (Optional)")
star2 = st.text_input("Favorite Star 2 (Optional)")
star3 = st.text_input("Favorite Star 3 (Optional)")
stars = [s for s in [star1, star2, star3] if s.strip()]

if st.button("Generate Jam Session"):
    if not mood or not theme:
        st.error("Mood and Theme are required inputs.")
    else:
        with st.spinner("Generating session..."):
            result = app.invoke({
                "mood": mood,
                "theme": theme,
                "song_range": song_range,
                "release_years": release_years,
                "stars": stars
            })
            jam_session = result["jam_session"]

        st.success("Here's your jamming session!")
        for part in jam_session:
            st.subheader(f"{part['part'].capitalize()} - {part['song']}")
            st.write(part['lyrics'])
