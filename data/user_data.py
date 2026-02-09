from helpers.utils import random_email


def new_user_payload():
    return {
        'email': random_email(),
        'password': 'Test1234',
        'name': 'Test User'
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
