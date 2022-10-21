

from requests import delete
from webapp import db, create_app
from webapp.model import RealEstateAds

app = create_app()
with app.app_context(): # Контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
    advertisement = RealEstateAds(title='Продажа',
                                    url='29',
                                    price=4.5,
                                    square=1600,
                                    address='г. Одинцово',
                                    number_of_rooms=5)  # Добавлякм значения в колонки нашей таблицы (Просто что то записываем в таблицу тестим)

    
    db.session.add(advertisement) # Зафиксировали изменения 
    db.session.commit() # Добавили изменения в таблицу


    advertisement.price = True
    db.session.commit()
    #При довавлении новых данных важно менять данные полей в которых значения являются уникальными, в нашем случаи это значения поля url






    #db.session.delete(user) Удалить
    #db.session.commit()




   # db.session.add(advertisement) # Зафиксировали изменения 
   # db.session.commit() # Добавили изменения в таблицу


   # advertisement.price = True
    #db.session.commit()
    # При довавлении новых данных важно менять данные полей в которых значения являются уникальными, в нашем случаи это значения поля url

    















    #db.session.add(advertisement) # Зафиксировали изменения
    #db.session.commit() # Добавили изменения в таблицу


    #advertisement.title = True# Обновить данные
    #db.session.commit()


    #db.session.delete(advertisement) # удалить
    #db.session.commit()

