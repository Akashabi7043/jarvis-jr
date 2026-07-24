import webbrowser
import urllib.parse


class BrowserCommands:

    def __init__(self, speaker):
        self.speaker = speaker

    def open_google(self):
        webbrowser.open("https://www.google.com")
        self.speaker.speak("Opening Google")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")
        self.speaker.speak("Opening YouTube")

    def open_gmail(self):
        webbrowser.open("https://mail.google.com")
        self.speaker.speak("Opening Gmail")

    def open_wikipedia(self):
        webbrowser.open("https://www.wikipedia.org")
        self.speaker.speak("Opening Wikipedia")

    def google_search(self, query):
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)
        self.speaker.speak(f"Searching Google for {query}")

    def youtube_search(self, query):
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        self.speaker.speak(f"Searching YouTube for {query}")