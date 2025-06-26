import streamlit as st
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from constants import *
from prompts import prompt
from pathlib import Path
import uuid
import requests
import os
from huggingface_hub import InferenceClient

# Config Streamlit
st.set_page_config(page_title="🎙️ Story Generator", layout="centered")
st.title("🎙️ Immersive Story Generator")
st.write("Enter a description of your universe, and I'll generate a story and narrate it for you.")

# Image generation
def generate_image_huggingface(prompt, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content  # Image in bytes
    else:
        st.error("Failed to generate image")
        st.text(response.text)
        return None

# Création client TTS
def generate_tts_audio(text, hf_token):
    client = InferenceClient(provider="fal-ai", api_key=HF_TOKEN)
    audio = client.text_to_speech(
        text,
        model="hexgrad/Kokoro-82M"
    )
    return audio  # bytes

# Entrée utilisateur
user_input = st.chat_input("Describe your universe here...")
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=LLM_NAME1)

if user_input:
    with st.spinner("Generating story..."):
        chain = LLMChain(llm=llm, prompt=prompt)
        story = chain.run(user_input=user_input)
        st.markdown("### 📖 Generated Story")
        st.write(story)

    with st.spinner("Generating voice..."):
        audio_bytes = generate_tts_audio(story, HF_TOKEN)
        if audio_bytes:
            audio_path = Path("speech") / f"{uuid.uuid4()}.wav"
            audio_path.parent.mkdir(exist_ok=True)
            with open(audio_path, "wb") as f:
                f.write(audio_bytes)
            st.audio(str(audio_path), format="audio/wav")
            st.success("✅ Voice generated!")

    with st.spinner("Generating image..."):
        image_bytes = generate_image_huggingface(user_input, HF_TOKEN)
        if image_bytes:
            st.image(image_bytes, caption="🎨 Generated Image", use_column_width=True)
