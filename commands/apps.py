import subprocess
import os


class AppCommands:

    def __init__(self, speaker):
        self.speaker = speaker

    def open_calculator(self):
        os.system("start calc")
        self.speaker.speak("Opening Calculator")

    def open_notepad(self):
        os.system("start notepad")
        self.speaker.speak("Opening Notepad")

    def open_chrome(self):
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        if os.path.exists(chrome_path):
            subprocess.Popen(chrome_path)
            self.speaker.speak("Opening Google Chrome")
        else:
            self.speaker.speak("Google Chrome is not installed.")

    def open_vscode(self):
        vscode_path = r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        if os.path.exists(vscode_path):
            subprocess.Popen(vscode_path)
            self.speaker.speak("Opening Visual Studio Code")
        else:
            self.speaker.speak("Visual Studio Code is not installed.")