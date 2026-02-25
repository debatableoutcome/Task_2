import pytest
import requests
import allure

from helpers import user
from data.user_data import new_user_payload


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    return session


@pytest.fixture
def registered_user(api_session):
    access_token = None
    payload = new_user_payload()

    with allure.step('Setup: create a test user'):
        response = user.register_user(api_session, payload)
        if response.status_code != 200:
            pytest.fail(f'Failed to create test user in fixture: {response.status_code} {response.text}')
        data = response.json()
        access_token = data.get('accessToken')
        if not access_token:
            pytest.fail('Failed to create test user in fixture: missing accessToken')

    user_data = {
        'email': payload['email'],
        'password': payload['password'],
        'token': access_token
    }

    yield user_data

    with allure.step('Teardown: delete the test user'):
        if access_token:
            user.delete_user(api_session, access_token)
