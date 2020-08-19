import json
import requests
import csv
import base64


# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/github/fetch/contents")
# print(response)
users = json.loads(response.text)

# https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository
# print(type(users))
# print(users)
textList = []
for d in users:
    x = str(d["name"])

    url = "https://api.github.com/repos/github/fetch/contents/{x}"
    endUrl = url.replace('{x}', x)

    response1 = requests.get(endUrl)
    jsonRes = response1.json()
    #allText = json.loads(jsonRes)
    textList.append(jsonRes)


for word in textList:
    print(word)
    # content = base64.b64decode(jsonRes['content'])
    # jsonString = content.decode('utf-8')

    # allText = json.loads(jsonString)


print(textList)


# print(textList)
# strText = str(jsonString)


# f = open("loc.txt", "x")
# f = open("loc.txt", "w")
# f.write(strText)
# f.close

# f = open("loc.csv", "w")
# with f:

#     writer = csv.writer(f)

#     for row in textList:
#         writer.writerow(row)
