from flask_sqlalchemy import SQLAlchemy #Импортируем библиотеку

from app import app #Импортируем объект
from datetime import datetime #Импортитуем библиотеку дата и время



app.config['SOLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' #устанавливаем значение той базы данных с которой будем работать и создаём название blog.db(с расширением db)
db = SQLAlchemy(app) #Создаём объект на основе класса SQLAlchemy и передаём туда объект app созданный на основе класса Flask

class Real_estate_ads(db.Model): #Создаём класс и говорим что наследуем всё от объекта db, который является объектом SQLAlchemy
    id = db.Column(db.Integer, primary_key=True) #Уникальный индификатор объявления это наш внутренний индефикатор
    title = db.Column(db.String, nullable=False) #Название объявления, нельзя установить пустое название
    url = db.Column(db.String, unique=True, nullable=False) #Ссылка на объявление, нельзя установить пустое название
    date = db.Column(db.DateTaim, default=datetime.utcnow) #выводится дата и время, виводим значение по умолчанию - это то время когда была создана наша статья, при условии если дата небыла установленна
    ads = db.Column(db.Text, nullable=True) #Полный текст объявления, может не иметь текста
    price = db.Column(db.Float, nullable=False) #Стоимостть указанная на объявлении
    square = db.Column(db.Float, nullable=False) # Площадь квартиры указанная в объявлении
    address = db.Column(db.String, nullable=False) # Адрес квартиры
    number_of_rooms = db.Column(db.Integer, nullable=False) #Колличество комнат в квартире

    def __repr__(self):  #Вызываем метод питона, self означает что мы обращаемся к объекту класса который сейчас активен тоесть News
        return '<real_estate_ads {} {}>'.format(self.tatle, self.url) #Позволит опознать каждую из новостей выведет tatle-название объявления и url-адрес объявления
