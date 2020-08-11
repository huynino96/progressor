import json
import requests


# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/andris9/fetch/contents")
# print(response)
users = json.loads(response.text)

# print(type(users))
# print(users)
textList = []
for d in users:
    x = str(d["name"])

    url = "https://api.github.com/repos/andris9/fetch/contents/{x}"
    endUrl = url.replace('{x}', x)

    response1 = requests.get(endUrl)
    allText = json.loads(response1.text)
    textList.append(allText)

strText = str(textList)


f = open("loc.txt", "x")
f = open("loc.txt", "w")
f.write(strText)
f.close
