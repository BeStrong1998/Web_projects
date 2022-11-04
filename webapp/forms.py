"""Создаём файл forms.py с описанием формы

1) Импортируем типы полей:
StringField - Для строкового типа
PasswordField - Поле для ввода пароля
SubmitField - Кнопка (в нашем случаи это кнопка "Отправить")

from wtforms.validators import DataRequired - Импортируем валидатор, клас который помогает избежать ручных проверок.
DataRequired - проверяе что пользователь действительно вбил какие то данные
"""


from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
"""BooleanField - Этот модуль для запоминания введённых данных при авторизации"""


class LoginForm(FlaskForm): # Создаём класс LoginForm который наследуем от FlaskForm
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form_control"}) #Создаём поле для формы с именем "Имя пользователя" и передаём список валидаторов, в нашем  случии один DataRequired()
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form_control"}) #Создаём поле для формы с именем "Пароль" и передаём список валидаторов, в нашем  случии один DataRequired()
    remember_me = BooleanField('Запомнить', default=True, render_kw={"class": "form-check-iput"}) #Запоминает введённые данные при авторизации, default=True - значение по умолчанию(значит галочка всегда отмечина)
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"}) #Делаем кнопку с именем "Отправить"
