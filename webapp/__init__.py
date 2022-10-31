from flask import Flask, render_template, abort

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
        titels = "Объявления"
        flats = RealEstateAds.query.filter(RealEstateAds.ads.isnot(None)).order_by(RealEstateAds.date.desc()).all()
        return render_template("index.html", page_title=titels, flats=flats)
        
    @app.route('/flat/<int:flat_id>')
    def single_flat(flat_id):
        my_flat = RealEstateAds.query.filter(RealEstateAds.id == flat_id).first()
        if not my_flat:
            abort(404)
        return render_template('single_flat.html', page_title=my_flat.title, flat=my_flat)

    return app