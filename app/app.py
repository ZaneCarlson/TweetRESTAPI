from flask import Flask
from data_loader import TwitterJson
from parsers import get_all_tweets
from parsers import get_tweet_details

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Welcome to the Twitter REST API"

@app.route('/all_tweets', methods=['GET'])
def all_tweets():
    return get_all_tweets(jsonObj.get_json())


@app.route('/external_links', methods=['GET'])
def external_links():
    data = jsonObj.get_json()
    return data


@app.route('/details/<str:tweetID>', methods=['GET'])
def details(tweetID):
    return get_tweet_details(jsonObj.get_json(), tweetID)
    

@app.route('/profile', methods=['GET'])
def profile():
    data = jsonObj.get_json()
    return data
    

if __name__ == '__main__':
    jsonObj = TwitterJson()
    app.run()