from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello!<h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXY3MnY4bnR6b3lteDIzbHpvNTUyb2F1ZHRiZzJrcmFjbXJpbjdqdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)