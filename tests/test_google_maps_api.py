from requests import Response

from utils.api import Google_maps_api

'''Create, change, delete new location'''

class Test_create_place():

    def test_create_new_place(self):

        print('Method POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("Method PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)

        print("Method GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("Method DELETE")
        result_get: Response = Google_maps_api.delete_new_place(place_id)

        print("Method GET DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)