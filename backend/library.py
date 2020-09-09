import requests
import base64
import json
import csv
import datetime
import constants


# API endpoint
def constructURL(user="404", repoName="404", pathToFile="404", url="404"):
    url = url.replace("{user}", user)
    url = url.replace("{repo_name}", repoName)
    url = url.replace("{path_to_file}", pathToFile)
    return url


user = 'github'
repoName = 'fetch'
pathToFile = 'package.json'
jsonUrl = constants.PACKAGE_URL

# forms the correct URL
json_url = constructURL(user, repoName, pathToFile, jsonUrl)

# get data from json file located at specified URL
response = requests.get(json_url)


if response.status_code == requests.codes.ok:
    jsonResponse = response.json()  # the response is a JSON
    # the JSON is encoded in base 64, hence decode it
    # print(jsonResponse)
    content = base64.b64decode(jsonResponse['content'])
    # convert the byte stream to string
    jsonString = content.decode('utf-8')
    finalJson = json.loads(jsonString)
else:
    print('Content not found.')

# Use only the DevDependencies
dependencies = finalJson["devDependencies"]
numLibrary = len(dependencies)

today = datetime.datetime.now()

# The lenght is the number of the libraries that have been added
with open(constants.OUTPUT_FOLDER + '/library.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Number of libraries"])
    writer.writerow([today.strftime('%x %X'), str(numLibrary)])
