from flask_login import UserMixin #Имеет встроенные дополнительные атрибуты и методы - для того что бы не добавлять руками
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


class User(db.Model, UserMixin): #Создаём класс User со своими полями
    id = db.Column(db.Integer, primary_key=True) #Уникальный индефикатор - primary_key=True
    username = db.Column(db.String(50), index=True, unique=True) # index=True - username делаем индексом, так как поиск по индексу намного быстрее. unique=True - означает что в базе могут быть только уникальные username
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True) # Ротль пользователя (в нашем случаи будет храниться admin либо user)

    def set_password(self, password): #Пишем функцию set_password, где в password - приходит некая строка
        self.password = generate_password_hash(password) # После чего мы эту некую строку пропускаем чезез generate_password_hash и получаем некий длинный шифр, а результат кладём в модель User в поле password
        """generate_password_hash - Делает такое шифрование которое потом нельзя зазшифровать для пароль который был сохранён в базу данных"""
    
    def check_password(self, password):
        return check_password_hash(self.password, password) # Принимает self.password - зашифрованный пароль который лежит в базе данных и password - пароль который ввел пользователь на сайте. Сравнит эти строки и вернет True или Folse
        """check_password_hash - Шифрует строку которая приходит от пользователя таким же способом как и generate_password_hash и потом сверяет с зашифрованнм паролем из бызы данных"""
 
    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name{} id={}>'.format(self.username, self.id) # Для того когда мы выводим на экран какого нибудь юзера получали строчку что это действительно user с каким то username. self.User - обращаемся к текущему username  

