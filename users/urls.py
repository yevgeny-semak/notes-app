from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.views import LoginUserView, LogoutUserView, RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="user_register"),
    path('logout/', LogoutUserView.as_view(), name='user_logout'),
    path('token/obtain/', LoginUserView.as_view(), name='token_obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
