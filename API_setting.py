import requests
from id_place.create_file import File


class TestLocation:

    def __init__(self, json_data):
        self.file = File("ID_place")
        self.file.creat_file()
        self.json_data = json_data
        self.base_url = "https://rahulshettyacademy.com/maps/api/place/"
        self.key = "?key=qaclick123"
        self.place_id = ""

    def post_create_new_location(self, num):
        post_resource = "add/json"
        post_url = self.base_url + post_resource + self.key
        result_post = requests.post(post_url, json=self.json_data[num])
        assert result_post.status_code == 200
        print(result_post)
        print(result_post.text)
        res_json = result_post.json()
        place_id = res_json.get('place_id')
        print(place_id)
        print(self.file.write_in_file(place_id))
        self.place_id = self.file.read_in_file().split()
        return self.place_id

    def get_info_about_new_location(self, num):
        get_resource = "get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id=" + self.place_id[num]
        result_get = requests.get(get_url)
        assert result_get.status_code == 200
        print(result_get)
        print(result_get.text)



