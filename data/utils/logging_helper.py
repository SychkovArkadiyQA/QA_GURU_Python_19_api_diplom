import json
import logging
import allure
from allure_commons.types import AttachmentType


def logging_helper(result):
    request_body = result.request.body

    allure.attach(body=result.request.method + " " + result.request.url, name="Request",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=request_body if request_body else "{}", name="Request Body",
                  attachment_type=AttachmentType.TEXT, extension="json")
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info(result.request.url)
    logging.info(result.status_code)
    logging.info(result.text)