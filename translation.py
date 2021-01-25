import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "88390c3221394049b65cbd0297e94b79"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'pl',
    'to': 'en'
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Iga Świątek wygrała Roland Garross.' #tu należy podać treść tweeta lub treść taga. Raczej trzeba to robić osobno
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


# struktura końcowa
# [
#     {
#         "translations": [
#             {
#                 "tag" : "I"
#                 "text": "I love ice cream.",
#                 "to": "en"
#             },
#         ]
#     }
# ]
