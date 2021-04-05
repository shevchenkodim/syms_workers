from django.urls import path
from rest_framework import routers
from .view_modules.base_auth import BaseAuth
from api.view_modules.simple_jwt_view import Login, Verify, Refresh

router = routers.DefaultRouter()

urlpatterns = [
    path('login', BaseAuth.as_view(), name='auth'),
    path('verify', Verify.as_view(), name='verify'),
    path('refresh', Refresh.as_view(), name='refresh'),
]

urlpatterns += router.urls
