import os
import pvporcupine
import pyaudio
import struct
# from config.settings import ACCESS_KEY
from config.setting import ACCESS_KEY
from modules.speech import speak, listen
from modules.commands import handle_command

WAKE_WORD_PATH = os.path.join(os.path.dirname(__file__), "../resources/Hey_Jarvis.ppn")

# Initialize wake word detection
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keyword_paths=[WAKE_WORD_PATH]
)

# Initialize audio stream
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

def detect_wake_word():
    """Continuously listen for the wake word"""
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

        if porcupine.process(pcm_unpacked) >= 0:
            print("Wake word detected! Listening for command...")
            speak("Yes?")
            command = listen()
            if command:
                handle_command(command)
