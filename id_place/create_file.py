# -*- coding: utf-8 -*-
class File:
    """создание класса по работе с файлами"""

    def __init__(self, file_name):
        self.file_name = file_name + ".txt"

    def creat_file(self):
        """метод создания файла с указанным иминем"""

        with open(self.file_name, "a") as files:
            files.write("")
        check = "Файл создан"
        return check

    def read_in_file(self):
        """метод чтения из файла"""

        with open(self.file_name, "r") as files:
            value = files.read()
        print("Файл прочитан")
        return value

    def write_in_file(self, data):
        """метод записи в файл"""

        with open(self.file_name, "a") as files:
            files.write(f"{data}\n")
        check = "Файл записан"
        return check
