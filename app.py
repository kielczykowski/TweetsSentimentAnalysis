from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from src.Pipeline import Pipeline

app = Flask(__name__)
api = Api(app)

hashtag_args = reqparse.RequestParser()


class HashtagRestAPi(Resource):

    def __init__(self):
        self.pipeline_ = Pipeline()

    def post(self):
        payload = request.json
        hashtag = payload['hashtag']
        limit = payload['limit']
        date = payload['fromDate']
        language = payload['language']

        return self.pipeline_.singleLoop(
            hashtag="#" + hashtag,
            language=language,
            number_of_tweets=int(limit),
            since_date=date), 200


api.add_resource(HashtagRestAPi, "/analyze")

if __name__ == "__main__":
    app.run()
