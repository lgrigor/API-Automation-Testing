from Resources.user import User
from Resources.database import Database
import pytest
import allure


@pytest.mark.api
class TestUserManipulations(User, Database):

    @allure.title("Test View All Users List")
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_user_list(self):
        response = self.send_get_user_list_request()
        expected_content = self.send_get_user_list_query()
        assert self.verify_status_code(response, 200)
        assert self.verify_response_content(response, expected_content)

    @allure.title("Test View Single User")
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_single_user(self):
        response = self.send_get_single_user_request(2)
        expected_content = self.send_get_user_with_id_query(2)
        assert self.verify_status_code(response, 200)
        assert self.verify_response_content(response, expected_content)

    @allure.title("Test User Creation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creation(self):
        response = self.send_post_create_user_request("morpheus", "leader")
        assert self.verify_status_code(response, 201)
        assert self.verify_response_key_value_class(response, "id", int)
        assert self.verify_response_key_value_regexp(response, "createdAt", self.DATE_REGEXP)

    @allure.title("Test User Full Modification")
    @allure.severity(allure.severity_level.MINOR)
    def test_update_user_put(self):
        response = self.send_put_update_user_request(2, "neo", "chosen")
        assert self.verify_status_code(response, 200)
        assert self.verify_response_key_value_regexp(response, "name", "neo")
        assert self.verify_response_key_value_regexp(response, "job", "chosen")
        assert self.verify_response_key_value_regexp(response, "updatedAt", self.DATE_REGEXP)
        assert self.verify_response_data_length(response, 3)

    @allure.title("Test User Partial Modification")
    @allure.severity(allure.severity_level.MINOR)
    def test_update_user_patch(self):
        response = self.send_patch_update_user_request(2, "neo")
        assert self.verify_status_code(response, 200)
        assert self.verify_response_key_value_regexp(response, "name", "neo")
        assert self.verify_response_key_value_regexp(response, "updatedAt", self.DATE_REGEXP)
        assert self.verify_response_data_length(response, 2)

    @allure.title("Test User Deletion")
    @allure.severity(allure.severity_level.MINOR)
    def test_delete_user(self):
        response = self.send_delete_user_request(2)
        assert self.verify_status_code(response, 204)
