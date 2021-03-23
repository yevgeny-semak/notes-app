from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users import serializers


class TokenObtainPairWithUserInfoView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CustomTokenObtainPairSerializer


class CustomUserRegisterView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serializer = serializers.CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        if user:
            data = serializer.data
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
