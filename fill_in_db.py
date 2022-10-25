
from webapp import db, create_app
from webapp.model import RealEstateAds

def ads_db():
    app = create_app()
    with app.app_context(): # Контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
        advertisement = RealEstateAds(title='Продажа',
                                        url='34',
                                        price=4000,
                                        square=1600,
                                        address='г. Одинцово',
                                        number_of_rooms=5)  # Добавлякм значения в колонки нашей таблицы (Просто что то записываем в таблицу тестим)

        #db1 = db.session.execute(db.select(RealEstateAds).order_by(RealEstateAds.address)).scalars() # Эта команда выводит все объявления с параметрами
        #for i in db1:
         #   print(i)

        db2 = db.session.execute(db.select(RealEstateAds).filter_by()) # выводит объявление с его параметрами по номеру id
        for j in db2:
            print(j)
if __name__ == '__main__':
   ads_db()

    #db.session.add(advertisement) # Зафиксировали изменения 
    #db.session.commit() # Добавили изменения в таблицу



    #advertisement.price = True
   #db.session.commit()
    #При довавлении новых данных важно менять данные полей в которых значения являются уникальными, в нашем случаи это значения поля url



    #db.session.delete(user) Удалить
    #db.session.commit()

