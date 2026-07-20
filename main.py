from datetime import datetime

from core.speaker import Speaker
from core.listener import Listener
from core.brain import Brain


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
    brain = Brain(speaker)

    speaker.speak("Hello Akash. I am Junior Jarvis.")

    while True:

        command = listener.listen()

        if command == "":
            continue

        keep_running = brain.process(command)

        if not keep_running:
            break


if __name__ == "__main__":
    main()