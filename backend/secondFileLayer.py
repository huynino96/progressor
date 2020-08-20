import json
import requests

f = open("folderInside.json", "r")
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
    for urlSecondLayer in urlList: 
        response1 = requests.get(str(urlSecondLayer))
        data = json.loads(response1.text)
        urlSecondList.append(data)
getUrl()
with open('secondLayerFileDetail.json', 'w', encoding='utf-8') as f:
    json.dump(urlSecondList, f, ensure_ascii=False, indent=4)