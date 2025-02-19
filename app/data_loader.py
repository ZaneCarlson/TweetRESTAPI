import json
import requests

class TwitterJson:
        response 
        def __init__():
                url = "https://foyzulhassan.github.io/files/favs.json"
                response = requests.get(url)
                response.raise_for_status()   

        def get_json():
                
                return response.json()
