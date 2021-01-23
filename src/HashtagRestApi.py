from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

hashtag_args = reqparse.RequestParser()
hashtag_args.add_argument("date", type=str, help="'date' parameter is required - date", required=True)
hashtag_args.add_argument("limit", type=int, help="'limit' parameter is required - amount of Tweets.", required=True)
hashtag_args.add_argument("language", type=str, help="'lang' tweet language is required, e.g.: pl, en...", required=True)


class HashtagRestAPi(Resource):
    def post(self, hashtag):
        hashtag_args.parse_args()
        limit = request.args['limit']
        date = request.args['date']
        lang = request.args['language']
        #
        #
        # Processing...
        #
        #
        return {"hashtag": hashtag, "limit": limit, "date": date, "lang": lang}, 200


api.add_resource(HashtagRestAPi, "/hashtag/<string:hashtag>")

if __name__ == "__main__":
    app.run()
