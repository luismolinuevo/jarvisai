import pyttsx3
import io
import numpy as np
import speech_recognition as sr
import whisper
# from config.settings import WHISPER_MODEL
from config import *

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load Whisper model
whisper_model = whisper.load_model(setting.WHISPER_MODEL)

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user input and convert speech to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        # Convert audio to numpy array
        # audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int16).astype(np.float32) / 32768.0
        # audio_data = np.frombuffer(audio.get_wav_data(), dtype=np.int16).astype(np.float32) / 32768.0
        audio_data = np.frombuffer(audio.get_wav_data(convert_rate=16000, convert_width=2), dtype=np.int16).astype(np.float32) / 32768.0



        # Transcribe using Whisper
        # result = whisper_model.transcribe(audio_data)
        result = whisper_model.transcribe(audio_data, no_speech_threshold=0.5, language="en")
        text = result["text"].strip()  # Strip extra whitespace

        print(f"You said: {text}" if text else "No speech detected.")
        return text if text else None
    except Exception as e:
        print("Error recognizing speech:", e)
        return None
