from jsonschema import validate
import json
import allure
import requests
from data.utils import path
from tests.api import get_unknown

@allure.feature("Получение данных о товаре")
@allure.story("Получение данных об одном товаре")
@allure.title("Получение данных о существующем товаре")
def test_get_single_resource():
    with allure.step('Отправление запроса'):
        id_user = 4
        response = get_unknown(id_user)

    with allure.step('Проверка кода'):
        assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.json()['data']['id'] == id_user

    with allure.step('Проверка схемы'):
        schema_path = path.abs_path_from_project('schemas/resource.json')
        with open(schema_path) as file:
            schema = json.load(file)
        validate(response.json(), schema)


@allure.feature("Получение данных о товаре")
@allure.story("Получение данных об одном товаре")
@allure.title("Проверка ошибки при получении данных о несуществующем товаре")
def test_get_single_resource_not_found():
    with allure.step('Отправление запроса'):
        id_user = 45
        response = get_unknown(id_user)

    with allure.step('Проверка кода'):
        assert response.status_code == 404

    with allure.step('Проверка ответа'):
        assert response.json() == {}