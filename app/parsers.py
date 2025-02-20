import json
from flask import jsonify


def get_all_tweets(json):
    data = []
    for tweet in json:
        data.append({
            'Time Created': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        })
    return jsonify(data)

def get_tweet_details(json, tweetID):
    data = []
    for tweet in json:
        if (tweet['id'] == tweetID):
            data.append({
                'Time Created': tweet['created_at'],
                'Text': tweet['text'],
                'ScreenName': tweet['user']['screen_name']
            })