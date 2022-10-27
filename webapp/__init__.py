

from flask import Flask, render_template
from flask_migrate import Migrate


from webapp.model import db
from webapp.model import RealEstateAds
from webapp.parsers.flats import get_flats_snippets, get_flat_content
 


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
   
    @app.route('/')
    def index():
        
        flats = RealEstateAds.query
        return render_template("index.html", flats=flats)

    @app.route('/flat/<int:flat_id>')
    def single_flat(flat_id):
        my_flat = RealEstateAds.query.filter(RealEstateAds.id == flat_id).first()
       
        return render_template("single_flat.html", flat=my_flat)


    return app


#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run - Для запуска через командную строку
# Запускаем проект просто командой run







'''
 real_ads = []
        selection_of_apartments = "Объявления"
        apartments_ads = "Продажа кавартир в новостройках"
        
        real_ads = db.select(RealEstateAds).filter_by# Выводит све объявления в Flask приложение

        return render_template("index.html", selection_of_apartments=selection_of_apartments, apartments_ads=apartments_ads, real_ads=real_ads)
        '''






'''
@app.route('/')
    def in_db():
       
        return render_template("in_db.html")

'''


'''
 real_ads = []
        selection_of_apartments = "Подбор квартир"
        apartments_ads = "Объявления"
        real_ads = RealEstateAds.query.order_by(RealEstateAds.date).all() # Выводит све объявления в Flask приложение

        return render_template("index.html", selection_of_apartments=selection_of_apartments, apartments_ads=apartments_ads, real_ads=real_ads)
'''



