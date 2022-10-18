from webapp import db, create_app
from webapp.model import RealEstateAds

app = create_app()
with app.app_context(): # Контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
    ads = RealEstateAds(title='Продажа 2 комнт кв', url='www.....какой то адрес', price=4.5, square=170.5, address='г. Москва',  number_of_rooms=5)  # Добавлякм значения в колонки нашей таблицы (Просто что то записываем в таблицу тестим)
    db.session.add(ads) # Зафиксировали изменения 
    db.session.commit() # Добавили изменения в таблицу

