from Data.data import Data
import random
import re
import string
import requests
import json


class Common(Data):

    @staticmethod
    def verify_status_code(response: requests.models.Response, expected_status_code: int):
        return response.status_code == expected_status_code

    @staticmethod
    def verify_response_key_exists(response: requests.models.Response, __key: str):
        json_dict = json.loads(response.content)
        return __key in json_dict

    @staticmethod
    def verify_response_key_value(response: requests.models.Response, __key: str, __value):
        json_dict = json.loads(response.content)
        if __key in json_dict:
            return json_dict[__key] == __value
        else:
            raise AssertionError(f"{__key} in not in the response content!")

    @staticmethod
    def verify_response_key_value_class(response: requests.models.Response, __key: str, __class):
        json_dict = json.loads(response.content)
        if __key in json_dict:
            try:
                __class(json_dict[__key])
                return True
            except ValueError:
                return False
        else:
            raise AssertionError(f"{__key} in not in the response content!")

    @staticmethod
    def verify_response_key_value_regexp(response: requests.models.Response, key, regexp):
        json_dict = json.loads(response.content)
        if key in json_dict:
            return bool(re.search(regexp, json_dict[key]))
        else:
            raise AssertionError(f"{key} in not in the response content!")

    @staticmethod
    def verify_response_content(response, expected_content):
        response_dict = json.loads(response.content)
        return response_dict == expected_content

    @staticmethod
    def generate_random_email():
        return "".join(random.choices(string.ascii_letters, k=8)) + "@reqres.in"

    @staticmethod
    def generate_random_password():
        return "".join(random.choices(string.ascii_letters, k=8))

    @staticmethod
    def verify_response_data_length(response: requests.models.Response, expected_length):
        json_dict = json.loads(response.content)
        return len(json_dict.keys()) == expected_length
