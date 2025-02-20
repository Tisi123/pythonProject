import os
from RedDownloader import RedDownloader
import shutil

link = "https://www.reddit.com/r/shitposting/comments/1g647ob/_/"
download_directory = "D:/Downloads"
name = "AOAIOA"

file = RedDownloader.Download(url=link, output=name, quality=1080)
file_name = file.output
filename = os.fsdecode(file_name+".mp4")
shutil.move(os.curdir+"/"+filename, download_directory+"/"+filename)
