import requests
import json

with requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82%20%D0%92%D0%BD%D1%83%D0%BA%D0%BE%D0%B2%D0%BE&format=json') as json_file:
    temp_json = json.loads(json_file.content)
    json.dump(temp_json, open('temp.json', 'w'), indent=4)
    print('type temp_json after loads content: ', type(temp_json), ':', temp_json)
    print('_________________________________')
    s = json.dumps(temp_json)
    print(s)
    print(type(s))
