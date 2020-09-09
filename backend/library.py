import requests
import base64
import json
import csv
import datetime
import constants
import os

# get data from json file located at specified URL
response = requests.get(constants.PACKAGE_URL)

jsonResponse = response.json()  # the response is a JSON
# the JSON is encoded in base 64, hence decode it
# print(jsonResponse)
content = base64.b64decode(jsonResponse['content'])
# convert the byte stream to string
jsonString = content.decode('utf-8')
finalJson = json.loads(jsonString)

# Use only the DevDependencies
dependencies = finalJson["devDependencies"]
numLibrary = len(dependencies)

today = datetime.datetime.now()

# File CSV
filePath = constants.OUTPUT_FOLDER + '/library.csv'
fileEmpty = True
try:
    fileEmpty = os.stat(filePath).st_size == 0
except:
    fileEmpty = True

# The lenght is the number of the libraries that have been added
with open(filePath, 'a', newline='') as file:
    writer = csv.writer(file)
    if fileEmpty:
        writer.writerow(["Date", "Number of libraries"])
    writer.writerow([today.strftime('%x %X'), str(numLibrary)])
