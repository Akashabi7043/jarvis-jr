class Brain:

    def __init__(self, speaker):
        self.speaker = speaker

    def process(self, command):

        command = command.lower().strip()

        if command in ["hi", "hello", "hey"]:
            self.speaker.speak("Hello! How can I help you?")
            return True

        if "exit" in command or "goodbye" in command:
            self.speaker.speak("Goodbye. Have a nice day.")
            return False

        self.speaker.speak("Sorry, I don't understand that command yet.")
        return True