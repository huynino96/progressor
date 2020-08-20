import json
"""Fetch data from local files"""
f1 = open("data.json", "r")
file1 = f1.read()
data1 = json.loads(file1)

f2 = open("secondLayerFileDetail.json", "r")
file2 = f2.read()
data2 = json.loads(file2)
# print(data1)
"""Data of data.json coverter"""
dictOnly1 = []
listOnly1 = []
fileOnly1 = []
folderOnly1 = []
for i1 in data1:
    if isinstance(i1, list):
        listOnly1.append(i1)
    else:
        dictOnly1.append(i1)

dictOnlyData1 = []
for index1 in listOnly1:
    for j1 in index1:
        dictOnlyData1.append(j1)

totalDict1 = dictOnly1 + dictOnlyData1

for k1 in totalDict1:
    if k1["type"] == 'file':
        fileOnly1.append(k1)
    elif k1["type"] == 'dir':
        folderOnly1.append(k1)

"""Data of secondLayerFileDetail.py coverter"""
dictOnly2 = []
listOnly2 = []
fileOnly2 = []

for i2 in data2:
    if isinstance(i2, list):
        listOnly2.append(i2)
    else:
        dictOnly2.append(i2)

dictOnlyData2 = []
for index2 in listOnly2:
    for j2 in index2:
        dictOnlyData2.append(j2)

totalDict2 = dictOnly2 + dictOnlyData2

for k2 in totalDict2:
    if k2["type"] == 'file':
        fileOnly2.append(k2)


"""Count total number of files"""
masterFile = fileOnly1 + fileOnly2
print(len(masterFile))

with open('masterFile.json', 'w', encoding='utf-8') as f:
    json.dump(masterFile, f, ensure_ascii=False, indent=4)