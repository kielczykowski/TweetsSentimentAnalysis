#!/usr/bin/env python3
from TwitterScraper import TwitterScraper
from DatabaseHandler import DatabaseHandler
from LanguageAnalyzer import LanguageAnalyzer
from datetime import date, timedelta
from Translation import Translator
from frazes_extraction_spacy import Extractor

import re


class Pipeline:

    def __init__(self):
        self.twitter_ = TwitterScraper()
        self.analyzer_ = LanguageAnalyzer()
        self.database_ = DatabaseHandler()
        self.database_.authenticate(db_name="ey")
        self.translator = Translator()
        self.extractor = Extractor()

    # call this method after calling the API
    def singleLoop(self, hashtag, language, language_confidence=0.9, number_of_tweets=100,
                since_date=date.today().strftime("%Y-%m-%d"),
                until_date=(date.today() + timedelta(days=1)).strftime("%Y-%m-%d")):

        # check language and hashtag fields from request
        if not hashtag or not language:
            raise Exception('Language and hashtag cannot be empty.')

        # SEARCHING FOR TWEETS
        found_tweets = self.twitter_.search(
            phrase=hashtag
            , since=since_date
            , until=until_date
            , language=language
            , tweets_number = number_of_tweets
        )

        # DOUBLE CHECK IF TEXT IS IN SPECIFIED LANGUAGE
        extracted_text_list = [element["text"] for element in found_tweets]

        # set language of analysis and confidence of classification
        self.analyzer_.setLanguage(language)
        self.analyzer_.setConfidence(language_confidence)

        language_detector_result = self.analyzer_.detectLanguage(extracted_text_list)
        does_language_match = self.analyzer_.extractLanguageDetections(language_detector_result)

        # Azure and Twitter language detection must match(2 factor certainty)
        found_tweets = [
            element for i,element in enumerate(found_tweets) \
            if does_language_match[i] and found_tweets[i]["twitter"]["detectedLanguage"]==language
        ]

        # remove urls
        for single_tweet in found_tweets:
            single_tweet['text'] = re.sub(r'http\S+', '', single_tweet['text'])
            single_tweet['text'] = single_tweet['text'].replace('@', '')
            single_tweet['text'] = single_tweet['text'].replace('#', '')

        # TRANSLATION TO ENGLISH
        for element in found_tweets:
            element['translated_text'] = self.translator.translate(element['text'])
            element['translated_tag'] = self.translator.translate(hashtag[1:len(hashtag)])

        # SPACY ANALYSIS
        print(found_tweets[0]['translated_text'], found_tweets[0]['translated_tag'])
        for element in found_tweets:
            element['frazes_to_sentiment_analysis'] = self.extractor.getPhrases(element['translated_text'],
                                                                                element['translated_tag'])
            # additional variable for database usage
            # analysis_output = found_tweets

            # SENTIMENT ANALYSIS + CLASSIFICATION
            element["sentiment_analysis"] = self.analyzer_.analyzeSentiment(element['frazes_to_sentiment_analysis'])

        # TODO? DATABASE HANDLING
        # self.database_.addMultipleDocuments("showcase", analysis_output)

        return found_tweets


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.singleLoop(
        '#najman'
        , 'pl'
        , since_date=(date.today() - timedelta(days=4)).strftime("%Y-%m-%d"))
