import json
import requests

f = open("masterFile.json", "r")
file = f.read()
data = json.loads(file)
contentList = []


for i in data:    
        if i2["type"] == 'content':
        contentList.append(i2)
        
       
# print(contentList)