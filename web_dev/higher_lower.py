from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9!<h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXY3MnY4bnR6b3lteDIzbHpvNTUyb2F1ZHRiZzJrcmFjbXJpbjdqdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif">'

def random_color(function):

    def wrap_with_color(**kwargs):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        content = function(**kwargs)
        return f"<h1 style='color: rgb{r,g,b}'>{content}</h1>"
    return wrap_with_color



@app.route("/<int:guess>")
@random_color
def check_guess(guess):
    if guess < random_number:
        return "Too low, try again!"
    elif guess > random_number:
        return "Too high, try again!"
    else:
        return "You found me!"
    

if __name__ == "__main__":
    app.run(debug=True)