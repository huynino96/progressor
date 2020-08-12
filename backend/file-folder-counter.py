import json
import requests


# Getting data from GitHub API
response = requests.get(
    "https://api.github.com/repos/visionmedia/superagent/contents")
data = json.loads(response.text)


fileFolderList = []
for i in data:
    fileFolderList.append(i["type"])


fileCount = fileFolderList.count('file')
folderCount = fileFolderList.count('dir')



childFileFolder = []
for j in data:
    if j["type"] == 'dir':
        url = j["url"]
        response1 = requests.get(str(url))
        data1 = json.loads(response1.text)
        #print(data1)
        for k in data1:
            childFileFolder.append(k["type"])

print(childFileFolder)

childFileCount = childFileFolder.count('file')
childFolderCount = childFileFolder.count('dir')

totalFiles = fileCount + childFileCount
totalFolders = folderCount + childFolderCount

print("Number of files: " + str(totalFiles))
print("Number of folders: " + str(totalFolders))
