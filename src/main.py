from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

hashtag_args = reqparse.RequestParser()
hashtag_args.add_argument("date", type=str, help="Date is required.", required=True)
hashtag_args.add_argument("limit", type=int, help="Amount of Tweets.", required=True)
hashtag_args.add_argument("lang", type=str, help="Tweet language is required, e.g.: pl, en...", required=True)


class HashtagRestAPi(Resource):
    def post(self, hashtag):
        hashtag_args.parse_args()
        date = request.form['date']
        limit = request.form['limit']
        lang = request.form['lang']
        #
        #
        # Processing...
        #
        #
        return {"hashtag": hashtag, "limit": limit, "date": date, "lang": lang}, 200


api.add_resource(HashtagRestAPi, "/hashtag/<string:hashtag>")

if __name__ == "__main__":
    app.run()
