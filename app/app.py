from flask import Flask
from data_loader import TwitterJson
from parsers import get_all_tweets, get_tweet_details, get_profile_details, get_external_links

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Welcome to the Twitter REST API options are:\n/all_tweets\n/external_links\n/details/{tweetID}\n/profile/{userID}\n"


#routes "/all_tweets" queries to the get_all_tweets parser.
@app.route('/all_tweets', methods=['GET'])
def all_tweets():
    try:
        return get_all_tweets(jsonObj.get_json())
    except Exception as e:
        return(f"Something went wrong: {e}")

#routes "/external_links" queries to the get_external_links parser.
@app.route('/external_links', methods=['GET'])
def external_links():
    try:
        return get_external_links(jsonObj.get_json())
    except Exception as e:
        return(f"Something went wrong: {e}")

#routes "/details/TweetID" queries to the get_tweet_details parser.
@app.route('/details/<int:tweetID>', methods=['GET'])
def details(tweetID):
    try:
        return get_tweet_details(jsonObj.get_json(), tweetID)
    except Exception as e:
        return(f"Something went wrong: {e}")
    
    
#routes "/profile/userID" queries to the get_profile_details parser.
@app.route('/profile/<userID>', methods=['GET'])
def profile(userID):
    try:
        return get_profile_details(jsonObj.get_json(), userID)
    except Exception as e:
        return(f"Something went wrong {e}")


# Create an instance of TwitterJson and start the server
if __name__ == '__main__':
    jsonObj = TwitterJson()
    app.run()