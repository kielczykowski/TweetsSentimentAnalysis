import importlib
import tweepy

class TwitterScraper:
    def __init__(self):
        auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
        auth.set_access_token(config.api_token, config.api_secret_token)

        self.api = tweepy.API(auth)

    def search(self, phrase = "#najman", since="2019-12-01"):
        found_tags = []
        for tweet in tweepy.Cursor(self.api.search, phrase, count = 100, since = since).items():
            print('Hashtags: ', tweet.entities.get('hashtags'), 'Text: ', tweet.text)
            temp = {}
            temp["hashtags"] = tweet.entities.get('hashtags')
            temp["contents"] = tweet.text
            found_tags.append(temp)
        self.found_tags = found_tags
        return found_tags


if __name__ == "__main__":
    search = TwitterScraper()
    tweets = search.search()
    print(len(tweets))
