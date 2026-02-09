import allure
from helpers import user
from data.user_data import new_user_payload, user_payload_without_field


class TestUserRegister:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user_success(self, api_session):

        payload = new_user_payload()

        response = user.register_user(api_session, payload)

        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Нельзя создать пользователя, который уже существует')
    def test_create_existing_user_error(self, registered_user, api_session):

        # пробуем зарегистрировать того же пользователя ещё раз
        payload = {
            'email': registered_user['email'],
            'password': registered_user['password'],
            'name': 'Test User'
        }

        response = user.register_user(api_session, payload)

        assert response.status_code == 403
        assert 'User already exists' in response.text


    @allure.title('Ошибка при отсутствии обязательного поля')
    def test_create_user_without_required_field(self, api_session):

        payload = user_payload_without_field('email')

        response = user.register_user(api_session, payload)

        assert response.status_code == 403
        assert 'required fields' in response.text
