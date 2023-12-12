class File:

    def __init__(self, file_name):
        self.file_name = file_name + ".txt"

    def creat_file(self):
        with open(self.file_name, "a") as files:
            files.write("")
        check = "Файл создан"
        return check

    def read_in_file(self):
        with open(self.file_name, "r") as files:
            value = files.read()
        print("Файл прочитан")
        return value

    def write_in_file(self, data):
        with open(self.file_name, "a") as files:
            files.write(f"{data}\n")
        check = "Файл записан"
        return check


