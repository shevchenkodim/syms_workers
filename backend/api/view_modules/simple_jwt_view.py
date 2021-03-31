from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView


class Login(TokenObtainPairView):
    pass


class Verify(TokenVerifyView):
    pass


class Refresh(TokenRefreshView):
    pass
