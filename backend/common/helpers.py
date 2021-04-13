import random
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class ApiException(Exception):
    def __init__(self, error: str):
        self.error = error


def json_response(success, response, status=HTTP_200_OK):
    """ Returned json response with code status """
    return Response({
        'success': success,
        'response': response
    }, status=status)


class GenerateOtpCode(object):
    """ class for generation otp code """

    @staticmethod
    def get_random():
        return random.randint(1000, 9999)
