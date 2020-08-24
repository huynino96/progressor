import json
import requests

f = open("masterFile.json", "r")
file = f.read()
data = json.loads(file)

listOnly = []
fileOnly =[]
def getList():
    for i in data:
        if isinstance(i, list):
            listOnly.append(i)
        else:
            fileOnly.append(i)

getList()

urlList = []
def getUrl():
    for i1 in listOnly:
        for i2 in i1:
            url = i2["url"]
            urlList.append(url)

getUrl()


fileData = []
def getFile():
    for url in urlList:
        response = requests.get(str(url))
        data = json.loads(response.text)
        fileData.append(data)

getFile()

masterFile1 = fileOnly +fileData
with open('newMasterFile.json', 'w', encoding='utf-8') as f:
    json.dump(masterFile1, f, ensure_ascii=False, indent=4)
