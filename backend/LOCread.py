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

print(type(itemList))

fileOnly = []

folderOnly = []
for k in itemList:
    if k["type"] == 'file':
        fileOnly.append(k)
    if k["type"] == 'dir':
        folderOnly.append(k)    

fileOny1 = []
folderOnly2 = []


for seconLayerFolder in folderOnly:
    if seconLayerFolder["type"] == 'file':
        fileOny1.append(seconLayerFolder)
    if seconLayerFolder["type"] == 'dir':
        folderOnly2.append(seconLayerFolder)



print(fileOnly)




