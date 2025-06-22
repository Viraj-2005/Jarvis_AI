# commands/web_tasks.py

import pywhatkit
import wikipedia
import webbrowser
from core.speech_engine import speak

def search_google(query):
    speak(f"Searching Google for {query}")
    pywhatkit.search(query)

def play_youtube(video):
    speak(f"Playing {video} on YouTube")
    pywhatkit.playonyt(video)

def search_wikipedia(topic):
    speak(f"Searching Wikipedia for {topic}")
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError:
        speak("Too many results. Please be more specific.")
    except:
        speak("Sorry, I couldn't find anything.")
