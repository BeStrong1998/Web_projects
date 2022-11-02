from flask import Flask, render_template, abort, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from webapp.forms import LoginForm
from flask_migrate import Migrate
from webapp.model import db, RealEstateAds, User 

 
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
   
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


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

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        titles = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=titles, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))

        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Вы не админ!'    


    return app
    