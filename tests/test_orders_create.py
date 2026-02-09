import allure

from helpers import orders, ingredients
from data.user_data import order_payload
from data.error_messages import ApiErrors


@allure.suite('Создание заказов')
class TestOrdersCreate:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth(self, api_session, registered_user):

        ingr_resp = ingredients.get_ingredients(api_session)
        ids = ingredients.take_some_ids(ingr_resp)

        response = orders.create_order(
            api_session,
            order_payload(ids),
            registered_user['token']
        )

        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Создание заказа без авторизации с ингредиентами')
    def test_create_order_without_auth(self, api_session):

        ingr_resp = ingredients.get_ingredients(api_session)
        ids = ingredients.take_some_ids(ingr_resp)

        response = orders.create_order(api_session, order_payload(ids))

        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, api_session, registered_user):

        response = orders.create_order(
            api_session,
            order_payload([]),
            registered_user['token']
        )

        assert response.status_code == 400
        assert ApiErrors.NO_INGREDIENTS in response.text


    @allure.title('Ошибка при создании заказа с неверным хешем ингредиентов')
    @allure.description('API возвращает 400 и сообщение об ошибке при невалидных id ингредиентов')

    def test_create_order_with_wrong_hash(self, api_session, registered_user):

        payload = order_payload(['wrong_id_123'])

        response = orders.create_order(
            api_session,
            payload,
            registered_user['token']
        )

        with allure.step('Проверяем фактический ответ стенда'):
            data = response.json()
            assert response.status_code == 400
            assert data.get('success') is False

        with allure.step('Проверяем текст ошибки'):
            assert data.get('message') == ApiErrors.INVALID_INGREDIENTS
