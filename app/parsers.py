import json
from flask import jsonify


def find_all_tweets(json):
    data = []
    for tweet in json:
        data.append({
            'Time Created:': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        })
    return jsonify(data)