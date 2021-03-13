from celery import shared_task
import json


@shared_task
def add(x, y):
    return json.dump(x+y)


@shared_task
def mul(x, y):
    return json.dump(x*y)
