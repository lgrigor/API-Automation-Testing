

class Data:

    BASE_URL = "https://reqres.in"

    LIST_USERS_ENDPOINT = "/api/users?page={}"
    SINGLE_USER_ENDPOINT = "/api/users/{}"
    CREATE_USER_ENDPOINT = "/api/users"
    UPDATE_USER_ENDPOINT = "/api/users/{}"
    DELETE_USER_ENDPOINT = "/api/users/{}"

    REGISTER_ENDPOINT = "/api/register"
    LOGIN_ENDPOINT = "/api/login"

    DEFINED_EMAIL = "eve.holt@reqres.in"
    DEFINED_PASSWORD = 'cityslicka'
    DATE_REGEXP = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"
