import json
import requests

# Getting data from GitHub API
response = requests.get("https://api.github.com/repos/andris9/fetch/contents")
users = json.loads(response.text)
strDict = str(users)

# Counting number of Files
def countFile():
    strFile = "\'file\'"
    fileCounter = strDict.count(strFile)
    print("Number of Files: ",fileCounter)

# Counting nuber of Folders
def countFolder():
    strFolder = "\'dir\'"
    folderCounter = strFolder.count(strFolder)
    print("Number of Folders: ",folderCounter)

countFile()
countFolder()



