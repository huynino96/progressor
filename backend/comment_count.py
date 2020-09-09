import constants
import datetime
import csv
import os

"""Fetch data from local files"""
f1 = open(constants.INPUT_FOLDER + "/allFile.txt", "r")
file1 = f1.read()

substr = "// "
substr1 = "/** "

comment1 = file1.count(substr)
comment2 = file1.count(substr1)

totalComment = comment1 + comment2

today = datetime.datetime.now()

# Comments CSV
filePath = constants.OUTPUT_FOLDER + '/comments.csv'
fileEmpty = True
try:
    fileEmpty = os.stat(filePath).st_size == 0
except:
    fileEmpty = True

with open(filePath, 'a', newline='') as file:
    writer = csv.writer(file)
    if fileEmpty:
        writer.writerow(["Date", "Number of comments"])
    writer.writerow([today.strftime('%x %X'), str(totalComment)])
