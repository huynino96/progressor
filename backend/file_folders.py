import json
import requests
import constants
from marshmallow import Schema, fields

# Getting data from GitHub API
response = requests.get(constants.CONTENT_URL)
data = json.loads(response.text)
# strDict = str(users)


class ContentSchema(Schema):
    type = fields.Str()


class RootSchema(Schema):
    contents = fields.List(fields.Nested(ContentSchema))


schema = RootSchema()
result = schema.load(data)
print(result)


def countFile():
    ''' Counting number of files '''
    strFile = "\'file\'"
    fileCounter = strDict.count(strFile)
    print("Number of Files: ", fileCounter)


def countFolder():
    ''' Counting nuber of folders '''
    strFolder = "\'dir\'"
    folderCounter = strFolder.count(strFolder)
    print("Number of Folders: ", folderCounter)


# countFile()
# countFolder()
