import json
import requests
import csv
import base64
import datetime
import constants


# Getting data from GitHub API
response = requests.get(constants.STATS_CONTRIBUTOR_URL)
results = json.loads(response.text)
total = 0
for result in results:
    statics = result['weeks']
    for static in statics:
        total = total + (static['a'] - static['d'])

today = datetime.datetime.now()

with open(constants.OUTPUT_FOLDER + '/loc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Total line of Code"])
    writer.writerow([today.strftime('%x %X'), str(total)])
