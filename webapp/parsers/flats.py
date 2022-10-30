import locale
import platform

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from webapp.parsers.utils import get_html, save_flat
from webapp import db
from webapp.model import RealEstateAds


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, "ru_RU")


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


def get_flats_snippets():# парсимим страницу на cian.ru по новострокам и берем от туда ссылку на конкретное обялвение
    for page in range(1, 5):# парсим первые 5 страниц
        html = get_html(f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={page}&region=1')# в 'page' передаем параметр номер страницы
        soup = BeautifulSoup(html, 'html.parser')
        flats_list = soup.find('div', class_="_93444fe79c--wrapper--W0WqH").find_all('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
        for flat in flats_list:
            url = flat.find('a')['href']
            title = flat.find('span', class_='_93444fe79c--color_primary_100--mNATk _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6').text
            date = flat.find('div', class_="_93444fe79c--absolute--yut0v").text
            date = parse_date(date)# приобразовываем данные в формат datetime
            price = flat.find('span', class_='_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6').text
            price = price.replace('₽', '').replace(' ', '')# убераем пробелы и обозначение рублей из суммы
            print(url, title, date, price)
            save_flat(url, title, date, price)# сохраняем данные в базу


def get_flat_content():
    flat_without_text = RealEstateAds.query.filter(RealEstateAds.ads.is_(None))#запрос в базу по url без описания квартиры
    for flat in flat_without_text:
        print(flat.url)
        html = get_html(flat.url)#получяем html на отдельную квартиру
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            address = soup.find('div', class_="a10a3f92e9--geo--VTC9X").find("address",class_="a10a3f92e9--address--F06X3").text                   #если описание сушествует то добовляем его в базу данных
            flat_ads = soup.find('main', class_='a10a3f92e9--offer_card_page--qobLH').decode_contents()
            if flat_ads:
                flat.ads = flat_ads
                flat.address = address
                db.session.add(flat)
                db.session.commit()

if __name__ == '__main__':#запускаем для отладки парсера файл fill in
    get_flats_snippets()