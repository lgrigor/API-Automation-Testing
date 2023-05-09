from Resources.common import Common
import requests


class Login(Common):

    def send_post_login_request(self, email, password):
        headers = {"Content-Type": "application/json"}
        json_data = {"email": email, "password": password}
        response = requests.post(self.BASE_URL + self.LOGIN_ENDPOINT, headers=headers, json=json_data)
        return response
