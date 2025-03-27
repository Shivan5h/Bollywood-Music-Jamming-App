# Bollywood Jamming Session 🎶

## Overview
This Streamlit app generates a Bollywood song mashup for a jamming session. Users can input a **Genre (required)** and an **Artist (optional)**, along with the number of songs they want. The app fetches lyrics from LyricsOVH, arranges them creatively using LLM and RAG techniques, and outputs a jam-ready lyrical arrangement.

## Features
- **User Inputs:** Genre (required), Artist (optional), Number of Songs (slider)
- **Song Selection:** Matches songs from `ex.csv` based on user inputs
- **Lyrics Fetching:** Scrapes lyrics from LyricsOVH API and stores them in a SQLite database
- **Jamming Arrangement:**
  - Uses intros, interludes, and outros from different songs
  - Reuses song parts to enhance the flow
  - Switches between songs if a common word appears
- **Interactive UI:** Built with Streamlit for seamless user experience

## Installation
### Prerequisites
- Python 3.x
- Pip
- Streamlit
- OpenAI API key (for LLM integration)

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd bollywood-jamming
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Configuration
- **API Keys:** Update OpenAI API key in the script.
- **Dataset:** Ensure `ex.csv` contains Bollywood song data with columns:
  - Song-Name
  - Singer/Artists
  - Genre
  - Album/Movie
  - User-Rating

## Usage
1. **Select Genre**: Mandatory input
2. **Enter Artist** (Optional)
3. **Adjust Number of Songs**: Using the slider
4. **Click 'Create Jamming'**
5. **Enjoy the lyrical arrangement!** 🎤

## Future Enhancements
- Improve NLP for better song transitions
- Integrate with YouTube for audio snippets
- Allow users to save and share jamming sessions

## License
MIT License

