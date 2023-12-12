from API_setting import TestLocation
from json_data import creat_json_data


json_data_list = [creat_json_data(num=f'Test # {str(i + 1)}') for i in range(5)]

test = TestLocation(json_data_list)

for i in range(5):
    test.post_create_new_location(i)
    test.get_info_about_new_location(i)


