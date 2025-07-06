from flask import Flask, render_template, request, jsonify, url_for
import random
import os


app = Flask(__name__)

webviewer_dir = "D:/PythonProjects/pythonProject/web_dev/webviewer_python/static/contents/"
media_directories = os.scandir(webviewer_dir)
videos_per_batch = 10

image_array = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"]
video_array = [".mp4", ".webm", ".ogg", ".avi", ".mov", ".wmv", ".mkv", ".m4v", ".m4v",".mpv", ".m4p", ".m4r", ".m4v"]


def get_content(name, format, offset=0, batch_size=videos_per_batch):
    requested_post = os.scandir(webviewer_dir+name)
    return_array = []
    for entry in requested_post :
        filename = os.fsdecode(entry)
        _, extension = os.path.splitext(filename)
        if extension in format:
            return_array.append("contents/"+name + "/"+entry.name)
    random.shuffle(return_array)
    return return_array[offset:offset + batch_size]


@app.route('/load_more/<path:name>')
def load_more(name):
    offset = int(request.args.get('offset', 0))
    folder_name = name
    videos = get_content(name, video_array, offset, videos_per_batch)
    video_urls = [url_for('static', filename=video) for video in videos]
    return jsonify(video_urls)


@app.route('/')
def home():
    return render_template('index.html', media_directories=media_directories)


@app.route("/media/<path:name>")
def show_images(name):
    images = get_content(name, image_array)
    return render_template("media.html", post_entries=images)


@app.route("/vids/<path:name>")
def show_vids(name):
    vids = get_content(name, video_array)
    return render_template("vids.html", post_entries=vids, folder_name=name)


if __name__ == "__main__":
    app.run()