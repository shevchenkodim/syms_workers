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


def validate_price(val, default=0):
    """ Validate any price """
    try:
        return int(val)
    except Exception as e:
        print(e.__str__())
        return default
