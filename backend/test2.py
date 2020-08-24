import json
import requests

f = open("file3.json", "r")
file = f.read()
data = json.loads(file)

fileOnly = []
for i in data:
    for i1 in i:
        print(type(i1))
        fileOnly.append(i1)
print(len(fileOnly))
