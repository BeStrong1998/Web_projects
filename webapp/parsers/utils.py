import time
from datetime import datetime, timedelta
from selenium import webdriver
from webapp import db
from webapp.model import RealEstateAds


def get_html(url):
    """
    -Функция работает с пакетом selenium(помогает обойти блакировки get-запросов на авито и циан).
    -Для работы нужно скачать ChromeDriver(https://sites.google.com/chromium.org/driver/).
    -Помесить ChromeDriver в паку с вертульным окружением проекта (env/bin).
    """
    # start web browser
    browser=webdriver.Chrome()

    # get source code
    browser.get(url)
    time.sleep(2)
    html = browser.page_source

    # close web browser
    browser.close()
    return html

def save_flat(url, title, date, price):
    flat_exits = RealEstateAds.query.filter(RealEstateAds.url == url).count()
    if not flat_exits:
        new_flat = RealEstateAds(title=title, url=url, date=date, price=price)
        db.session.add(new_flat)
        db.session.commit()

def parser_room(room_str):
    if '8-комн' in room_str:
        room = 8
    elif '7-комн' in room_str:
        room = 7
    elif '6-комн' in room_str:
        room = 6
    elif '5-комн' in room_str:
        room = 5
    elif '4-комн' in room_str:
        room = 4
    elif '3-комн' in room_str:
        room = 3
    elif '2-комн' in room_str:
        room = 2
    elif '1-комн' in room_str:
        room = 1
    else:# студия
        room = 9
    return room


def parse_date(date_str):# парсим строку на вхождение слова сегодня/вчера и меняем на актуальную дату
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y, %H:%M')
    except ValueError:
        this_year = datetime.today().year# добавляем год к дате
        return datetime.strptime(date_str, '%d %b, %H:%M').replace(year=this_year)