from flask import Flask, render_template, request
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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        return render_template("contact.html", sent=True)
    else:
        return render_template("contact.html", sent=False)   
        
if __name__ == "__main__":
    app.run()