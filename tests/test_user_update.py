import allure
import pytest

from helpers import user
from data.user_data import update_email_payload, update_name_payload, update_password_payload
from helpers.utils import random_email


class TestUserUpdate:

    @allure.title('Изменение email с авторизацией')
    def test_update_email_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        new_email = random_email()
        payload = update_email_payload(new_email)

        response = user.update_user(api_session, token, payload)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == new_email


    @allure.title('Изменение name с авторизацией')
    def test_update_name_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        payload = update_name_payload('New Name')

        response = user.update_user(api_session, token, payload)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['name'] == 'New Name'


    @allure.title('Изменение password с авторизацией')
    def test_update_password_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        new_password = 'NewPass1234'
        payload = update_password_payload(new_password)

        response = user.update_user(api_session, token, payload)

        assert response.status_code == 200
        assert response.json()['success'] is True

        
        login_payload = {
            'email': registered_user['email'],
            'password': new_password
        }
        login_response = user.login_user(api_session, login_payload)

        assert login_response.status_code == 200
        assert login_response.json()['success'] is True


    @pytest.mark.parametrize('payload', [
        update_name_payload('No Auth Name'),
        update_password_payload('NoAuth1234'),
        update_email_payload('noauth@test.ru'),
    ])
    @allure.title('Изменение данных без авторизации возвращает ошибку')
    def test_update_user_without_auth_error(self, api_session, payload):

        response = user.update_user_without_auth(api_session, payload)

        assert response.status_code == 401
        assert response.json()['success'] is False
