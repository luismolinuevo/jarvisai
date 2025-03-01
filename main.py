import sys
import os
# from dotenv import load_dotenv #import dotenv
from modules.wake_word import detect_wake_word

# Load environment variables from .env
# load_dotenv()
 
# Get the current working directory

# project_dir = os.getcwd()
# print(f"Project directory: {project_dir}")  # Debug print
# sys.path.append(project_dir)
# print(f"Sys.path: {sys.path}")  # Debug print

# from modules.wake_word import detect_wake_word

if __name__ == "__main__":
    detect_wake_word()