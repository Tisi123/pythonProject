import os
import shutil
import context

download_directory = context.download_directory
screenshot_directory = context.screenshot_directory
video_directory = context.video_directory
music_directory = context.music_directory
saves_directory = context.saves_directory

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
