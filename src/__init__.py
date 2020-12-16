import importlib
import tweepy

config = importlib.__import__('twitterApiConf')

auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.api_token, config.api_secret_token)

api = tweepy.API(auth)


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    tweetsArray = []

    def on_status(self, status):
        self.tweetsArray.append(status)
        print('Hashtags: ', status.entities.get('hashtags'), 'Text: ', status.text)


myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
# myStream.filter(track=['blacklivesmatter'])

class SearchingTweetsByHashtags:

    def search(self):
        for tweet in tweepy.Cursor(api.search, q="#najman", count=100,
                                   since="2019-12-01").items():
            print('Hashtags: ', tweet.entities.get('hashtags'), 'Text: ', tweet.text)


search = SearchingTweetsByHashtags()
search.search()
