import importlib
import tweepy

config = importlib.__import__('twitterApiConf')

auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.api_token, config.api_secret_token)

api = tweepy.API(auth)
tweetsArray = []

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweetsArray.append(status)
        print('Hashtags: ', status.entities.get('hashtags'), 'Text: ', status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['blacklivesmatter'])
