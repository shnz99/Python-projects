from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Guess the number between 0 and 9<br>\
        <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"
        
if __name__ == "__main__":
    app.run(debug=True)