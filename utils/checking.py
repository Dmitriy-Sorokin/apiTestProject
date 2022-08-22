'''Methods for checking the responses of our requests'''
import json

from requests import Response


class Checking():

    '''Method for checking status code'''
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully!!! Status code = " + str(response.status_code))
        else:
            print("FALSE!!! Status code = " + str(response.status_code))

    '''Method for checking presence of required fields in response fo request '''
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields present")

    '''Method for checking value of required fields in response fo request '''
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ' TRUE !!!')

    '''Method for checking value of required fields in response fo request on word'''

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + ' TRUE !!!')
        else:
            print("Word " + search_word + ' FALSE !!!')