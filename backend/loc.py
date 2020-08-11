import json
import requests
import csv
import base64


# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/andris9/fetch/contents")
# print(response)
users = json.loads(response.text)

# print(type(users))
# print(users)
# textList = []
for d in users:
    x = str(d["name"])

    url = "https://api.github.com/repos/andris9/fetch/contents/{x}"
    endUrl = url.replace('{x}', x)

    response1 = requests.get(endUrl)
    jsonRes = response1.json()
    content = base64.b64decode(jsonRes['content'])
    jsonString = content.decode('utf-8')

    print(jsonString)

    # allText = json.loads(jsonString)
    # textList.append(allText)


# print(textList)
strText = str(jsonString)


f = open("loc.txt", "x")
f = open("loc.txt", "w")
f.write(strText)
f.close

# f = open("loc.csv", "w")
# with f:

#     writer = csv.writer(f)

#     for row in textList:
#         writer.writerow(row)
