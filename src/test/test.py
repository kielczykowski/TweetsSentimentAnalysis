import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "hashtag/lewandowski",  {"limit": 100, "date": "2020-11-20", "lang": "pl"})
print(response.json())
