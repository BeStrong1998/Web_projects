import requests


def get_html(url):# по url полсчаем hrml страницу и возвращаем ее
    headers = {
        'User=Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False        