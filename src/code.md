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

## Local Flask app run

In case to run Flask application please:
* make sure that You have `FLASK_APP` environment varialbe set
* `flask run` command