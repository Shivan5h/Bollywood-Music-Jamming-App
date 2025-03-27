import streamlit as st
import pandas as pd
import random
import requests
from transformers import pipeline
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import DataFrameLoader
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "openaiapikey"
# Load the dataset
df = pd.read_csv("ex.csv")

def fetch_lyrics(artist, song):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("lyrics", "Lyrics not found")
    return "Lyrics not found"

# Streamlit UI
st.title("Bollywood Jamming Session AI")

embedding_function = OpenAIEmbeddings()

artist_input = st.text_input("Enter Artist (Optional)")
genre_input = st.text_input("Enter Genre (Required)")
song_count = st.slider("Number of Songs", min_value=1, max_value=10, value=5)

if st.button("Create Jamming"):
    # Filter dataset
    filtered_songs = df[df["Genre"].str.contains(genre_input, case=False, na=False)]
    if artist_input:
        filtered_songs = filtered_songs[filtered_songs["Singer/Artists"].str.contains(artist_input, case=False, na=False)]
    
    if filtered_songs.empty:
        st.warning("No songs found for the given criteria.")
    else:
        selected_songs = filtered_songs.sample(min(song_count, len(filtered_songs)))
        song_lyrics = {}
        
        for _, row in selected_songs.iterrows():
            lyrics = fetch_lyrics(str(row["Singer/Artists"]).split(",")[0], row["Song-Name"])
            song_lyrics[row["Song-Name"]] = lyrics
        
        # NLP-based arrangement
        llm = OpenAI()
        selected_songs["Lyrics"] = selected_songs["Song-Name"].apply(lambda song: song_lyrics.get(song, ""))
        loader = DataFrameLoader(selected_songs, page_content_column="Lyrics")
        documents = loader.load()
        vectorstore = Chroma.from_documents(
            documents,
            embedding=embedding_function,
            persist_directory="./chroma_db"
        )


        jam_arrangement = ""
        
        for song, lyrics in song_lyrics.items():
            jam_arrangement += f"{song}: {lyrics[:300]}...\n\n"  # Truncated for jamming flow
        
        # Display final jamming session
        st.subheader("Your Jamming Session:")
        st.text(jam_arrangement)
