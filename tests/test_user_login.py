import allure

from helpers import user
from data.user_data import login_payload
from data.error_messages import ApiErrors


@allure.suite('Логин пользователя')
class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_success(self, api_session, registered_user):

        payload = login_payload(
            registered_user['email'],
            registered_user['password']
        )

        response = user.login_user(api_session, payload)

        data = response.json()

        assert response.status_code == 200
        assert data['success'] is True
        assert 'accessToken' in data


    @allure.title('Логин с неверным логином и паролем')
    def test_login_wrong_credentials_error(self, api_session):

        payload = login_payload('wrong@test.ru', 'Wrong1234')

        response = user.login_user(api_session, payload)

        data = response.json()

        assert response.status_code == 401
        assert data['success'] is False
        assert ApiErrors.INVALID_CREDENTIALS in response.text
