import os


basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, '..', 'apartments.db'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'apartments.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "sjiwjspowpjsi;l7uh4rr4h7bhnopej%94tj"
