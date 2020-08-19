import json

f = open("data.json", "r")
file = f.read()
data = json.loads(file)

print(type(data))



