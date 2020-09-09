import json
import requests
import constants

f = open(constants.INPUT_FOLDER + "/folderInside.json", "r")
file = f.read()
folderInside = json.loads(file)
urlList = []
for listIndex in folderInside:
    for i in listIndex:
        urlSecondLayer = i["url"]
        urlList.append(urlSecondLayer)
    #    print(urlSecondLayer)
urlSecondList = []
# print(urlList)


def getUrl():
    ''' get url of second plauyer '''
    for urlSecondLayer in urlList:
        response1 = requests.get(str(urlSecondLayer))
        data = json.loads(response1.text)
        urlSecondList.append(data)


getUrl()
with open(constants.INPUT_FOLDER + '/secondLayerFileDetail.json', 'w', encoding='utf-8') as f:
    json.dump(urlSecondList, f, ensure_ascii=False, indent=4)
