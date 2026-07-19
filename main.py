from datetime import datetime

from core.speaker import Speaker
from core.listener import Listener


def startup():
    print("=" * 50)
    print("         JARVIS JUNIOR v0.1")
    print("=" * 50)

    current_time = datetime.now().strftime("%I:%M:%S %p")

    print("System Started Successfully!")
    print(f"Current Time : {current_time}")
    print("Status       : ONLINE")
    print("=" * 50)


def main():

    startup()

    speaker = Speaker()
    listener = Listener()

    speaker.speak("Hello Akash. I am Junior Jarvis.")

    while True:

        command = listener.listen()

        if command == "":
            continue

        if "exit" in command or "goodbye" in command:

            speaker.speak("Goodbye. Have a nice day.")

            break

        else:

            speaker.speak(f"You said {command}")


if __name__ == "__main__":
    main()