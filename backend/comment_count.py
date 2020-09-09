"""Fetch data from local files"""
f1 = open("allFile.txt", "r")
file1 = f1.read()

substr = "// "
substr1 = "/** "

comment1 = file1.count(substr)
comment2 = file1.count(substr1)

totalCmt = comment1 + comment2
print(totalCmt)