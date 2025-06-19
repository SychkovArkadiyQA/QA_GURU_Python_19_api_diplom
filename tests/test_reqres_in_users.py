from jsonschema import validate
from schemas.user import get_user, post_user, put_user
import allure
import requests

endpoint = '/users/'

@allure.feature("Пользователь")
@allure.story("Получение данных о пользователе")
@allure.title("Получение данных о существующем пользователе")
def test_get_single_user(base_url, headers):
    with allure.step('Отправление запроса'):
        id_user = 4
        url = base_url
        response = requests.get(f'{url}{endpoint}{id_user}', headers=headers)

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['data']['id'] == id_user
        validate(response.json(), get_user)


@allure.feature("Пользователь")
@allure.story("Создание нового пользователя")
@allure.title("Успешное создание нового пользователя")
def test_post_create_user(base_url, headers):
    with allure.step('Отправление запроса'):
        payload = {
            "name": "Jhon",
            "job": "team-leader"
        }
        url = base_url
        response = requests.post(f'{url}{endpoint}', data=payload, headers=headers)

    with allure.step('Проверка кода'):
        assert response.status_code == 201

    with allure.step('Проверка ответа'):
        assert response.json()['name'] == payload['name']
        assert response.json()['job'] == payload['job']
        validate(response.json(), post_user)


@allure.feature("Пользователь")
@allure.story("Редактирование пользователя")
@allure.title("Редактирование существующего пользователя")
def test_put_user(base_url, headers):
    with allure.step('Отправление запроса'):
        id_user = 4
        payload = {
            "name": "Mark",
            "job": "team-leader"
        }
        url = base_url
        response = requests.put(f'{url}{endpoint}{id_user}', data=payload, headers=headers)

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['name'] == payload['name']
        assert response.json()['job'] == payload['job']
        validate(response.json(), put_user)


@allure.feature("Пользователь")
@allure.story("Удаление пользователя")
@allure.title("Удаление существующего пользователя")
def test_delete_user(base_url, headers):
    with allure.step('Отправление запроса'):
        id_user = 4
        url = base_url
        response = requests.delete(f'{url}{endpoint}{id_user}', headers=headers)

    with allure.step('Проверка кода'):
        assert response.status_code == 204

    with allure.step('Проверка ответа'):
        assert response.text == ''