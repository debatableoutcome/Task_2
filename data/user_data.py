from helpers.utils import random_email

DEFAULT_USER_NAME = 'Test User'
WRONG_LOGIN_EMAIL = 'wrong@test.ru'
WRONG_LOGIN_PASSWORD = 'Wrong1234'
UPDATED_NAME = 'New Name'
UPDATED_PASSWORD = 'NewPass1234'
NO_AUTH_NAME = 'No Auth Name'
NO_AUTH_EMAIL = 'noauth@test.ru'
NO_AUTH_PASSWORD = 'NoAuth1234'
INVALID_INGREDIENT_ID = 'wrong_id_123'


def new_user_payload():
    return {
        'email': random_email(),
        'password': 'Test1234',
        'name': DEFAULT_USER_NAME
    }


def user_payload_without_field(field_name):
    payload = new_user_payload()
    payload.pop(field_name, None)
    return payload


def login_payload(email, password):
    return {
        'email': email,
        'password': password
    }


def update_email_payload(new_email):
    return {'email': new_email}


def update_name_payload(new_name):
    return {'name': new_name}


def update_password_payload(new_password):
    return {'password': new_password}


def order_payload(ingredient_ids):
    return {'ingredients': ingredient_ids}


def existing_user_payload(email, password, name=DEFAULT_USER_NAME):
    return {
        'email': email,
        'password': password,
        'name': name
    }


def wrong_login_payload():
    return login_payload(WRONG_LOGIN_EMAIL, WRONG_LOGIN_PASSWORD)


def update_payloads_without_auth():
    return [
        update_name_payload(NO_AUTH_NAME),
        update_email_payload(NO_AUTH_EMAIL),
        update_password_payload(NO_AUTH_PASSWORD),
    ]
