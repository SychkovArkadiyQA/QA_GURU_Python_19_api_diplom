import pytest


@pytest.fixture()
def base_url():
    base_url = 'https://reqres.in/api'

    return base_url

@pytest.fixture
def headers():
    headers = {
        "x-api-key": "reqres-free-v1"}
    return headers

