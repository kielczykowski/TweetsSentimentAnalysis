import requests, uuid, json

class Translator:
    def __init__(self):
        self.subscription_key = "88390c3221394049b65cbd0297e94b79"
        self.endpoint =  "https://api.cognitive.microsofttranslator.com"
        self.location ="westeurope"
# # Add your subscription key and endpoint
# subscription_key = "88390c3221394049b65cbd0297e94b79"
# endpoint = "https://api.cognitive.microsofttranslator.com"

# # Add your location, also known as region. The default is global.
# # This is required if using a Cognitive Services resource.
# location = "westeurope"

# 

    def translate(self, text):
        path = '/translate'
        constructed_url = self.endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'pl',
            'to': 'en'
        }
        constructed_url = self.endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text #tu należy podać treść tweeta lub treść taga. Raczej trzeba to robić osobno
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        request = request.json()
        translation = request[0]['translations'][0]['text']
        # print(type(translation))
        return translation

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


# struktura końcowa
# [
#     {
#         "translations": [
#             {
#                 "text": "I love ice cream.",
#                 "to": "en"
#             },
#         ]
#     }
# ]
