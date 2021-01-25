#!/usr/bin/env python3

import importlib
import tweepy
from datetime import date, timedelta
import json
import os

class TwitterScraper:
    def __init__(self):
        api_key = os.environ["TWITTER_API_KEY"]
        api_secret_key = os.environ["TWITTER_API_SECRET_KEY"]
        api_token = os.environ["TWITTER_API_TOKEN"]
        api_secret_token = os.environ["TWITTER_API_SECRET_TOKEN"]
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(api_token,  api_secret_token)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)  # wait_on_rate_limit - waits until 15 minutes rate limit gets refreshed

    def search(self, phrase="#najman", since=date.today().strftime("%Y-%m-%d")
            , until=(date.today() + timedelta(days=1)).strftime("%Y-%m-%d")  # until today excludes todays'tweets
            , tweets_number=10, tweet_mode='extended', language='pl'):
        found_tweets = []
        for tweet in tweepy.Cursor(
                self.api.search
                , phrase
                , since = since
                , until=until, lang=language
                , tweet_mode=tweet_mode).items(tweets_number):
            temp = {}
            temp["id"] = tweet.id
            temp["query"] = phrase
            temp["creationTime"] = str(tweet.created_at)
            if 'retweeted_status' in dir(tweet):
                temp["text"] = tweet.retweeted_status.full_text
            else:
                temp["text"] = tweet.full_text

            temp["twitter"] = {}
            temp["twitter"]["detectedLanguage"] = tweet.lang
            temp["twitter"]["hashtags"] = tweet.entities.get('hashtags')
            if tweet.place is not None:
                temp["twitter"]["place"] = {
                    key:getattr(tweet.place, key) for key in ['place_type', 'name', 'full_name', 'country']
                }
                temp["twitter"]["place"]["coordinatesType"] = tweet.place.bounding_box.type
                temp["twitter"]["place"]["coordinates"] = tweet.place.bounding_box.coordinates
            found_tweets.append(temp)

        self.found_tweets = found_tweets
        return found_tweets


if __name__ == "__main__":
    search = TwitterScraper()
    tweets = search.search(phrase = '#biedronka', since="2021-01-10")
    print("\nreturned object\n")
    for element in tweets:
        print(element)
