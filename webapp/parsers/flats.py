from bs4 import BeautifulSoup
from utils import get_html, save_flat


def get_flats_snippets():# парсимим страницу на cian.ru по новострокам и берем от туда ссылку на конкретное обялвение
    html = get_html("https://www.cian.ru/kupit-kvartiru-novostroyki/")
    soup = BeautifulSoup(html, 'html.parser')
    flats_list = soup.find('div', class_="_93444fe79c--wrapper--W0WqH").find_all('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
    for flat in flats_list:
        url = flat.find('a')['href']
        title = flat.find('span', class_='_93444fe79c--color_primary_100--mNATk _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6').text
        residential_name =flat.find('a', class_='_93444fe79c--jk--dIktL').text
        published = flat.find('div', class_="_93444fe79c--absolute--yut0v").text
        price = flat.find('span', class_='_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6').text
        save_flat(url, residential_name, title, published, price)


if __name__ == '__main__':
    get_flats_snippets()