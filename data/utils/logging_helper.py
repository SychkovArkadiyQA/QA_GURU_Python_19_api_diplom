import json
import logging
import allure
from allure_commons.types import AttachmentType


def logging_helper(result):
    """Логирует запросы и ответы с обработкой пустых ответов (204)"""
    try:
        # Логирование запроса
        allure.attach(
            body=f"{result.request.method} {result.request.url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        # Логирование тела запроса (если есть)
        request_body = result.request.body or "{}"
        allure.attach(
            body=request_body,
            name="Request Body",
            attachment_type=allure.attachment_type.JSON
        )

        # Логирование ответа (с обработкой 204)
        response_data = {} if result.status_code == 204 else result.json()
        allure.attach(
            body=json.dumps(response_data, indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        # Логирование в console
        logging.info(f"URL: {result.request.url}")
        logging.info(f"Status: {result.status_code}")
        logging.info(f"Response: {result.text[:200]}...")  # Логируем первые 200 символов

    except Exception as e:
        logging.error(f"Logging error: {str(e)}")
        allure.attach(
            body=f"Logging failed: {str(e)}",
            name="Logging Error",
            attachment_type=allure.attachment_type.TEXT
        )