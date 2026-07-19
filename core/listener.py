import speech_recognition as sr


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("\n🎤 Listening...")

            # Reduce background noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)

            print(f"\n👤 You said: {text}")

            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you.")
            return ""

        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return ""