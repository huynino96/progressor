import json
import requests
import constants

f = open(constants.INPUT_FOLDER + "/file.txt", "r")
file = f.read()
fileStri = file[1:-1]
fileString = fileStri.replace("\'", "")
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
    ''' Write url into text file '''
    f = open(constants.INPUT_FOLDER + "/fileDetail.txt", "x")
    f = open(constants.INPUT_FOLDER + "/fileDetail.txt", "w")
    detailTextList = f.write(str(itemList))

    print(type(detailTextList))
    # urlString = str(urlInt)
    # print(urlString.split(","))


fileOnly = []
folderOnly = []


def firstLayerCount():
    ''' Count first player of dir and file '''
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
    ''' Count second player of dir and file '''
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
    ''' Count third player of dir and file '''
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
    ''' Write master file '''
    f = open(constants.INPUT_FOLDER + "/masterFile.txt", "x")
    f = open(constants.INPUT_FOLDER + "/masterFile.txt", "w")
    detailTextList = f.write(str(masterFile))


writeMasterFile()
