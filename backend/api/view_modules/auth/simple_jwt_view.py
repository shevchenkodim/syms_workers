from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


class Verify(TokenVerifyView):
    pass


class Refresh(TokenRefreshView):
    pass
