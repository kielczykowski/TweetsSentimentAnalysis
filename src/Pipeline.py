#!/usr/bin/env python3
from TwitterScraper import TwitterScraper
from DatabaseHandler import DatabaseHandler
from LanguageAnalyzer import LanguageAnalyzer
from datetime import date, timedelta

class Pipeline:

    def __init__(self):
        self.twitter_ = TwitterScraper()
        self.analyzer_ = LanguageAnalyzer()
        self.database_ = DatabaseHandler()
        self.database_.authenticate(db_name="ey")

    # call this method after calling the API
    def singleLoop(self, hashtag, language, language_confidence=0.9, number_of_tweets=100,
                since_date=date.today().strftime("%Y-%m-%d"),
                until_date=(date.today() + timedelta(days=1)).strftime("%Y-%m-%d")):

        # TODO handle empty/null hashtag and language
        # SEARCHING FOR TWEETS
        found_tweets = self.twitter_.search(
            phrase=hashtag
            , since=since_date
            , until=until_date
            , language=language
            , tweets_number = number_of_tweets
        )

        # DOUBLE CHECK IF TEXT IS IN SPECIFIED TEXT
        extracted_text_list = [element["text"] for element in found_tweets]

        print("Extracted Text ", len(extracted_text_list))
        for i, element in enumerate(extracted_text_list):
            print(i)
            print(element)
            print(found_tweets[i]["twitter"]["detectedLanguage"])

        # set language of analysis and confidence of classification
        self.analyzer_.setLanguage(language)
        self.analyzer_.setConfidence(language_confidence)

        language_detector_result = self.analyzer_.detectLanguage(extracted_text_list)
        does_language_match = self.analyzer_.extractLanguageDetections(language_detector_result)

        print("Does language match ", len(does_language_match))
        for i, element in enumerate(does_language_match):
            print(i)
            print(element)

        # TODO think do what do we want: OR vs AND (2 factor certainty)
        # print("Azure OR Twitter Language")
        # for i, element in enumerate(does_language_match):
        #     print(i)
        #     print(element or found_tweets[i]["twitter"]["detectedLanguage"]=='pl')

        # print("Azure AND Twitter Language")
        # for i, element in enumerate(does_language_match):
        #     print(i)
        #     print(element and found_tweets[i]["twitter"]["detectedLanguage"]=='pl')

        # SPACY ANALYSIS


        analysis_output = found_tweets
        # SENTIMENT ANALYSIS



        # DATABASE HANDLING
        # self.database_.addMultipleDocuments("showcase", analysis_output)

        # RETURN API REQUEST OBJECTS


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.singleLoop(
        '#najman'
        , 'pl'
        , since_date=(date.today() - timedelta(days=4)).strftime("%Y-%m-%d"))