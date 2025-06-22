import json
import logging
import allure
from allure_commons.types import AttachmentType

def logging_helper(response):
    try:
        # Для ответов без содержимого (204)
        if response.status_code == 204:
            allure.attach(
                body=f"Empty response (Status: {response.status_code})",
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )
            return

        # Для ответов с содержимым
        response_json = response.json()
        allure.attach(
            body=json.dumps(response_json, indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )
    except ValueError:
        allure.attach(
            body=response.text,
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )