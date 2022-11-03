from flask import Flask, render_template, abort, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
""" Подключаем flask_login с наше приложение с помощью  LoginManager
    login_user - Для реализации обработке самой формы логина
    flash - позволяет передавать сообщения между route-ами
    redirect - делает перенаправление пользователя на другую страницу
    url_for - помогает получить url по имени функции, которая этот url обрабатывает
    logout_user - Даёт возможность выйти из системы и завершить сесию
    current_user - Убирает возможность заходить повторно уже авторизованным пользователям
    login_required - Создаёт страницу только зарегистрированным
"""


from webapp.forms import LoginForm
from flask_migrate import Migrate
from webapp.model import db, RealEstateAds, User 

 
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager() #Создаём экземпляр LoginManager()
    login_manager.init_app(app) #Делаем init и передаём app(апликейшн)
    login_manager.login_view = 'login' # Говорим как у нас будет называться функция которая будет заниматься логином пользователя(у нас login())
   

    """Создаём функцию которая будет проверять и получать по id нужного пользователя"""
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id) #Запрос в базу данных для получения и сравнения пользователя по id


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


    @app.route('/login') # Создаём форму, пишем функцию которая будет рисовать нам саму страничку
    def login():
        if current_user.is_authenticated: #Проверяет авторизован ли пользователь
            return redirect(url_for('index')) # если пользователь авторизован перебрасывает на главную страницу 'index'
        titles = "Авторизация"
        login_form = LoginForm() # Создаём экземпляр класса
        return render_template('login.html', page_title=titles, form=login_form) #Передаём в браузер данные из шаблона login.html


    @app.route('/process-login', methods=['POST']) #Говорим какие методы будем обрабатывать (у нас:'POST')
    def process_login(): #Создаём функцию
        form = LoginForm() #Создаём экземпляр объекта LoginForm()

        if form.validate_on_submit():#Если нам пришли данные формы и она валидируется
            user = User.query.filter(User.username == form.username.data).first() #Если ошибки не возникло мы можем запросить пользователя из базы данных по имени username
            if user and user.check_password(form.password.data): #Если такой пользователь существует и проверка пароля прошла
                login_user(user, remember=form.remember_me.data) #Запоминаем данного пользователя. remember=form.remember_me.data - проверяет стоит ли галочка или нет, remember - будет False либо True
                flash('Вы успешно вошли на сайт') # Выводим на странице сообщение
                return redirect(url_for('index')) # Переадресуем пользователя на главную страницу

        flash('Неправильные имя или пароль') # Если проверка не прошла
        return redirect(url_for('login')) # Переадресуем на страницу 'login'


    @app.route('/logout') 
    def logout(): #Пользоватедь зашёл на '/logout'
        logout_user() #Делаем logout_user (выходим из системы)
        flash('Вы успешно разлогинились') #Пишет на экране сообщение 'Вы успешно разлогинились'
        return redirect(url_for('index')) #Переадресует на страницу 'index'


    @app.route('/admin')
    @login_required #Проверяет авторизован ли пользователь если нет выдаст ошибку
    def admin_index():
        if current_user.is_admin: #Если в функции is_admin, role == 'admin'
            return 'Привет админ!' #Показываем скрытую страницу пользователю если поле role = 'admin'
        else:
            return 'Вы не админ!'  #Не показываем скрытую страницу пользователю так как поле role = другому значению


    return app
    