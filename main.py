# main.py

from core.recognizer import take_command
from core.speech_engine import speak
from core.command_parser import parse_command

if __name__ == "__main__":
    speak("Hello Viraj, I am ready to assist you.")

    while True:
        command = take_command()
        if command:
            result = parse_command(command)
            if result == "exit":
                break
