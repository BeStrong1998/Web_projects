from flask import Flask
from parsers.utils import get_html

app = Flask(__name__)

@app.route("/")
def hello():
    url ='https://habr.com/ru/search/?q=python&target_type=posts&order=date'
    return get_html(url)

if __name__=="__main__":
    app.run()