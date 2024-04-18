from celery import shared_task
from users.utils import change_is_pay, claener_token


@shared_task
def change_is_pays():
    change_is_pay()


@shared_task
def claener_tokens():
    claener_token()
