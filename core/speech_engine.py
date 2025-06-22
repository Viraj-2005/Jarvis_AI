# core/speech_engine.py

from gtts import gTTS
import os
import time

def speak(text):
    print(f"🗣️ Jarvis: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    os.system(f"mpg123 {filename} > /dev/null 2>&1")
    time.sleep(0.1)
    os.remove(filename)
