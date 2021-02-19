import requests
import os

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


def get_bacon_ipsum_content():
    url = os.getenv('BACON_URL')

    querystring = {'type': 'all-meat', 'paras': '1', 'start-with-lorem': '1', 'format': 'json'}

    headers = {
        'x-rapidapi-key': os.getenv('BACON_KEY'),
        'x-rapidapi-host': os.getenv('BACON_HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text[2:-2]


def authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError('Invalid username/password. Please try again!')
    return user


def create_user_account(email, password, username, **extra_fields):
    user = get_user_model().objects.create_user(email=email, password=password, username=username, **extra_fields)
    return user
