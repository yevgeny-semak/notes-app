import json

from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoginTest(APITestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='test@localhost', password='1234', username='test')

    def test_login_with_valid_payload(self):
        response = self.client.post(
            reverse('auth-login'),
            data=json.dumps({'email': 'test@localhost', 'password': '1234'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_email(self):
        response = self.client.post(
            reverse('auth-login'),
            data=json.dumps({'email': 'test1@localhost', 'password': '4242'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_invalid_password(self):
        response = self.client.post(
            reverse('auth-login'),
            data=json.dumps({'email': 'test@localhost', 'password': '4242'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RegisterTest(APITestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='test@localhost', password='1234', username='test')

    def test_register_with_valid_payload(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_invalid_email(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test@localhost', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_password(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test@localhost', 'password': 'test1234', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_username(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test1234', 'username': 'test'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_email(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': '', 'password': 'test4321', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_password(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test@localhost', 'password': '', 'username': 'test1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_empty_username(self):
        response = self.client.post(
            reverse('auth-register'),
            data=json.dumps({'email': 'test1@localhost', 'password': 'test1234', 'username': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LogoutTest(APITestCase):
    pass


class PasswordChangeTest(APITestCase):
    pass
