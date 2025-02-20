import os
import shutil

download_directory = "D:/Downloads"
screenshot_directory = "D:/Screenshots"
video_directory = "D:/Screenshots/vids"
music_directory = "D:/Music"
saves_directory = "D:/Games/Neuer Ordner/saves"

for file in os.listdir(download_directory):
    filename = os.fsdecode(file)
    _, extension = os.path.splitext(filename)
    match extension:
        case ".save":
            shutil.move(download_directory+"/"+filename, saves_directory+"/"+filename)
        case ".png" | ".jpg" | ".jpeg" | ".webp":
            shutil.move(download_directory+"/"+filename, screenshot_directory+"/"+filename)
        case ".mp4":
            shutil.move(download_directory+"/"+filename, video_directory+"/"+filename)
        case ".mp3" | ".m4a":
            shutil.move(download_directory+"/"+filename, music_directory+"/"+filename)
        case _:
            print("Unknown file type: " + filename)
