import requests


def get_bacon_ipsum_content():
    url = "https://baconator-bacon-ipsum.p.rapidapi.com/"

    querystring = {'type': 'all-meat', 'paras': '1', 'start-with-lorem': '1', 'format': 'json'}

    headers = {
        'x-rapidapi-key': "6121edef27msh607ef4e68085a20p1db0c3jsnba630fd6ddb4",
        'x-rapidapi-host': "baconator-bacon-ipsum.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text[2:-2]
