import allure
from config.urls import BASE_URL


@allure.step('Create order')
def create_order(session, payload, token=None):
    headers = None

    if token:
        headers = {'Authorization': token}

    return session.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)


@allure.step('Get user orders')
def get_orders(session, token=None):
    headers = None

    if token:
        headers = {'Authorization': token}

    return session.get(f'{BASE_URL}/api/orders', headers=headers)


