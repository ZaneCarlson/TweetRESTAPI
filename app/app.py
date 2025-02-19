from flask import Flask
from data_loader import get_json

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Welcome to the Twitter REST API"

@app.route('/all_tweets', methods=['GET'])
def get_all_tweets():
    data = get_json()


    return data

@app.route('/external_links', methods=['GET'])
def get_all_tweets():
    data = get_json()
    return data

@app.route('/get_details', methods=['GET'])
def get_all_tweets():
    data = get_json()
    return data

@app.route('/get_profile', methods=['GET'])
def get_all_tweets():
    data = get_json()
    return data
    

if __name__ == '__main__':
    
    app.run()