from Resources.login import Login
import allure
import pytest


@pytest.mark.api
class TestLogin(Login):

    @allure.title("Test Login")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_user_successful(self):
        response = self.send_post_login_request(self.DEFINED_EMAIL, self.DEFINED_PASSWORD)
        assert self.verify_status_code(response, 200)
        assert self.verify_response_key_exists(response, "token")
        assert self.verify_response_data_length(response, 1)

    @allure.title("Test Login Without Password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_missing_password(self):
        response = self.send_post_login_request(self.DEFINED_EMAIL, None)
        assert self.verify_status_code(response, 400)
        assert self.verify_response_key_value(response, "error", "Missing password")
        assert self.verify_response_data_length(response, 1)

    @allure.title("Test Login Without Email, Password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_missing_both(self):
        response = self.send_post_login_request(None, None)
        assert self.verify_status_code(response, 400)
        assert self.verify_response_key_value(response, "error", "Missing email or username")
        assert self.verify_response_data_length(response, 1)

    @allure.title("Test Login With Undefined Email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_undefined_email(self):
        random_email = self.generate_random_email()
        random_password = self.generate_random_password()
        response = self.send_post_login_request(random_email, random_password)
        assert self.verify_status_code(response, 400)
        assert self.verify_response_key_value(response, "error", "user not found")
        assert self.verify_response_data_length(response, 1)
