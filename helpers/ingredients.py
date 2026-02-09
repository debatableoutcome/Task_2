import allure
from config.urls import BASE_URL


@allure.step('Get ingredients list')
def get_ingredients(session):
    return session.get(f'{BASE_URL}/api/ingredients')


def take_some_ids(response, count=2):
    data = response.json()
    ids = []

    for item in data.get('data', [])[:count]:
        ids.append(item.get('_id'))

    return ids
