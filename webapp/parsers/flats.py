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


def get_flats_snippets():# парсимим страницу на cian.ru по новострокам и берем от туда ссылку на конкретное обялвение
    for page in range(1,3):# парсим первые 5 страниц
        html = get_html(f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=2&offer_type=flat&p={page}&region=-1')# в 'page' передаем параметр номер страницы
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
    flat_without_photos = RealEstateAds.query.filter(RealEstateAds.photos.is_(None))#запрос в базу по url без описания квартиры
    for flat in flat_without_photos:
        print(flat.url)
        html = get_html(flat.url)#получяем html на отдельную квартиру
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            address = soup.find('div', class_="a10a3f92e9--geo--VTC9X").find("address",class_="a10a3f92e9--address--F06X3").text.replace('На карте', '.') #парсинг адреса
            square = soup.find('div', class_='a10a3f92e9--info-value--bm3DC').text# парсинг колличество квадратных метров
            square = float((square.replace(' м²', '').replace(',', '.')))# привеодим строку к float для кооректной записи в базу
            number_of_rooms = parser_room(soup.find('h1', class_='a10a3f92e9--title--UEAG3').text)# парсим колличество комнот
            try:
                photos = soup.find('div', class_='a10a3f92e9--item--CEy7Z')
                all_photos = photos.find('img')['src']
            except AttributeError:
                print('другая структура хранения фотографий')
                all_photos = soup.find('li', class_='a10a3f92e9--container--LhW9D').find('img')['src']

            flat.address = address
            flat.square = square
            flat.number_of_rooms = number_of_rooms
            flat.photos = all_photos
            db.session.add(flat)
            db.session.commit()


if __name__ == '__main__':#запускаем для отладки парсера файл fill in
    get_flats_snippets()