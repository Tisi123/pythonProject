from pytubefix import YouTube
from pytubefix.cli import on_progress
from sys import argv
from moviepy.editor import *
import os
import context.context as context

link = "https://youtu.be/_a5UACtf8Cc"
directory = context.download_directory


def download_video(yt_link):
    yt = YouTube(yt_link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=directory)


def download_audio(yt_link):
    yd = YouTube(yt_link, on_progress_callback=on_progress)
    ys = yd.streams.get_audio_only()
    ys.download(output_path=directory, mp3=True)


download_video(link)
#download_audio(link)
