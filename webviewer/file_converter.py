import moviepy.editor as moviepy
import os

FROM_EXT    = "mkv"
TO_EXT      = "mp4"
SOURCE_DIR  = "/Volumes/Seagate Media/Movies/MKVs"
DEST_DIR    = "/Volumes/Seagate Media/Movies/MP4s"

for file in os.listdir(SOURCE_DIR):
    if file.lower().endswith(FROM_EXT.lower()):
        from_path   = os.path.join(SOURCE_DIR, file)
        to_path     = os.path.join(DEST_DIR, file.rsplit('.', 1)[0]) + '.' + TO_EXT

        print(f"Converting {from_path} to {to_path}")

        clip = moviepy.VideoFileClip(from_path)
        clip.write_videofile(to_path)