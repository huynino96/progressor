import json
import requests
import base64

# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/visionmedia/superagent/contents")
data = json.loads(response.text)

itemList = []
for i in data:
    url = i["url"]
    #print(url)
    response1 = requests.get(str(url))
    data1 = json.loads(response1.text)
    itemList.append(data1)


fileOnly = []
folderOnly = []



for k in itemList:
    for j in k:
        if j["type"] == 'file':
            fileOnly.append(j)
        if j["type"] == 'dir':
            folderOnly.append(folderOnly)

fileOny1 = []
folderOnly2 = []


for seconLayerFolder in folderOnly:
    if seconLayerFolder["type"] == 'file':
        fileOny1.append(seconLayerFolder)
    if seconLayerFolder["type"] == 'dir':
        folderOnly2.append(seconLayerFolder)



print(fileOnly)