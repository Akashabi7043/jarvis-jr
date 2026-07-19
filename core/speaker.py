import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        # Voice settings
        self.engine.setProperty("rate", 170)      # Speaking speed
        self.engine.setProperty("volume", 1.0)    # Volume (0.0 - 1.0)

        voices = self.engine.getProperty("voices")

        # Use the first available voice
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        print(f"JARVIS: {text}")   # Also print to terminal
        self.engine.say(text)
        self.engine.runAndWait()