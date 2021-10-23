from django.urls import path
from rest_framework import routers
from api.view_modules.auth.base_auth import BaseAuth
from api.view_modules.frontend.cart import CartViewSet
from api.view_modules.frontend.comments import CommentViewSet
from api.view_modules.frontend.order import OrderViewSet
from api.view_modules.frontend.search import SearchViewSet
from api.view_modules.frontend.users import UserViewSet
from api.view_modules.frontend.seller import SellerViewSet
from api.view_modules.auth.simple_jwt_view import Verify, Refresh
from api.view_modules.frontend.categories import CategoriesViewSet
from api.view_modules.frontend.main_slider import MainSliderImagesViewSet
from api.view_modules.frontend.products import NoveltiesViewSet, ProductsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'search', SearchViewSet, basename='search')
router.register(r'novelties', NoveltiesViewSet, basename='novelties')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'sellers', SellerViewSet, basename='sellers')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'slider/main/images', MainSliderImagesViewSet, basename='sliders')

urlpatterns = [
    path('auth/login', BaseAuth.as_view(), name='auth'),
    path('auth/verify', Verify.as_view(), name='verify'),
    path('auth/refresh', Refresh.as_view(), name='refresh'),
]

urlpatterns += router.urls
