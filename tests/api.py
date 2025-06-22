import requests

from data.utils.logging_helper import logging_helper

url_ = 'https://reqres.in/api'
headers = {
    "x-api-key": "reqres-free-v1"}


def base_api(method, endpoint, **kwargs):
    url = f"{url_}{endpoint}"
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        **kwargs
    )
    logging_helper(response)
    return response


def post_login(payload):
    response = base_api(method="POST", endpoint="/login/", json=payload)
    return response

def post_register(payload):
    response = base_api(method="POST", endpoint="/register/", json=payload)
    return response
