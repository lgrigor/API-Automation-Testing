from Resources.common import Common
import requests
import json


class User(Common):

    def send_get_user_list_request(self, page=1):
        response = requests.get(self.BASE_URL + self.LIST_USERS_ENDPOINT.format(page))
        return response

    def send_get_single_user_request(self, user_id):
        response = requests.get(self.BASE_URL + self.SINGLE_USER_ENDPOINT.format(user_id))
        return response

    def send_post_create_user_request(self, name, job):
        headers = {"Content-Type": "application/json;"}
        json_body = json.dumps({"name": name, "job": job}, indent=2)
        response = requests.post(self.BASE_URL + self.CREATE_USER_ENDPOINT, headers=headers, json=json_body)
        return response

    def send_put_update_user_request(self, user_id, new_name, new_job):
        headers = {"Content-Type": "application/json"}
        json_data = {"name": new_name, "job": new_job}
        response = requests.put(self.BASE_URL + self.UPDATE_USER_ENDPOINT.format(user_id), headers=headers, json=json_data)
        return response

    def send_patch_update_user_request(self, user_id, new_name=None, new_job=None):
        headers = {"Content-Type": "application/json"}
        json_data = {}

        if new_name:
            json_data["name"] = new_name
        if new_job:
            json_data["job"] = new_job

        response = requests.patch(self.BASE_URL + self.UPDATE_USER_ENDPOINT.format(user_id), headers=headers, json=json_data)
        return response

    def send_delete_user_request(self, user_id):
        response = requests.delete(self.BASE_URL + self.DELETE_USER_ENDPOINT.format(user_id))
        return response
