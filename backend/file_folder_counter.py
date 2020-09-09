import json
import requests
import csv
import datetime
import constants

# Getting data from GitHub API
response = requests.get(constants.CONTENT_URL)
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
        # print(data1)
        for k in data1:
            childFileFolder.append(k["type"])

print(childFileFolder)

childFileCount = childFileFolder.count('file')
childFolderCount = childFileFolder.count('dir')

totalFiles = fileCount + childFileCount
totalFolders = folderCount + childFolderCount

print("Number of files: " + str(totalFiles))
print("Number of folders: " + str(totalFolders))

today = datetime.datetime.now()

# The lenght is the number of the libraries that have been added
with open(constants.OUTPUT_FOLDER + '/files.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Number of files"])
    writer.writerow([today.strftime('%x %X'), str(totalFiles)])

# The lenght is the number of the libraries that have been added
with open(constants.OUTPUT_FOLDER + '/folders.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Number of folders"])
    writer.writerow([today.strftime('%x %X'), str(totalFolders)])
