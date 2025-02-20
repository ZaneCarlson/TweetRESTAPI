import json
import requests


# When TwitterJson is created, it creates an instance of the json data.
# An instance of TwitterJson can retrieve the json data anytime.
class TwitterJson:
        def __init__(self):
                self.url = "https://foyzulhassan.github.io/files/favs.json"
                self.response = requests.get(self.url)
                self.response.raise_for_status()   

        def get_json(self):
                return self.response.json()
