import os
import subprocess


class FileCommands:
    def list_files(self, folder):
        folders = {
            "desktop": self.desktop,
            "documents": self.documents,
            "downloads": self.downloads,
            "pictures": self.pictures,
            "music": self.music,
            "videos": self.videos,
        }

        path = folders.get(folder.lower())

        if not path or not os.path.exists(path):
            self.speaker.speak("Folder not found.")
            return

        files = os.listdir(path)

        if not files:
            self.speaker.speak(f"The {folder} folder is empty.")
            return

        self.speaker.speak(f"There are {len(files)} items in {folder}.")

        for file in files:
            print(file)

    def create_file(self, file_name):
        desktop = self.desktop

        file_path = os.path.join(desktop, file_name)

        try:
            with open(file_path, "w") as file:
                pass

            self.speaker.speak(f"File {file_name} created successfully.")

        except Exception as e:
            self.speaker.speak("Unable to create the file.")
            print(e)

    def delete_file(self, file_name):
        desktop = self.desktop
        file_path = os.path.join(desktop, file_name)

        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                self.speaker.speak(f"File {file_name} deleted successfully.")
            else:
                self.speaker.speak("File not found.")

        except Exception as e:
            self.speaker.speak("Unable to delete the file.")
            print(e)

    def rename_file(self, old_name, new_name):
        desktop = self.desktop

        old_path = os.path.join(desktop, old_name)
        new_path = os.path.join(desktop, new_name)

        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                self.speaker.speak(f"Renamed {old_name} to {new_name}.")
            else:
                self.speaker.speak("File not found.")

        except Exception as e:
            self.speaker.speak("Unable to rename the file.")
            print(e)

    def create_folder(self, folder_name):
        desktop = self.desktop
        folder_path = os.path.join(desktop, folder_name)

        try:
            os.makedirs(folder_path, exist_ok=True)
            self.speaker.speak(f"Folder {folder_name} created successfully.")

        except Exception as e:
            self.speaker.speak("Unable to create folder.")
            print(e)

    def __init__(self, speaker):
        self.speaker = speaker
        home = os.path.expanduser("~")
        onedrive = os.path.join(home, "OneDrive")

        def get_folder(folder):
            one = os.path.join(onedrive, folder)
            normal = os.path.join(home, folder)

            if os.path.exists(one):
                return one
            elif os.path.exists(normal):
                return normal
            else:
                return None

        self.desktop = get_folder("Desktop")
        self.documents = get_folder("Documents")
        self.downloads = get_folder("Downloads")
        self.pictures = get_folder("Pictures")
        self.music = get_folder("Music")
        self.videos = get_folder("Videos")

    def open_folder(self, path, name):
        if path and os.path.exists(path):
            subprocess.Popen(["explorer", path])
            self.speaker.speak(f"Opening {name}")
        else:
            self.speaker.speak(f"{name} folder was not found.")

    def open_desktop(self):
        self.open_folder(self.desktop, "Desktop")

    def open_documents(self):
        self.open_folder(self.documents, "Documents")

    def open_downloads(self):
        self.open_folder(self.downloads, "Downloads")

    def open_pictures(self):
        self.open_folder(self.pictures, "Pictures")

    def open_music(self):
        self.open_folder(self.music, "Music")

    def open_videos(self):
        self.open_folder(self.videos, "Videos")