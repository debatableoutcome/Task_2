import allure

from helpers import user
from data.error_messages import ApiErrors
from data.user_data import existing_user_payload, new_user_payload, user_payload_without_field


@allure.suite('Регистрация пользователя')
class TestUserRegister:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user_success(self, api_session, registered_user):


        assert registered_user['token'] is not None


    @allure.title('Нельзя создать пользователя, который уже существует')
    def test_create_existing_user_error(self, api_session, registered_user):

        payload = existing_user_payload(registered_user['email'], registered_user['password'])

        response = user.register_user(api_session, payload)

        data = response.json()

        assert response.status_code == 403
        assert data.get('success') is False
        assert ApiErrors.USER_ALREADY_EXISTS in response.text


    @allure.title('Ошибка при отсутствии обязательного поля')
    def test_create_user_without_required_field(self, api_session):

        payload = user_payload_without_field('email')

        response = user.register_user(api_session, payload)

        data = response.json()

        assert response.status_code == 403
        assert data.get('success') is False
        assert ApiErrors.REQUIRED_FIELDS in response.text

