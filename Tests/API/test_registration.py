from Resources.registration import Registration
import pytest
import allure


@pytest.mark.api
class TestRegistration(Registration):

    @allure.title("Test User Registration")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_register_user_successful(self):
        random_password = self.generate_random_password()
        response = self.send_post_register_user_request(self.DEFINED_EMAIL, random_password)
        assert self.verify_status_code(response, 200)
        assert self.verify_response_key_value(response, "id", 4)
        assert self.verify_response_key_value_regexp(response, "token", r"\w+")
        assert self.verify_response_data_length(response, 2)

    @allure.title("Test User Registration With Undefined Email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_user_unsuccessful(self):
        random_email = self.generate_random_email()
        random_password = self.generate_random_password()
        response = self.send_post_register_user_request(random_email, random_password)
        assert self.verify_status_code(response, 400)
        assert self.verify_response_key_value(response, "error", "Note: Only defined users succeed registration")
        assert self.verify_response_data_length(response, 1)
