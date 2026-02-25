import allure
from config.urls import LOGIN_URL, REGISTER_URL, USER_URL

@allure.step('Register user')
def register_user(session, payload):
    return session.post(REGISTER_URL, json=payload)


@allure.step('Delete user')
def delete_user(session, token):
    headers = {'Authorization': token}
    return session.delete(USER_URL, headers=headers)

@allure.step('Login user')
def login_user(session, payload):
    return session.post(LOGIN_URL, json=payload)

@allure.step('Update user with auth')
def update_user(session, token, payload):
    headers = {'Authorization': token}
    return session.patch(USER_URL, headers=headers, json=payload)


@allure.step('Update user without auth')
def update_user_without_auth(session, payload):
    return session.patch(USER_URL, json=payload)


