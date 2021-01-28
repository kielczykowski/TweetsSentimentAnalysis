#!/usr/bin/env python3

import os
from azure.ai.textanalytics import TextAnalyticsClient, DocumentError, DetectLanguageResult
from azure.core.credentials import AzureKeyCredential


class LanguageAnalyzer(TextAnalyticsClient):

    def __init__(self, confidence_factor = 0.9, language='pl'):
        self.language_ = language
        self.confidence_ = confidence_factor
        credentials = AzureKeyCredential(os.environ["AZURE_TEXT_ANALYTICS_KEY"])
        super(LanguageAnalyzer, self).__init__(
            endpoint=os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"],
            credential=credentials
        )

    def setLanguage(self, lang):
        self.language_ = lang

    def setConfidence(self, confidence):
        self.confidence_ = confidence

    def extractLanguageDetections(self, detections):
        isSpecificLanguage = []
        for detection in detections:
            if detection.is_error is False:
                if detection.primary_language.iso6391_name == self.language_ and \
                detection.primary_language.confidence_score >= self.confidence_:
                    isSpecificLanguage.append(True)
                else:
                    isSpecificLanguage.append(False)
            elif detection.is_error is True:
                isSpecificLanguage.append(False)
        return isSpecificLanguage

    def detectLanguage(self, message):
        input_messages = message
        if type(input_messages) is not list:
            input_messages = [input_messages]

        try:
            response = self.detect_language(documents = input_messages, country_hint=self.language_)
            print(response)
            return response
        except Exception as err:
            print("Encountered exception. {}".format(type(err)))
            return None
        pass

    def analyzeSentiment(self, messages):
        if len(messages) == 0:
            return {}

        try:
            response_array = self.analyze_sentiment(documents=messages)
            if response_array is None:
                print("AnalyzeSentiment response is None.")
                return None
        except Exception as err:
            print("Encountered exception. {}".format(type(err)))
            return None

        return self.response_analyze(response_array)

    def response_analyze(self, response_array):
        sentence_list = []
        analyze_sentiment_response = {}
        analyze_sentiment_response_list = []

        for phrases in response_array:
            print("--------------------START_SENTIMENT_ANALYZE----------------------------")
            print("Azure Document Sentiment: {}".format(phrases.sentiment))
            print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f}".format(
                phrases.confidence_scores.positive,
                phrases.confidence_scores.neutral,
                phrases.confidence_scores.negative,
            ))
            print("---------------------------------")

            for idx, sentence in enumerate(phrases.sentences):
                print("Sentence: {}".format(sentence.text))
                print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
                print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}".format(
                    sentence.confidence_scores.positive,
                    sentence.confidence_scores.neutral,
                    sentence.confidence_scores.negative,
                ))
                print("---------------------------------")

                item_sentiment_score = self.calcSentimentScore(sentence.confidence_scores)
                item_sentiment = self.defineSentiment(item_sentiment_score)

                sentence_sentiment = {}
                sentence_sentiment["text"] = sentence.text
                sentence_sentiment["sentimentScore"] = item_sentiment_score
                sentence_sentiment["sentiment"] = item_sentiment

                sentence_list.append(sentence_sentiment)

            sentiment_score = self.avg(sentence_list)
            sentiment = self.defineSentiment(sentiment_score)

            analyze_sentiment_response["sentimentScore"] = sentiment_score
            analyze_sentiment_response["sentiment"] = sentiment
            analyze_sentiment_response["itemList"] = sentence_list

            print("Final Mesagges Sentiment: {}".format(sentiment))
            print("Overall scores: score={0:.2f}".format(sentiment_score))

            analyze_sentiment_response_list.append(analyze_sentiment_response)

        print("-----------------------------END---------------------------------------\n")
        return analyze_sentiment_response_list

    def calcSentimentScore(self, confidence_scores):
        return (-1 * confidence_scores.negative) + (1 * confidence_scores.positive)

    def defineSentiment(self, score):
        if score <= -0.4:
            return "negative"
        elif score >= 0.4:
            return "positive"
        else:
            return "neutral"

    @staticmethod
    def avg(item_list):
        if len(item_list) != 0:
            sum_score = 0
            weight = 0
            for item in item_list:
                # neutral phrase has lower weight: 0.3
                if item["sentiment"] == "neutral":
                    sum_score += item["sentimentScore"]
                    weight += 0.3
                else:
                    sum_score += item["sentimentScore"]
                    weight += 1

            return sum_score / weight


if __name__ == "__main__":
    language_analyzer = LanguageAnalyzer()
    x = language_analyzer.detectLanguage([
        "Lecymy dur wdupiamy żur #masno #gang",
        "Stanoski... #Najman",
        "4 piwa w cenie 1 tylko w #Biedronka",
        "#Najman to super pozytywny gość",
        "#EYPolska"
    ])
    for element in x:
        print(element)
