# commands/system_control.py

import os
import datetime
from core.speech_engine import speak

def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime('%A, %d %B %Y')
    speak(f"Today is {date}")

def open_application(app_name):
    if app_name == "vs code":
        speak("Opening Visual Studio Code")
        os.system("code")
    elif app_name == "chrome":
        speak("Opening Chrome")
        os.system("google-chrome")
    else:
        speak("I don't know how to open that app yet.")

def shutdown_system():
    speak("Shutting down in 5 seconds.")
    os.system("shutdown now")

def restart_system():
    speak("Restarting system.")
    os.system("reboot")
