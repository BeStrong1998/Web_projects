import time
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
    time.sleep(6)
    html = browser.page_source
    #time.sleep(6)

    # close web browser
    browser.close()
    return html

def save_flat(url, title, date, price):
    flat_exits = RealEstateAds.query.filter(RealEstateAds.url == url).count()
    if not flat_exits:
        new_flat = RealEstateAds(title=title, url=url, date=date, price=price)
        db.session.add(new_flat)
        db.session.commit()