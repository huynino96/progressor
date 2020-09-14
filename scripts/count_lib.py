import os
import json

def readJson():
    global data
    f = open("/Users/huyho/Documents/progressor/scripts/input/superagent/package.json", "r")
    file = f.read()
    data = json.loads(file)
readJson()




libraries = []
def count_lib():
    for i in data['dependencies']:
        libraries.append(i)

    for j in data['devDependencies']:
        libraries.append(j)

count_lib()


print("Number of Libraries: " + str(len(libraries)))

