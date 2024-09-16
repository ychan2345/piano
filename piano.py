import streamlit as st
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Initialize session state for playback status
if 'playing' not in st.session_state:
    st.session_state['playing'] = False

# Streamlit app title
st.title("🎹 Piano Player")

# File uploader for the MIDI file
uploaded_file = st.file_uploader("Upload a piano sheet with MIDI file", type=["mid", "midi"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_midi_file.mid", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Load the uploaded MIDI file
    pygame.mixer.music.load("temp_midi_file.mid")
    
    # Buttons with icons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶️ Start"):
            pygame.mixer.music.play()
            st.session_state['playing'] = True

    with col2:
        if st.button("⏹️ Stop"):
            pygame.mixer.music.stop()
            st.session_state['playing'] = False

    # Display status
    if st.session_state['playing']:
        st.write("🎶 Playing...")
    else:
        st.write("⏹️ Stopped.")
else:
    st.write("Please upload a MIDI file to start playing.")
