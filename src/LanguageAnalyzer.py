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

    # TODO bound with SENTIMENT ANALYSIS + CLASSIFICATION
    def analyzeSentiment(self, messages):
        pass


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
