from flask import Flask
from random import randint

app = Flask(__name__)
rand_num = randint(0,9)

@app.route("/")
def home():
    return f"<h1>Guess the number between 0 and 9<br>\
        <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

@app.route("/<int:number>")
def check_number(number):
    if number<rand_num:
        return f"<h1 style='color:red;'>Too low, try again!</h1><br>\
            <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    elif number>rand_num:
        return f"<h1 style='color:blue;'>Too high, try again!</h1><br>\
            <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    else:
        return f"<h1 style='color:green;'>You found me!</h1><br>\
            <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)