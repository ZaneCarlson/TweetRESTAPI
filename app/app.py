from flask import Flask
from data_loader import TwitterJson
from parsers import find_all_tweets

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Welcome to the Twitter REST API"

@app.route('/all_tweets', methods=['GET'])
def get_all_tweets():
    return find_all_tweets(jsonObj.get_json())


@app.route('/external_links', methods=['GET'])
def get_external_links():
    data = jsonObj.get_json()
    return data


@app.route('/get_details', methods=['GET'])
def get_details():
    data = jsonObj.get_json()
    return data


@app.route('/get_profile', methods=['GET'])
def get_profile():
    data = jsonObj.get_json()
    return data
    

if __name__ == '__main__':
    jsonObj = TwitterJson()
    app.run()