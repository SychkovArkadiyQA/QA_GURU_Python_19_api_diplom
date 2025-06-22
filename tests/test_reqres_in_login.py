import json
from jsonschema import validate
import re
import allure
from data.utils import path
import requests
from tests.api import post_login


@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя")
@allure.title("Успешная авторизация пользователя")
def test_post_login_success():
    with allure.step('Отправление запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        response = post_login(payload)
        token = response.json().get("token")
        token_pattern = r"^[A-Za-z0-9]+$"

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка токена'):
        assert re.match(token_pattern, token)

    with allure.step('Проверка схемы'):
        schema_path = path.abs_path_from_project('schemas/login.json')
        with open(schema_path) as file:
            schema = json.load(file)
        validate(response.json(), schema)

@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя")
@allure.title("Неуспешная авторизация пользователя")
def test_post_login_fail():
    with allure.step('Отправление запроса'):
        payload = {
            "email": "petya@gmail"
        }
        response = post_login(payload)

        with allure.step('Проверка кода'):
            assert response.status_code == 400

        with allure.step('Проверка текста ошибки'):
            assert response.json()['error'] == "Missing password"