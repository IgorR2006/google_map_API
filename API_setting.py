# -*- coding: utf-8 -*-
import requests         # Импорт библиотеки реквест для работы с API
from id_place.create_file import File       # импорт класса File для работы с файлами


class TestLocation:
    """создание класса для тестирования API методы (POST, GET)"""

    def __init__(self, json_data):
        self.file = File("ID_place")        # создание экземпряла класса File
        self.file.creat_file()              # создание файла с указанным именем
        self.json_data = json_data          # передача в методы класса json файла(списка)
        self.base_url = "https://rahulshettyacademy.com/maps/api/place/"        # базовый url
        self.key = "?key=qaclick123"        # базовый params для передачи во все методы
        self.place_id = ""                  # инциализация списка place_id, для передачи в методы класса

    def post_create_new_location(self, num):
        """метод отправки post запроса для создания новой локации, в параметры получает число по которому
        получает соответствующий json файл(передается в качестве индекса для списка)"""
        post_resource = "add/json"      # эндпоинт для запроса post
        post_url = self.base_url + post_resource + self.key     # url запроса post
        result_post = requests.post(post_url, json=self.json_data[num])
        assert result_post.status_code == 200       # проверка статус кода ответа
        print(result_post)
        print(result_post.text)
        res_json = result_post.json()
        place_id = res_json.get('place_id')         # парсинг json ответа для извлечения 'place_id'
        print(place_id)
        print(self.file.write_in_file(place_id))    # запись 'place_id' в файл
        self.place_id = self.file.read_in_file().split()        # чтение 'place_id' из файла для передачи в селф в виде списка, для дальнейшего чтения в методе get
        return self.place_id

    def get_info_about_new_location(self, num):
        """метод отправки get запроса для получения информации о новой локации, в параметры получает число по которому
        получает соответствующий 'place_id' из селфа, который в свою очередь попадает туда из файла в методе post (передается в качестве индекса для списка)"""
        get_resource = "get/json"       # эндпоинт гет запроса
        get_url = self.base_url + get_resource + self.key + "&place_id=" + self.place_id[num]       # url запроса гет с соответствующим place_id
        result_get = requests.get(get_url)
        assert result_get.status_code == 200
        print(result_get)
        print(result_get.text)



