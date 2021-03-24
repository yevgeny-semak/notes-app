from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.views import TokenObtainPairWithUserInfoView, CustomUserRegisterView

urlpatterns = [
    path('users/register/', CustomUserRegisterView.as_view(), name="user_register"),
    path('token/obtain/', TokenObtainPairWithUserInfoView.as_view(), name='token_obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
