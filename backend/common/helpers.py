from rest_framework.response import Response


class ApiException(Exception):
    def __init__(self, error: str):
        self.error = error


def json_response(success, response, status):
    """ Returned json response with code status """
    return Response({
        'success': success,
        'response': response
    }, status=status)
