import os
import subprocess
from commands.files import FileCommands
from commands.browser import BrowserCommands
from commands.system import SystemCommands
from commands.apps import AppCommands


class Brain:

    def __init__(self, speaker):
        home = os.path.expanduser("~")
        onedrive = os.path.join(home, "OneDrive")

        def get_folder(name):
            one = os.path.join(onedrive, name)
            normal = os.path.join(home, name)

            if os.path.exists(one):
                return one
            return normal

        self.desktop = get_folder("Desktop")
        self.documents = get_folder("Documents")
        self.downloads = get_folder("Downloads")
        self.pictures = get_folder("Pictures")
        self.music = get_folder("Music")
        self.videos = get_folder("Videos")
        self.speaker = speaker
        self.files = FileCommands(speaker)
        self.system = SystemCommands(speaker)
        self.apps = AppCommands(speaker)
        self.browser = BrowserCommands(speaker)

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

        # Google
        if "open google" in command:
            self.browser.open_google()
            return True

        # YouTube
        if "open youtube" in command:
            self.browser.open_youtube()
            return True

        # Gmail
        if "open gmail" in command:
            self.browser.open_gmail()
            return True

        # Wikipedia
        if "open wikipedia" in command:
            self.browser.open_wikipedia()
            return True

        # Google Search
        if command.startswith("search google for"):
            query = command.replace("search google for", "").strip()
            self.browser.google_search(query)
            return True

        # YouTube Search
        if command.startswith("search youtube for"):
            query = command.replace("search youtube for", "").strip()
            self.browser.youtube_search(query)
            return True
        # Desktop
        if "open desktop" in command:
            self.files.open_desktop()
            return True

        # Documents
        if "open documents" in command:
            self.files.open_documents()
            return True

        # Downloads
        if "open downloads" in command:
            self.files.open_downloads()
            return True

        # Pictures
        if "open pictures" in command:
            self.files.open_pictures()
            return True

        # Music
        if "open music" in command:
            self.files.open_music()
            return True

        # Videos
        if "open videos" in command:
            self.files.open_videos()
            return True

        # Create Folder
        if command.startswith("create folder"):
            folder_name = command.replace("create folder", "").strip()

            if folder_name == "":
                self.speaker.speak("Please tell me the folder name.")
                return True

            self.files.create_folder(folder_name)
            return True

        # Create File
        if command.startswith("create file"):
            file_name = command.replace("create file", "").strip()

            if file_name == "":
                self.speaker.speak("Please tell me the file name.")
                return True

            self.files.create_file(file_name)
            return True

        # Exit
        if "exit" in command or "goodbye" in command:
            self.speaker.speak("Goodbye. Have a nice day.")
            return False

        # Unknown command
        self.speaker.speak("Sorry, I don't understand that command yet.")
        return True