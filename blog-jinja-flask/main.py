from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/846586136f22502264d9"
response = requests.get(blog_url)
all_posts = response.json()

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:id>")
def post(id):
    for post in all_posts:
        if post["id"] == id:
            returned_post = post
            return render_template("post.html", post=returned_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()