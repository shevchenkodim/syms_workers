from django.urls import path
from rest_framework import routers
from api.view_modules.auth.base_auth import BaseAuth
from api.view_modules.frontend.products import NoveltiesViewSet
from api.view_modules.auth.simple_jwt_view import Verify, Refresh
from api.view_modules.frontend.categories import CategoriesViewSet
from api.view_modules.frontend.main_slider import MainSliderImagesViewSet


router = routers.DefaultRouter()
router.register(r'novelties', NoveltiesViewSet, basename='novelties')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'slider/main/images', MainSliderImagesViewSet, basename='sliders')

urlpatterns = [
    path('auth/login', BaseAuth.as_view(), name='auth'),
    path('auth/verify', Verify.as_view(), name='verify'),
    path('auth/refresh', Refresh.as_view(), name='refresh'),
]

urlpatterns += router.urls
