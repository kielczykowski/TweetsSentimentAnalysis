# TweetsSentimentAnalysis - code requirements


## Requirements

All scripts requirements should be placed in `requirements.txt` file. All dependencies can be installed using the following command:

``` python
pip3 install -r requirements.txt
```



### Service credentials

Every service needs to get a credential for authentication. Our script make use of the following variables that need to get filled before running Pipeline. Authentication keys need to be written into `src/config/config.py` file with the following structure

``` python

AZURE_DATABASE_URL = "key"
AZURE_DATABASE_USER = "key"
AZURE_DATABASE_PASSWORD="key"
TWITTER_API_KEY = "key"
TWITTER_API_SECRET_KEY = "key"
TWITTER_API_TOKEN = "key"
TWITTER_API_SECRET_TOKEN = "key"
AZURE_TEXT_ANALYTICS_KEY = "key"
AZURE_TEXT_ANALYTICS_ENDPOINT = "url"
TRANSLATION_SUBSCRIPTION_KEY = "key"
TRANSLATION_ENDPOIIN =  "url"
TRANSLATION_LOCATION ="key"

```


## Local pipeline usage

To run computation Pipeline locally you need to:
* have requirements installed
* fill credentials
* run `python3 Pipeline.py`

Local pipeline usage doesn't need https requests. You can specify pipeline options by changing `__main__` section in `Pipeline.py` file.
## Flask app host

### Running app

In case to run Flask application please:
* make sure that You have `FLASK_APP` environment varialbe set
* `flask run` command
### Sending request

After running the application, to test it's functionality you can send `curl` https request:

```
curl --location --request POST 'localhost' \
--header 'Content-Type: application/json' \
--header 'Cookie: ARRAffinity=432ef3d4dab42dca9b00bb4c90a041b0d3d477d7dbfaf4534da5813ade4f9397; ARRAffinitySameSite=432ef3d4dab42dca9b00bb4c90a041b0d3d477d7dbfaf4534da5813ade4f9397' \
--data-raw '{
 "hashtag": "najman",
 "limit": "10",
 "fromDate": "2021-01-19",
 "language": "pl"
}'
```

* Section `--data-raw` specifies all keys that are needed to be specified before sending request.
* In case to test app hosted on server please change localhost to server URL.
* Please keep in mind that request might take a while before showing computation result.