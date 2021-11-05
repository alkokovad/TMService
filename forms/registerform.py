from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = TextAreaField('Ваше имя', validators=[DataRequired()])
    email = EmailField('Ваш email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Вход')
