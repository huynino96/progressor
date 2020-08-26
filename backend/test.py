import json
import requests
"""Fetch data from local files"""
f1 = open("masterFile.json", "r")
file1 = f1.read()
data1 = json.loads(file1)

for i in data1:
    print(type(i))