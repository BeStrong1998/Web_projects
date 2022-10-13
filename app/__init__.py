from flask import Flask, render_template


from app.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return "Привет!"

    return app


#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run - Для запуска через командную строку

