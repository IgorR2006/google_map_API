# -*- coding: utf-8 -*-
from API_setting import TestLocation        # импорт класса для раоты с APi google map
from json_data import creat_json_data       # импорт метода создания json файла для отправки в методе POST


json_data_list = [creat_json_data(num=f'Test # {str(i + 1)}') for i in range(5)]
"""создание списка из json файлов, позволяюший внутри класса обращаться к отдельному файлу по индексу"""

test = TestLocation(json_data_list)         # создание экзепляра класса

for i in range(5):
    """отправка 5 запросов метода post, получение подтвержения создания новых локаций через метод get, в каждом запросе 
    свой json файл, по результам ответа можно сравтить строку адреса, с указанным Test # """
    test.post_create_new_location(i)
    test.get_info_about_new_location(i)
