import json

f = open("data.json", "r")
file = f.read()
data = json.loads(file)

# print(type(data))

dictOnly = []
listOnly = []
for i in data:
    if isinstance(i, list):
        listOnly.append(i)
    else:
        dictOnly.append(i)

dictOnly1 = []
for index in listOnly:
    for i1 in index:
        dictOnly1.append(i1)

totalDict = dictOnly + dictOnly1

fileOnly = []
folderOnly = []

for i2 in totalDict:
    if i2["type"] == 'file':
        fileOnly.append(i2)
    elif i2["type"] == 'dir':
        folderOnly.append(i2)

print(folderOnly)








