from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users import serializers


class RegisterUserView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        serializer = serializers.CustomUserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LogoutUserView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        try:
            token_refresh = request.data['refresh']
            token = RefreshToken(token_refresh)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
