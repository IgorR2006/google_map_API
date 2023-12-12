# -*- coding: utf-8 -*-
def creat_json_data(num):
    """Метод создания json файла, позволяет кастомизировать файл"""
    json_data = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362

            }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "Test testovich ### " + num,     # по параметру нам можно отслеживать данные файла
        "types": [
         "shoe park",
         "shop"
         ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    return json_data



