import json
import requests

f = open("file.txt", "r")
file=f.read()
fileStri = file[1:-1]
fileString = fileStri.replace("\'","")
# print(fileString)
fileList = fileString.split(",")
# print(fileList)
itemList = []
def getUrl():
    for url in fileList: 
        response = requests.get(url)
        data1 = json.loads(response.text)
        # print(data1)
        itemList.append(data1)
getUrl()


def writeUrlToTxt():
    f = open("fileDetail.txt", "x")
    f = open("fileDetail.txt", "w")
    detailTextList =f.write(str(itemList))

    print(type(detailTextList))
    # urlString = str(urlInt)
    # print(urlString.split(","))

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
    for secondLayerFolder in folderOnly:
        for secondLayerFolder2 in secondLayerFolder:
            if secondLayerFolder2["type"] == 'file':
                fileOny1.append(secondLayerFolder2)
            if secondLayerFolder2["type"] == 'dir':
                folderOnly2.append(secondLayerFolder2)


secondLayerCount()

fileOny2 = []
folderOnly3 = []
def thirdLayerCount():
    for thirdLayerFolder in folderOnly3:
        for thirdLayerFolder2 in thirdLayerFolder:
            if thirdLayerFolder2["type"] == 'file':
                fileOny2.append(thirdLayerFolder2)
            if thirdLayerFolder2["type"] == 'dir':
                folderOnly3.append(thirdLayerFolder2)

thirdLayerCount()



masterFile = fileOnly + fileOny1 + fileOny2

print(masterFile)
def writeMasterFile():
    f = open("masterFile.txt", "x")
    f = open("masterFile.txt", "w")
    detailTextList =f.write(str(masterFile))
writeMasterFile()
