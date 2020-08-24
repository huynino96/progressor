import json
import requests

f = open("secondLayerContent.json", "r")
file = f.read()
data = json.loads(file)

for i in data:
    print(type(i))
