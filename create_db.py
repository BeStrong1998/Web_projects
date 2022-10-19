<<<<<<< HEAD
from webapp import db
from webapp import create_app

app = create_app()
with app.app_context(): #контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
    db.create_all()

    
=======
from app import db, create_app

app = create_app()
with app.app_context():
    db.create_all()
>>>>>>> 008685bcc8b37e28b80bf57dd0bfa7e7c5be3f1c
