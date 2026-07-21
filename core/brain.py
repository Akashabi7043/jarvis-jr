import os
import subprocess
from commands.system import SystemCommands
from commands.apps import AppCommands


class Brain:

    def __init__(self, speaker):
        self.speaker = speaker
        self.system = SystemCommands(speaker)
        self.apps = AppCommands(speaker)

    def process(self, command):

        command = command.lower().strip()

        # Greetings
        if command in ["hi", "hello", "hey"]:
            self.speaker.speak("Hello! How can I help you?")
            return True

        # Time
        if "time" in command:
            self.system.tell_time()
            return True

        # Date
        if "date" in command:
            self.system.tell_date()
            return True

        # Calculator
        if "calculator" in command:
            self.apps.open_calculator()
            return True

        # Notepad
        if "notepad" in command:
            self.apps.open_notepad()
            return True

        # Chrome
        if "chrome" in command:
            chrome_path = r"C:\Users\Admin\AppData\Local\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_path):
                subprocess.Popen(chrome_path)
                self.speaker.speak("Opening Google Chrome")
            else:
                self.speaker.speak("Google Chrome is not installed.")
            return True

        # VS Code
        if "code" in command or "visual studio" in command:
            vscode_path = r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            if os.path.exists(vscode_path):
                subprocess.Popen(vscode_path)
                self.speaker.speak("Opening Visual Studio Code")
            else:
                self.speaker.speak("Visual Studio Code is not installed.")
            return True

        # Exit
        if "exit" in command or "goodbye" in command:
            self.speaker.speak("Goodbye. Have a nice day.")
            return False

        # Unknown command
        self.speaker.speak("Sorry, I don't understand that command yet.")
        return True