import constants

f = open(constants.INPUT_FOLDER + "/loc.txt", "r")

strFile = f.read()

# print(strFile)


def countLoc():
    ''' count line of code '''
    substring = str("\\n")
    print(substring)
    newLineCounter = strFile.count(substring)
    lineOfCode = newLineCounter * 2
    print(lineOfCode)


countLoc()