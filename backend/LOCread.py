import json
import requests
import base64

# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/visionmedia/superagent/contents")
data = json.loads(response.text)



itemList = []
urlList = []

for i in data:
    url = i["url"]
    urlList.append(url)
        #print(url)

def writeUrlToTxt():
    f = open("file.txt", "x")
    f = open("file.txt", "w")
    f.write(urlList)

writeUrlToTxt()


    
#  def getUrl():   
#     response1 = requests.get(str(url))
#     data1 = json.loads(response1.text)
#     itemList.append(data1)

fileOnly = []
folderOnly = []


def firstLayerCount():
    for itemIndex1 in itemList:
        for itemIndex2 in itemIndex1:
            print(type(itemIndex2))
            if itemIndex2["type"] == 'file':
                fileOnly.append(itemIndex2)
            if itemIndex2["type"] == 'dir':
                folderOnly.append(itemIndex2)

firstLayerCount()

fileOny1 = []
folderOnly2 = []

def secondLayerCount():
    for seconLayerFolder in folderOnly:
        if seconLayerFolder["type"] == 'file':
            fileOny1.append(seconLayerFolder)
        if seconLayerFolder["type"] == 'dir':
            folderOnly2.append(seconLayerFolder)


secondLayerCount()


print(fileOnly)