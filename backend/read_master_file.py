import json
import requests
import base64
import constants

"""Fetch data from local files"""
f1 = open(constants.INPUT_FOLDER + "/masterFile.json", "r")
file1 = f1.read()
data1 = json.loads(file1)

content = []
for i in data1:
    j = i["content"]
    content.append(j)


allFileList = []
for indexContent in content:
    decodedContent = base64.b64decode(indexContent)
    f = open(constants.INPUT_FOLDER + "/allFile.txt", "a")
    allFileText = f.write(str(decodedContent))
