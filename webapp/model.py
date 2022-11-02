from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy #Импортируем библиотеку
from datetime import datetime


db = SQLAlchemy() #Создаём объект на основе класса SQLAlchemy и передаём туда объект app созданный на основе класса Flask

class RealEstateAds(db.Model): #Создаём класс и говорим что наследуем всё от объекта db, который является объектом SQLAlchemy
    id = db.Column(db.Integer, primary_key=True) #Уникальный индификатор объявления это наш внутренний индефикатор
    title = db.Column(db.String, nullable=False) #Название объявления, нельзя установить пустое название
    url = db.Column(db.String, unique=True, nullable=False) #Ссылка на объявление, нельзя установить пустое название
    date = db.Column(db.String, default=datetime.utcnow) #выводится дата и время, виводим значение по умолчанию - это то время когда была создана наша статья, при условии если дата небыла установленна
    ads = db.Column(db.Text, nullable=True) #Полный текст объявления, может не иметь текста
    price = db.Column(db.Float, nullable=True) #Стоимостть указанная на объявлении
    square = db.Column(db.Float, nullable=True) # Площадь квартиры указанная в объявлении
    address = db.Column(db.String, nullable=True) # Адрес квартиры
    number_of_rooms = db.Column(db.Integer, nullable=True) #Колличество комнат в квартире

    def __repr__(self):
        return '<RealEstateAds {} {} {} {} {} {} {} {} {} {}>'.format(self.id, self.title, self.url, self.date, self.ads, self.price, self.square, self.address, self.number_of_rooms)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name{} id={}>'.format(self.username, self.id)

