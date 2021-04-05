from common.models import User
from core.settings.tools import SIMPLE_JWT
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken


class CustomJWTAuth:
    """ Custom class for generate and refresh jwt token """

    @classmethod
    def get_token(cls, user: User) -> dict:
        """ Returned tokens for user """
        response = dict()

        refresh = RefreshToken.for_user(user)

        response['refresh'] = str(refresh)
        response['access'] = str(refresh.access_token)

        if SIMPLE_JWT["UPDATE_LAST_LOGIN"]:
            update_last_login(None, user)

        return response

    @classmethod
    def refresh_token(cls, token):
        """ Refresh token for user """
        refresh = RefreshToken(token)

        response = {'access': str(refresh.access_token)}

        if SIMPLE_JWT["ROTATE_REFRESH_TOKENS"]:
            if SIMPLE_JWT["BLACKLIST_AFTER_ROTATION"]:
                try:
                    refresh.blacklist()
                except AttributeError:
                    pass

            refresh.set_jti()
            refresh.set_exp()

            response['refresh'] = str(refresh)

        return response

    @classmethod
    def validate_token(cls, token):
        """ Check for validation token """
        UntypedToken(token)


jwt_auth = CustomJWTAuth()
