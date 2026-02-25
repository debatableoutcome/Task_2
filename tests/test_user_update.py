import allure
import pytest

from helpers import user
from helpers.utils import random_email
from data.user_data import (
    update_email_payload,
    update_name_payload,
    update_password_payload,
    update_payloads_without_auth,
    UPDATED_NAME,
    UPDATED_PASSWORD,
    login_payload
)
from data.error_messages import ApiErrors


@allure.suite('Изменение данных пользователя')
class TestUserUpdate:

    @allure.title('Изменение email с авторизацией')
    def test_update_email_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        payload = update_email_payload(random_email())

        response = user.update_user(api_session, token, payload)
        data = response.json()

        assert response.status_code == 200
        assert data['success'] is True
        assert data['user']['email'] == payload['email']


    @allure.title('Изменение name с авторизацией')
    def test_update_name_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        payload = update_name_payload(UPDATED_NAME)

        response = user.update_user(api_session, token, payload)
        data = response.json()

        assert response.status_code == 200
        assert data['success'] is True
        assert data['user']['name'] == payload['name']


    @allure.title('Изменение password с авторизацией')
    def test_update_password_with_auth(self, api_session, registered_user):

        token = registered_user['token']
        new_password = UPDATED_PASSWORD
        payload = update_password_payload(new_password)

        response = user.update_user(api_session, token, payload)
        data = response.json()

        assert response.status_code == 200
        assert data['success'] is True

        login = login_payload(registered_user['email'], new_password)
        login_response = user.login_user(api_session, login)
        login_data = login_response.json()

        assert login_response.status_code == 200
        assert login_data['success'] is True


    @pytest.mark.parametrize('payload', update_payloads_without_auth())
    @allure.title('Изменение данных без авторизации возвращает ошибку')
    def test_update_user_without_auth_error(self, api_session, payload):

        response = user.update_user_without_auth(api_session, payload)
        data = response.json()

        assert response.status_code == 401
        assert data['success'] is False
        assert ApiErrors.UNAUTHORIZED in response.text

