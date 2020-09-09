import json
import requests
import base64
import constants

# Getting data from GitHub API
response = requests.get(constants.CONTENT_URL)
data = json.loads(response.text)


itemList = []
urlList = []

for i in data:
    url = i["url"]
    urlList.append(url)
    # print(url)


def writeUrlToTxt():
    ''' Write url to text file '''
    f = open(constants.INPUT_FOLDER + "/file.txt", "x")
    f = open(constants.INPUT_FOLDER + "/file.txt", "w")
    urltextList = f.write(str(urlList))


writeUrlToTxt()

# urlString = str(urlInt)
# print(urlString.split(","))


def getUrl():
    ''' Get url of responding '''
    for url in urlList:
        response1 = requests.get(str(url))
        data1 = json.loads(response1.text)
        itemList.append(data1)


getUrl()


with open(constants.OUTPUT_FOLDER + '/data.json', 'w', encoding='utf-8') as f:
    json.dump(itemList, f, ensure_ascii=False, indent=4)


# fileOnly = []
# folderOnly = []


# def firstLayerCount():
#     for itemIndex1 in itemList:
#         for itemIndex2 in itemIndex1:
#             print(type(itemIndex2))
#             if itemIndex2["type"] == 'file':
#                 fileOnly.append(itemIndex2)
#             if itemIndex2["type"] == 'dir':
#                 folderOnly.append(itemIndex2)

# firstLayerCount()

# fileOny1 = []
# folderOnly2 = []

# def secondLayerCount():
#     for seconLayerFolder in folderOnly:
#         if seconLayerFolder["type"] == 'file':
#             fileOny1.append(seconLayerFolder)
#         if seconLayerFolder["type"] == 'dir':
#             folderOnly2.append(seconLayerFolder)


# secondLayerCount()


# print(fileOnly)
