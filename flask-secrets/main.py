from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, email

app = Flask(__name__)
app.secret_key = 'sfvnoqu3498hfdv'

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)