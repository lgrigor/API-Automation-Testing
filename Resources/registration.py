from Resources.common import Common
import requests


class Registration(Common):

    def send_post_register_user_request(self, email, password):
        headers = {"Content-Type": "application/json"}
        json_data = {"email": email, "password": password}
        response = requests.post(self.BASE_URL + self.REGISTER_ENDPOINT, headers=headers, json=json_data)
        return response
