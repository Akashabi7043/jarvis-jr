import json
import os


class Memory:

    def __init__(self):
        self.memory_file = os.path.join("data", "memory.json")

        # Create the memory file if it doesn't exist
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as file:
                json.dump({}, file, indent=4)

    def load_memory(self):
        with open(self.memory_file, "r") as file:
            return json.load(file)

    def save_memory(self, data):
        with open(self.memory_file, "w") as file:
            json.dump(data, file, indent=4)

    def remember(self, key, value):
        data = self.load_memory()
        data[key] = value

        print("Saving:", data)   # Debug message

        self.save_memory(data)

    def recall(self, key):
        data = self.load_memory()
        return data.get(key, None)