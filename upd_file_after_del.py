import requests
from id_place.create_file import File

file = File("ID_place")
data = file.read_in_file()


class UpdateFile:

    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com/maps/api/place/"
        self.key = "?key=qaclick123"
        self.place_id = data.split()
        self.file = File("UPD_place_id after del")

    def del_new_location(self, num):
        del_resource = "delete/json"
        del_url = self.base_url + del_resource + self.key
        body = {
            "place_id": self.place_id[num]
        }
        result_del = requests.delete(del_url, json=body)
        print(result_del)
        print(result_del.text)

    def get_info_about_location_after_del(self, num):
        self.file.creat_file()
        get_resource = "get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id=" + self.place_id[num]
        result_get = requests.get(get_url)
        if result_get.status_code == 200:
            return self.file.write_in_file(self.place_id[num])


upd_info_location = UpdateFile()

for i in range(1, 5, 2):
    upd_info_location.del_new_location(i)

for i in range(5):
    upd_info_location.get_info_about_location_after_del(i)

