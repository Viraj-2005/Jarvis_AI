# core/command_parser.py

from commands.web_tasks import search_google, play_youtube, search_wikipedia
from commands.system_control import tell_time, tell_date, open_application, shutdown_system, restart_system
from core.speech_engine import speak

def parse_command(command):
    command = command.lower()

    if "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open youtube" in command:
        play_youtube("trending videos")

    elif "search for" in command:
        query = command.replace("search for", "")
        search_google(query)

    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "")
        search_wikipedia(query)

    elif "open vs code" in command:
        open_application("vs code")

    elif "open chrome" in command:
        open_application("chrome")

    elif "shutdown" in command:
        shutdown_system()

    elif "restart" in command:
        restart_system()

    elif "stop" in command or "exit" in command:
        speak("Goodbye Viraj.")
        return "exit"

    else:
        speak("Sorry, I didn't understand that.")
