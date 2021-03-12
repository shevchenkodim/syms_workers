from core import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from common.view_modules.simple_jwt_view import Login, Verify, Refresh


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/login', Login.as_view(), name='login'),
    path('api/v1/auth/verify', Verify.as_view(), name='verify'),
    path('api/v1/auth/refresh', Refresh.as_view(), name='refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
