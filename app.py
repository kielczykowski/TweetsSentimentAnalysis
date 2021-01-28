from flask import Flask, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

hashtag_args = reqparse.RequestParser()

class HashtagRestAPi(Resource):
    def post(self):
        payload = request.json
        hashtag = payload['hashtag']
        limit = payload['limit']
        date = payload['fromDate']
        lang = payload['language']
        #
        #
        # Processing...
        #
        #
        return {"hashtag": hashtag, "limit": limit, "date": date, "lang": lang}, 200


api.add_resource(HashtagRestAPi, "/analyze")

if __name__ == "__main__":
    app.run()
