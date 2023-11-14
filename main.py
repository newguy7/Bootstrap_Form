from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length,Email
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.secret_key = "this is my secret key"
bootstrap = Bootstrap4(app)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),Email(message=('Invalid email address.'))])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    login_form = LoginForm()
    email_data = login_form.email.data
    password_data = login_form.password.data
    if login_form.validate_on_submit():
        if email_data == "admin@email.com" and password_data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html",form=login_form)




if __name__ == "__main__":
    app.run(debug=True)