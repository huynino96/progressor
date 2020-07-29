import requests
from pprint import pprint

# github username
username = "huynino96"
# url to request
url = "https://api.github.com/users/huynino96"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)