import requests
import json

# TODO  correct test

BASE = "http://127.0.0.1:5000/"
body = {
    'hashtag': "najman",
    'limit': "10",
    'fromDate': "2021-01-19",
    'language': "pl"
}

data = json.dumps(body)

response = requests.post(BASE + "analyze", data)

print(response.json())
