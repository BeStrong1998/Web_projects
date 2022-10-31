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