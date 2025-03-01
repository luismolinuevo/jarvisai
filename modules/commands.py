import webbrowser
# from modules.speech import speak
from modules import speech
from modules.ai import ask_ollama

def handle_command(command):
    """Process and execute user commands"""
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speech.speak("Opening YouTube")

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speech.speak(f"Searching Google for {query}")

    elif "weather" in command:
        speech.speak("I am still learning how to fetch the weather, but you can check on your phone.")

    else:
        ai_response = ask_ollama(command)
        speech.speak(ai_response)
