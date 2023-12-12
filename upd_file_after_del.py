# -*- coding: utf-8 -*-
import requests     # Импорт библиотеки реквест для работы с API
from id_place.create_file import File       # импорт класса File для работы с файлами

file = File("ID_place")
data = file.read_in_file()
"""читаем из файла ID_place, передаем их в качестве стоки в переменную дата"""


class UpdateFile:
    """создание класса для удаления (метод delete) и повторного получения информации о локациях (метод get)
     записи актуальных place_id в новый файл"""

    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com/maps/api/place/"
        self.key = "?key=qaclick123"
        self.place_id = data.split()        # получаем place_id в виде списка из файла ID_place
        self.file = File("UPD_place_id after del")      # создаем экзеплляр класса файл для дальнейшего создания файла с актуальными place_id

    def del_new_location(self, num):
        """метод удаления созданных локаций"""
        del_resource = "delete/json"        # эндпоинт для метода delete
        del_url = self.base_url + del_resource + self.key
        body = {
            "place_id": self.place_id[num]
        }
        result_del = requests.delete(del_url, json=body)
        print(result_del)
        print(result_del.text)

    def get_info_about_location_after_del(self, num):
        """метод get для получения актуально информации о локациях"""
        self.file.creat_file()      # создаем новый файл с актуальными place_id
        get_resource = "get/json"   # эндпоинт для метода get
        get_url = self.base_url + get_resource + self.key + "&place_id=" + self.place_id[num]
        """создаем url запроса "читаем" place_id из селфа, который в свою очередь получает их из файла ID_place"""
        result_get = requests.get(get_url)
        if result_get.status_code == 200:
            """проверяем ответы по статус коду при "200" записываем place_id в новый файл иначе сообщение в консоль
            о том что локация с указанным place_id не существует"""
            return self.file.write_in_file(self.place_id[num])
        else:
            print("Локация с указанным place_id: " + self.place_id[num] + " не существует")


upd_info_location = UpdateFile()

for i in range(1, 5, 2):
    """цикл удаляет локации с индексом place_id 2 и 4"""
    upd_info_location.del_new_location(i)

for i in range(5):
    """цикл актуализирует информацию о place_id в новом файле"""
    upd_info_location.get_info_about_location_after_del(i)
