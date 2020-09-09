import requests
import base64
import json

"""Fetch data from local files"""
f1 = open("allFile.txt", "r")
file1 = f1.read()

substr1 = "function(){"
substr2 = "=> {"
substr3 = "function ("


funcCount = file1.count(substr1)
funcCount1 = file1.count(substr3)
arrowFuncCount = file1.count(substr2)

totalFunc = funcCount + arrowFuncCount + funcCount1
print(totalFunc)

