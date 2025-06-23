import os
import dotenv
from dotenv import load_dotenv
import requests

from core.utils.logging_helper import logging_helper

load_dotenv()
header = os.getenv("HEADER")
token = os.getenv("TOKEN")

url_ = os.getenv('URL')
headers = {
    header: token
}

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

def get_unknown(id_user):
    response = base_api(method="GET", endpoint=f"/unknown/{id_user}")
    return response

def get_users(id_user):
    response = base_api(method="GET", endpoint=f"/users/{id_user}")
    return response

def post_users(payload):
    response = base_api(method="POST", endpoint=f"/users/", json=payload)
    return response

def put_users(id_user, payload):
    response = base_api(method="PUT", endpoint=f"/users/{id_user}", json=payload)
    return response

def delete_users(id_user):
    response = base_api(method="DELETE", endpoint=f"/users/{id_user}")
    return response
