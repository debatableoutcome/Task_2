import allure
from config.urls import BASE_URL

@allure.step('Register user')
def register_user(session, payload):
    return session.post(f'{BASE_URL}/api/auth/register', json=payload)


@allure.step('Delete user')
def delete_user(session, token):
    headers = {'Authorization': token}
    return session.delete(f'{BASE_URL}/api/auth/user', headers=headers)

@allure.step('Login user')
def login_user(session, payload):
    return session.post(f'{BASE_URL}/api/auth/login', json=payload)

@allure.step('Update user with auth')
def update_user(session, token, payload):
    headers = {'Authorization': token}
    return session.patch(f'{BASE_URL}/api/auth/user', headers=headers, json=payload)


@allure.step('Update user without auth')
def update_user_without_auth(session, payload):
    return session.patch(f'{BASE_URL}/api/auth/user', json=payload)


