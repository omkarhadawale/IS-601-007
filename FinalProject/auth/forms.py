from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField("username",validators=[InputRequired(),Length(min=2, max=20, message="The username should be minimum 2 characters in length")])
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match'),Length(min=6, max=20, message="The password should be minimum 6 characters in length")])
    confirm = PasswordField("confirm", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Login")

class UserProfileEdit(FlaskForm):
    username  = StringField("username",validators=[InputRequired(),Length(min=2, max=20, message="The username should be minimum 2 characters in length")])
    email = EmailField("email", validators=[DataRequired(), Email()])
    submit = SubmitField("Update")

class ChangeUserPassword(FlaskForm):
    oldpassword = PasswordField("old password", validators=[InputRequired()])
    newpassword = PasswordField("new password", validators=[InputRequired(), EqualTo('confirmnewpassword', message='Passwords must match'),Length(min=6, max=20, message="The password should be minimum 6 characters in length")])
    confirmnewpassword = PasswordField("confirm new password", validators=[DataRequired()])
    submit = SubmitField("Set Password")