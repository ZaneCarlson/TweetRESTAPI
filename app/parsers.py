import json
from flask import jsonify
import re

# Returns all tweets' Time Created, ID, and Text
def get_all_tweets(json):
    data = []
    for tweet in json:
        data.append({
            'Time Created': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        })
    return jsonify(data)

# Returns all external links found in tweets and seperates them by tweet ID
def get_external_links(jsonData): 
    pattern = r'https?://[^\s<>",]+'
    data = []
    for tweet in jsonData:
        links = re.findall(pattern, tweet['text'])
        data.append({
            'id': tweet['id'],
            'links': links
        })
    return jsonify(data)

# Returns Time Created, Text, and ScreenName for a given tweet ID
def get_tweet_details(json, tweetID):
    data = []
    for tweet in json:
        if (tweet['id'] == tweetID):
            data.append({
                'Time Created': tweet['created_at'],
                'Text': tweet['text'],
                'ScreenName': tweet['user']['screen_name']
            })
    return jsonify(data)

# Returns location, description, follower count, and friend count for a given userID
def get_profile_details(json, userID):
    data = []
    for tweet in json:
        if (tweet['user']['screen_name'] == userID):
            data.append({
                'location': tweet['user']['location'],
                'description': tweet['user']['description'],
                'followers_count': tweet['user']['followers_count'],
                'friends_count': tweet['user']['friends_count']   
            })
            return jsonify(data)
    return jsonify("Could not find a profile by that name!")
    