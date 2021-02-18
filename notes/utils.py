import requests
import os


def get_bacon_ipsum_content():
    url = os.getenv('BACON_URL')

    querystring = {'type': 'all-meat', 'paras': '1', 'start-with-lorem': '1', 'format': 'json'}

    headers = {
        'x-rapidapi-key': os.getenv('BACON_KEY'),
        'x-rapidapi-host': os.getenv('BACON_HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text[2:-2]
