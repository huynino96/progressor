import json
import requests
import csv
import base64


# Getting data from GitHub API
response = requests.get(
    "https://api.github.com/repos/visionmedia/superagent/stats/contributors")
results = json.loads(response.text)
total = 0
for result in results:
    statics = result['weeks']
    for static in statics:
        total = total + (static['a'] - static['d'])

print('Total line of code: ' + str(total))
