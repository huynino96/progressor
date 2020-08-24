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

getList

urlList = []
def getUrl():
    for i1 in listOnly:
        for i2 in i1:
            url = i2["url"]
            urlList.append(url)

getUrl()


fileData = []

for url in urlList:
    response = requests.get(str(url))
    data = json.loads(response)
    fileData.append(data)

