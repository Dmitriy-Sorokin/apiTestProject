from requests import Response

from utils.api import Google_maps_api

'''Create, change, delete new location'''

class Test_create_place():

    def test_create_new_place(self):

        print('Method POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method GET")
        result_get: Response = Google_maps_api.get_new_place(place_id)
