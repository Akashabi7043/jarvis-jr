from commands.system import SystemCommands


class Brain:

    def __init__(self, speaker):
        self.speaker = speaker
        self.system = SystemCommands(speaker)

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

        # Exit
        if "exit" in command or "goodbye" in command:
            self.speaker.speak("Goodbye. Have a nice day.")
            return False

        # Unknown command
        self.speaker.speak("Sorry, I don't understand that command yet.")
        return True