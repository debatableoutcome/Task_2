import allure
from config.urls import ORDERS_URL


@allure.step('Create order')
def create_order(session, payload, token=None):
    headers = None

    if token:
        headers = {'Authorization': token}

    return session.post(ORDERS_URL, json=payload, headers=headers)


@allure.step('Get user orders')
def get_orders(session, token=None):
    headers = None

    if token:
        headers = {'Authorization': token}

    return session.get(ORDERS_URL, headers=headers)


