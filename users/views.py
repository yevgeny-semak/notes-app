from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users import serializers


class CustomUserRegisterView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        serializer = serializers.CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            data = serializer.data
            return Response({'user': data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TokenObtainPairWithUserInfoView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CustomTokenObtainPairSerializer


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        try:
            token_refresh = request.data["token_refresh"]
            token = RefreshToken(token_refresh)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
