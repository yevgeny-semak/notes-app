import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class RegisterTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@localhost', password='1234', username='test')

    def test_register_with_valid_payload(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_invalid_email(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test@localhost', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_password(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test@localhost', 'password': 'test1234', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_username(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test1234', 'username': 'test'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_email(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': '', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_password(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test@localhost', 'password': '', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_username(self):
        response = self.client.post(
            reverse('user_register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test1234', 'username': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ObtainTokenTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@localhost', password='1234', username='test')

    def test_obtain_token_with_valid_payload(self):
        response = self.client.post(
            reverse('token_obtain'),
            data=json.dumps({'email': 'test@localhost', 'password': '1234'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obtain_token_with_invalid_email(self):
        response = self.client.post(
            reverse('token_obtain'),
            data=json.dumps({'email': 'test1@localhost', 'password': '4242'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_obtain_token_with_invalid_password(self):
        response = self.client.post(
            reverse('token_obtain'),
            data=json.dumps({'email': 'test@localhost', 'password': '4242'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RefreshTokenTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@localhost', password='1234', username='test')
        self.token_refresh = self.client.post(
            reverse('token_obtain'),
            data=json.dumps({'email': 'test@localhost', 'password': '1234'}),
            content_type='application/json'
        ).data.pop('refresh')

    def test_refresh_token_with_valid_payload(self):
        response = self.client.post(
            reverse('token_refresh'),
            data=json.dumps({'refresh': self.token_refresh}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token_with_invalid_refresh_token(self):
        response = self.client.post(
            reverse('token_refresh'),
            data=json.dumps({'refresh': 'random_value'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
