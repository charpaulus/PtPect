import requests

geocoder_request = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json&geocode=Севастополь"

response = requests.get(geocoder_request)
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("HTTP Статус:", response.status_code, '(', response.reason, ')')
