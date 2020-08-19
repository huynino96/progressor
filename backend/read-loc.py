f = open("loc.txt", "r")

strFile = f.read()

#print(strFile)

def countLoc():
    substring = str("\\n")
    print(substring)
    newLineCounter = strFile.count(substring)
    lineOfCode = newLineCounter * 2
    print(lineOfCode)

countLoc()