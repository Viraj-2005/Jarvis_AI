# core/recognizer.py

import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("⚠️ Internet error or API down.")
        return ""
