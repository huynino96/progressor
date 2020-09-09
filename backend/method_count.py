import requests
import base64
import json
import constants
import csv
import os
import datetime

"""Fetch data from local files"""
f1 = open(constants.INPUT_FOLDER + "/allFile.txt", "r")
file1 = f1.read()

substr1 = "function(){"
substr2 = "=> {"
substr3 = "function ("


funcCount = file1.count(substr1)
funcCount1 = file1.count(substr3)
arrowFuncCount = file1.count(substr2)

totalFunc = funcCount + arrowFuncCount + funcCount1

today = datetime.datetime.now()

# File CSV
filePath = constants.OUTPUT_FOLDER + '/methods.csv'
fileEmpty = True
try:
    fileEmpty = os.stat(filePath).st_size == 0
except:
    fileEmpty = True

# The lenght is the number of the method that have been added
with open(filePath, 'a', newline='') as file:
    writer = csv.writer(file)
    if fileEmpty:
        writer.writerow(["Date", "Number of methods"])
    writer.writerow([today.strftime('%x %X'), str(totalFunc)])
