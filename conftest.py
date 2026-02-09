import pytest
import requests
import allure

from helpers import user
from data.user_data import new_user_payload
from config.urls import BASE_URL


@pytest.fixture
def api_session():
    """
    Базовая сессия для всех запросов
    """
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    return session


@pytest.fixture
def registered_user(api_session):
    """
    Фикстура:
    1. Создаёт уникального пользователя
    2. Отдаёт данные в тест
    3. После теста удаляет пользователя
    """

    with allure.step('Подготовка: создание пользователя для теста'):
        payload = new_user_payload()
        response = user.register_user(api_session, payload)

        data = response.json()

        access_token = data.get('accessToken')

        user_data = {
            'email': payload['email'],
            'password': payload['password'],
            'token': access_token
        }

    yield user_data

    with allure.step('Очистка: удаление тестового пользователя'):
        if access_token:
            user.delete_user(api_session, access_token)


@pytest.fixture
def auth_token(registered_user):
    """
    Отдельная фикстура только для токена
    """
    return registered_user['token']
