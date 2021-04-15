from django.urls import path
from rest_framework import routers
from api.view_modules.auth.base_auth import BaseAuth
from api.view_modules.auth.simple_jwt_view import Verify, Refresh

router = routers.DefaultRouter()

urlpatterns = [
    path('auth/login', BaseAuth.as_view(), name='auth'),
    path('auth/verify', Verify.as_view(), name='verify'),
    path('auth/refresh', Refresh.as_view(), name='refresh'),
]

urlpatterns += router.urls
