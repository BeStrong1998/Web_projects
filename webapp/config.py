from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, '..', 'apartments.db'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'apartments.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "sjiwjspowpjsi;l7uh4rr4h7bhnopej%94tj" # Вводим случайную строку которую сложно угадать
"""Переменная конфигурации SECRET_KEY - важная часть многих приложений Flask и используется в качестве криптографического ключа,
при генерации подписей или токенов. Flask-WTF использует его для защиты веб-форм от Межсайтовой подделки запроса или CSRF (произносится как «seasurf»)."""

REMEMBER_COOKIE_DURATION = timedelta(days=5) #Запоминает пароль пользователя на 5 дней
