
from flask import Flask, render_template
from flask_migrate import Migrate



from webapp.model import db




def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
   
    @app.route('/')
    def index():
        return render_template("index.html")

    return app


#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run - Для запуска через командную строку
# Запускаем проект просто командой run
