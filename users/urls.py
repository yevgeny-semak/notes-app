from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from users.views import AuthViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('', AuthViewSet, basename='users')

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
urlpatterns += router.urls
