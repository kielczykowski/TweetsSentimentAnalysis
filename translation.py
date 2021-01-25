import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "YOUR_RESOURCE_LOCATION"

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
    'tag': '', #tu należy podać tag
    'text': '' #tu należy podać treść tweeta
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
