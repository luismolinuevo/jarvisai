import os
from dotenv import load_dotenv #remove dotenv load from here

# Load environment variables
load_dotenv() #remove dotenv load from here

# API Keys & Settings
ACCESS_KEY = os.getenv("PORCUPINE_ACCESS_KEY")
WHISPER_MODEL = "base"
OLLAMA_MODEL = "mistral"