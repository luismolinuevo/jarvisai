import ollama
from config.setting import OLLAMA_MODEL

def ask_ollama(question):
    """Send query to Ollama AI model and return response"""
    response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": question}])
    return response['message']['content']
