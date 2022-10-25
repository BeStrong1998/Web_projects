
from flask import Flask, render_template
from flask_migrate import Migrate

from webapp.model import db
from webapp.model import RealEstateAds


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
   
    @app.route('/')
    def index():
        real_ads = []
        selection_of_apartments = "Объявления"
        apartments_ads = "Продажа кавартир в новостройках"
        real_ads = RealEstateAds.query #.order_by(RealEstateAds.date).all() # Выводит све объявления в Flask приложение

        return render_template("index.html", selection_of_apartments=selection_of_apartments, apartments_ads=apartments_ads, real_ads=real_ads)

    return app


#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run - Для запуска через командную строку
# Запускаем проект просто командой run



'''
 real_ads = []
        selection_of_apartments = "Подбор квартир"
        apartments_ads = "Объявления"
        real_ads = RealEstateAds.query.order_by(RealEstateAds.date).all() # Выводит све объявления в Flask приложение

        return render_template("index.html", selection_of_apartments=selection_of_apartments, apartments_ads=apartments_ads, real_ads=real_ads)
'''



