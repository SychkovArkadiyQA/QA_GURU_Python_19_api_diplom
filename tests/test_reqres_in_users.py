from jsonschema import validate
from resources.schemas.user import get_user, post_user, put_user
import allure
from core.reqeust_api import get_users, post_users, put_users, delete_users

@allure.feature("Пользователь")
@allure.story("Получение данных о пользователе")
@allure.title("Получение данных о существующем пользователе")
def test_get_single_user():
    with allure.step('Отправление запроса'):
        id_user = 4
        response = get_users(id_user)

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['data']['id'] == id_user
        validate(response.json(), get_user)


@allure.feature("Пользователь")
@allure.story("Создание нового пользователя")
@allure.title("Успешное создание нового пользователя")
def test_post_create_user():
    with allure.step('Отправление запроса'):
        payload = {
            "name": "John",
            "job": "team-leader"
        }
        response = post_users(payload)

    with allure.step('Проверка кода'):
        assert response.status_code == 201

    with allure.step('Проверка ответа'):
        assert response.json()['name'] == payload['name']
        assert response.json()['job'] == payload['job']
        validate(response.json(), post_user)


@allure.feature("Пользователь")
@allure.story("Редактирование пользователя")
@allure.title("Редактирование существующего пользователя")
def test_put_user():
    with allure.step('Отправление запроса'):
        id_user = 4
        payload = {
            "name": "Mark",
            "job": "team-leader"
        }
        response = put_users(id_user, payload)

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['name'] == payload['name']
        assert response.json()['job'] == payload['job']
        validate(response.json(), put_user)


@allure.feature("Пользователь")
@allure.story("Удаление пользователя")
@allure.title("Удаление существующего пользователя")
def test_delete_user():
    with allure.step('Отправление запроса'):
        id_user = 4
        response = delete_users(id_user)

    with allure.step('Проверка кода'):
        assert response.status_code == 204

    with allure.step('Проверка ответа'):
        assert response.text == ''