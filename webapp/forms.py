from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form_control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form_control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
