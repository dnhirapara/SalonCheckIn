from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status


class IsNotSalonOwner(APIException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = 'You are not Salon Owner.'
    default_field = 'error'

    def __init__(self, detail, field, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else:
            self.detail = {default_field: force_text(self.default_detail)}
