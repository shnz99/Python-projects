from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, email
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sfvnoqu3498hfdv'
    Bootstrap(app)
    
    return app
    
app = create_app()


class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), email(message="You must type a valid email (with '@' and '.')")])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, message="Field must be 8 characters long at least.")])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success", methods=['GET'])
def success():
    return render_template('success.html')

@app.route("/denied", methods=['GET'])
def denied():
    return render_template('denied.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return success()
        else:
            return denied()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)