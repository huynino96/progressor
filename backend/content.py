import json
import requests

f = open("masterFile.json", "r")
file = f.read()
data = json.loads(file)
contentList = []


for i in data:    
        if i2["type"] == 'content':
        fileOnly.append(i2)
        
       
