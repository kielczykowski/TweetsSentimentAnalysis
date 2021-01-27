from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

hashtag_args = reqparse.RequestParser()
hashtag_args.add_argument("hashtag", type=str, help="'hashtag' param is required.", required=True)
hashtag_args.add_argument("date", type=str, help="'date' param is required.", required=True)
hashtag_args.add_argument("limit", type=int, help="'limit' param is required.", required=True)
hashtag_args.add_argument("language", type=str, help="'lang' param is required.", required=True)


class HashtagRestAPi(Resource):
    def get(self):
        hashtag_args.parse_args()
        hashtag = request.args['hashtag']
        limit = request.args['limit']
        date = request.args['date']
        lang = request.args['language']
        #
        #
        # Processing...
        #
        #
        return {"hashtag": hashtag, "limit": limit, "date": date, "lang": lang}, 200


api.add_resource(HashtagRestAPi, "/analyze")

if __name__ == "__main__":
    app.run()
