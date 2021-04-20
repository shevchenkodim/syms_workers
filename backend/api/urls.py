from django.urls import path
from rest_framework import routers
from api.view_modules.auth.base_auth import BaseAuth
from api.view_modules.auth.simple_jwt_view import Verify, Refresh
from api.view_modules.frontend.main_slider import MainSliderImagesViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('auth/login', BaseAuth.as_view(), name='auth'),
    path('auth/verify', Verify.as_view(), name='verify'),
    path('auth/refresh', Refresh.as_view(), name='refresh'),

    path('slider/main/images', MainSliderImagesViewSet.as_view(), name='slides_main_images'),
]

urlpatterns += router.urls
