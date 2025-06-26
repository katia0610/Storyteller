import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Variables récupérées depuis le .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
LLM_NAME1 = os.getenv("LLM_NAME1")
LLM_NAME2 = os.getenv("LLM_NAME2")
VOICE = os.getenv("VOICE")
