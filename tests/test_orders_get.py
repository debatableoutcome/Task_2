import allure

from helpers import orders
from data.error_messages import ApiErrors

@allure.suite('Получение заказов')
class TestOrdersGet:

    @allure.title('Получение заказов авторизованным пользователем')
    def test_get_orders_with_auth(self, api_session, registered_user):

        response = orders.get_orders(api_session, registered_user['token'])

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'orders' in response.json()


    @allure.title('Ошибка при получении заказов без авторизации')
    def test_get_orders_without_auth(self, api_session):

        response = orders.get_orders(api_session)

        assert response.status_code == 401
        assert response.json()['success'] is False
        assert ApiErrors.UNAUTHORIZED in response.text
