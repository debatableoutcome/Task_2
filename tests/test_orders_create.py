import allure

from helpers import orders, ingredients
from data.user_data import order_payload


class TestOrdersCreate:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth(self, api_session, registered_user):

        ingr_resp = ingredients.get_ingredients(api_session)
        ids = ingredients.take_some_ids(ingr_resp)

        payload = order_payload(ids)

        response = orders.create_order(
            api_session,
            payload,
            registered_user['token']
        )

        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Создание заказа без авторизации с ингредиентами')
    def test_create_order_without_auth(self, api_session):

        ingr_resp = ingredients.get_ingredients(api_session)
        ids = ingredients.take_some_ids(ingr_resp)

        payload = order_payload(ids)

        response = orders.create_order(api_session, payload)

        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Ошибка 400 при создании заказа без ингредиентов')
    def test_create_order_without_ingredients(self, api_session, registered_user):

        payload = order_payload([])

        response = orders.create_order(
            api_session,
            payload,
            registered_user['token']
        )

        assert response.status_code == 400

        data = response.json()

        assert data['success'] is False
        assert data['message'] == 'Ingredient ids must be provided'


    @allure.title('Ошибка 500 при неверном хеше ингредиентов')
    def test_create_order_with_wrong_hash(self, api_session, registered_user):

        payload = order_payload(['wrong_id_123'])

        with allure.step('Отправляем заказ с невалидным хешем ингредиента'):
            response = orders.create_order(
                api_session,
                payload,
                registered_user['token']
            )

        with allure.step('Ожидаем 500 согласно документации API'):
            assert response.status_code == 500, (
                f'По документации должен быть 500, но стенд вернул {response.status_code}'
            )



