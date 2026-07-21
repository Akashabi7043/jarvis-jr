from datetime import datetime


class SystemCommands:
    def __init__(self, speaker):
        self.speaker = speaker

    def tell_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        self.speaker.speak(f"The current time is {current_time}")

    def tell_date(self):
        current_date = datetime.now().strftime("%d %B %Y")
        self.speaker.speak(f"Today's date is {current_date}")