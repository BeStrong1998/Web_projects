import requests


link = "https://auto.ru/cars/used/sale/bmw/3er/1115926858-810e07cd/"
responce = requests.get(link)
print(responce.status_code)
print(responce.text) # выводит html конкретного объявления
